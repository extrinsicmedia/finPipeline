import os
import unittest
import tempfile
import shutil

import pymel.core as pm
import maya.cmds as cmds

class testCase_references(unittest.TestCase):

    def setUp(self):
        print "getting temp dir"
        self.temp = os.path.join(tempfile.gettempdir(), 'referencesTest')
        if not os.path.isdir(self.temp):
            os.makedirs(self.temp)
        
        # create sphere file
        print "sphere file"
#        cmds.file(new=1, f=1)
        pm.newFile(f=1)
        sphere = pm.polySphere()
        # We will use this to test failed ref edits...
        pm.addAttr(sphere, ln='zombieAttr')
        self.sphereFile = pm.saveAs( os.path.join( self.temp, 'sphere.ma' ), f=1 )
        
        # create cube file
        print "cube file"
        pm.newFile(f=1)
        pm.polyCube()
        pm.createReference( self.sphereFile, namespace='sphere' )
        pm.PyNode('sphere:pSphere1').attr('translateX').set(2)
        self.cubeFile = pm.saveAs( os.path.join( self.temp, 'cube.ma' ), f=1 )
        
        # create cone file
        print "cone file"
        pm.newFile(f=1)
        pm.polyCone()
        pm.createReference( self.cubeFile, namespace='cubeInCone' )
        pm.PyNode('cubeInCone:pCube1').attr('translateZ').set(2)
        pm.PyNode('cubeInCone:sphere:pSphere1').attr('translateZ').set(2)
        self.coneFile = pm.saveAs( os.path.join( self.temp, 'cone.ma' ), f=1 )
        
        print "master file"
        pm.newFile(f=1)
        self.sphereRef1 = pm.createReference( self.sphereFile, namespace='sphere1' )
        pm.PyNode('sphere1:pSphere1').attr('translateY').set(2)
        self.sphereRef2 = pm.createReference( self.sphereFile, namespace='sphere2' )
        pm.PyNode('sphere2:pSphere1').attr('translateY').set(4)
        self.cubeRef1 = pm.createReference( self.cubeFile, namespace='cube1' )
        pm.PyNode('cube1:sphere:pSphere1').attr('translateY').set(6)
        pm.PyNode('cube1:pCube1').attr('translateY').set(6)
        self.coneRef1 = pm.createReference( self.coneFile, namespace='cone1' )
        
    def test_iterRefs_depth(self):
        # Test that each subsequent ref is either a child of the previous ref,
        # or the sibling of of some ref higher in the stack'''
        refStack = []
        for ref in pm.iterReferences(recursive=True):
            splitNS = ref.fullNamespace.split(':')
            if len(splitNS) <= len(refStack):
                refStack = refStack[:len(splitNS) - 1]
            
            self.assertEqual(splitNS[:-1], refStack)
            refStack.append(ref.namespace)

    def test_iterRefs_breadth(self):
        # Test that each subsequent ref is has a recursive depth >= the
        # previous ref
        refDepth = 0
        for ref in pm.iterReferences(recursive=True, recurseType='breadth'):
            splitNS = ref.fullNamespace.split(':')
            thisDepth = len(splitNS)
            self.assertTrue(thisDepth >= refDepth)
            refDepth = thisDepth

    def test_basic_file_cmds(self):
        print "Exporting all", os.path.join( self.temp, 'all.ma' )
        expFile = pm.exportAll( os.path.join( self.temp, 'all.ma' ), preserveReferences=1, force=1)
        print "Importing"
        impFile = pm.importFile( expFile )
        print "Exporting all" 
        pm.exportAll( os.path.join( self.temp, 'all.ma' ), preserveReferences=1, force=1)
        print "Exporting animation"
        pm.exportAnim( os.path.join( self.temp, 'anim.ma' ), force=1)
        pm.select(pm.SCENE.persp)
        print "Exporting selected animation"
        pm.exportSelectedAnim( os.path.join( self.temp, 'selAnim.ma' ), force=1)
    
    def test_file_reference(self):
        self.assert_( isinstance( self.sphereRef1, pm.FileReference ) )
        self.assert_( isinstance( self.sphereRef1.refNode, pm.PyNode ) )
        self.assert_( self.sphereRef1.namespace == 'sphere1' )
        self.assert_( self.sphereRef1.isLoaded() )
        self.sphereRef1.unload()
        self.assert_( self.sphereRef1.isDeferred() )
        self.sphereRef1.load()
        self.sphereRef1.exportAnim( os.path.join( self.temp, 'refAnim.ma' ), force=1 )
        pm.select( self.sphereRef1.nodes() )
        self.sphereRef1.exportSelectedAnim( os.path.join( self.temp, 'selRefAnim.ma' ), force=1 )
        self.sphereRef1.remove()
        self.sphereRef2.importContents()

    def test_file_reference_creation(self):
        for ref in pm.listReferences(recursive=True):
            self.assertEqual(ref, pm.FileReference(pm.PyNode(ref.refNode)))
            self.assertEqual(ref, pm.FileReference(str(ref.refNode)))
            self.assertEqual(ref, pm.FileReference(pm.Path(ref.withCopyNumber())))
            self.assertEqual(ref, pm.FileReference(str(ref.withCopyNumber())))
            self.assertEqual(ref, pm.FileReference(namespace=ref.fullNamespace))

    def test_failed_ref_edits(self):
        # Animate the zombieAttrs
        for transform in [x.getParent() for x in pm.ls(type='mesh')]:
            try:
                zombie = transform.attr('zombieAttr')
            except pm.MayaAttributeError:
                continue
            zombie.setKey(t=1, v=1)
            zombie.setKey(t=2, v=2)
            zombie.setKey(t=3, v=4)
        self.masterFile = pm.saveAs( os.path.join( self.temp, 'master.ma' ), f=1 )
        
        pm.openFile(self.sphereFile, f=1)
        pm.SCENE.pSphere1.zombieAttr.delete()
        pm.saveFile(f=1)
        
        # deleting the attr should give some failed ref edits...
        pm.openFile(self.masterFile, f=1)
        
        sphereRefs = [x for x in pm.listReferences(recursive=True)
                      if x.path.endswith('sphere.ma')]
        for ref in sphereRefs:
            print "testing failed ref edits on: %s" % ref
            self.assertEqual(1, len(pm.referenceQuery(ref,successfulEdits=False,failedEdits=True,es=True)))
            self.assertEqual(1, len(cmds.referenceQuery(str(ref.refNode), successfulEdits=False,failedEdits=True,es=True)))
        
    def tearDown(self):
        pm.newFile(f=1)
        shutil.rmtree(self.temp, ignore_errors =True)
        
class testCase_fileInfo(unittest.TestCase):
    def setUp(self):
        pm.newFile(f=1)
        cmds.fileInfo('testKey', 'testValue')
        
    def test_get(self):
        default = "the default value!"
        self.assertEqual(pm.fileInfo.get('NoWayDoIExist', default), default)
        self.assertEqual(pm.fileInfo.get('NoWayDoIExist'), None)
        self.assertEqual(pm.fileInfo.get('testKey'), cmds.fileInfo('testKey', q=1)[0])
        
    def test_getitem(self):
        self.assertRaises(KeyError, lambda: pm.fileInfo['NoWayDoIExist'])
        self.assertEqual(pm.fileInfo['testKey'], cmds.fileInfo('testKey', q=1)[0])

class testCase_namespaces(unittest.TestCase):
    recurseAvailable= ( pm.versions.current() >= pm.versions.v2011 )
    
    def setUp(self):
        cmds.file(f=1, new=1)
        cmds.namespace( add='FOO' )
        cmds.namespace( add='BAR' )
        cmds.namespace( add='FRED' )
        cmds.namespace( add='BAR', parent=':FOO')
        cmds.namespace( add='CALVIN', parent=':FOO:BAR')
        cmds.sphere( n='FOO:sphere1' )
        cmds.sphere( n='FOO:sphere2' )
        cmds.sphere( n='BAR:sphere1' )
        cmds.sphere( n='FOO:BAR:sphere1' )
        
    def test_listNodes(self):
        self.assertEqual(set(pm.Namespace('FOO').listNodes()),
                         set([pm.PyNode('FOO:sphere1'),
                              pm.PyNode('FOO:sphere1Shape'),
                              pm.PyNode('FOO:sphere2'),
                              pm.PyNode('FOO:sphere2Shape'),
                              ]))
        
        if self.recurseAvailable:
            self.assertEqual( set(pm.Namespace('FOO').listNodes(recursive=False)),
                              set([pm.PyNode('FOO:sphere1'),
                                   pm.PyNode('FOO:sphere1Shape'),
                                   pm.PyNode('FOO:sphere2'),
                                   pm.PyNode('FOO:sphere2Shape'),
                                   ]))
            self.assertEqual( set(pm.Namespace('FOO').listNodes(recursive=True)),
                              set([pm.PyNode('FOO:sphere1'),
                                   pm.PyNode('FOO:sphere1Shape'),
                                   pm.PyNode('FOO:sphere2'),
                                   pm.PyNode('FOO:sphere2Shape'),
                                   pm.PyNode('FOO:BAR:sphere1'),
                                   pm.PyNode('FOO:BAR:sphere1Shape'),
                              ]))
    def test_listNamespaces(self):
        self.assertEqual(set(pm.Namespace('FOO').listNamespaces()),
                         set([pm.Namespace('FOO:BAR'),
                              ]))
        
        if self.recurseAvailable:
            self.assertEqual(set(pm.Namespace('FOO').listNamespaces(recursive=False)),
                             set([pm.Namespace('FOO:BAR'),
                                  ]))
            self.assertEqual(set(pm.Namespace('FOO').listNamespaces(recursive=True)),
                             set([pm.Namespace('FOO:BAR'),
                                  pm.Namespace('FOO:BAR:CALVIN')
                                  ]))
