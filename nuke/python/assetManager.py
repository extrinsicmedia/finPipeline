#!/usr/bin/env python

import nukescripts
import nuke
import re
import os
from glob import glob

### GET ENV VARS SETUP ###
finServer = os.environ.get('SERVER', None)
jobServer = os.environ.get('JOB_SERVER', None)
user = os.environ.get('USER', None)
job = os.environ.get('JOB', None)
seq = os.environ.get('SEQUENCE', None)
shot = os.environ.get('SHOT', None)

# DEFINE FACILITY ROOT
def rootDir():
    return os.environ.get('JOB_SERVER')

# DEFINE SHOT'S NUKE DIR
##### Add error Exception here if job or shot not set
def nukeDir():
    print shot
    if seq == None:
        nkDir = os.path.join( jobServer, job, os.environ.get('PROD_DIR', None), shot, 'prj', 'nuke', 'projects' )
    else:
        nkDir = os.path.join( jobServer, job, os.environ.get('PROD_DIR', None), seq, shot, 'prj', 'nuke', 'projects' )
        
    if not os.path.isdir( nkDir ):
        print "Starting outside jobStart system"
    return nkDir

def easySave():
    nkDir = nukeDir()
    # GET DESCRIPTION FROM USER BUT STRIP ALL WHITE SPACES
    description = nuke.getInput( 'script description', 'bashComp' ).replace( ' ', '' )

    fileSaved = False
    version = 1
    while not fileSaved:
        # CONSTRUCT FILE NAME
        if seq == None:
            nkName = '%s_%s_%s_v%02d.nk' % ( job, shot, description, version )
        else:
            nkName = '%s_%s_%s_%s_v%02d.nk' % ( job, seq, shot, description, version )
        # JOIN DIRECTORY AND NAME TO FORM FULL FILE PATH
        nkPath = os.path.join( nkDir, nkName )
        # IF FILE EXISTS VERSION UP        
        if os.path.isfile( nkPath ):
            version += 1
            continue
        # SAVE NUKE SCRIPT
        nuke.scriptSaveAs( nkPath )
        fileSaved = True
    return nkPath

# CHECK FOR VERSION IN SCRIPT NAME
def checkScriptName():
    if not re.search( r'[vV]\d+', nuke.root().name() ):
        raise NameError, 'Please include a version number and save script again.'


# GET ALL NUKE SCRIPTS FOR CURRENT SHOT
def getNukeScripts():
    nkFiles = glob( os.path.join( nukeDir(), '*.nk'  ) )
    return nkFiles


# PARSE "DATABASE" FOR AVAILABLE IMAGE SEQUENCES
def getVersions():
    '''Return a dictionary of rendered versions per type'''
    # DEFINE THE DIRECTORIES YOU WANT TO INCLUDE
    types = [ 'footage', 'graphics', 'hdri', 'render_2d', 'render_3d', 'textures' ]
    # INITIALISE THE DICTIONARY WE WILL RETURN AT THE END OF THE FUNCTION
    versionDict = {}
    # GET THE DIRECTORY BASED ON THE CURRENT SHOT ENVIRONMENT
    shotDir = os.path.join( nukeDir(), assets )
    
    # LOOP THROUGH THE FOLDERS INSIDE THE SHOT DIRECTORY AND COLLECT THE IMAGE SEQUENCES THEY CONTAIN
    for t in types:
        versionDict[t] = [] # THIS WILL HOLD THE FOUND SEQUENCES
        typeDir = os.path.join( shotDir, t ) # GET THE CURRENT DIRECTORY PATH
        for d in os.listdir( typeDir ): # LOOP THROUGH IT'S CONTENTS
            path = os.path.join( typeDir, d)
            if os.path.isdir( path ): # LOOP THROUGH SUB DIRECTORIES
                versionDict[t].append( getFileSeq( path ) ) # RUN THE getFileSeq() FUNCTION AND APPEND IT'S OUTPUT TO THE LIST

    return versionDict

# ONUSERCREATE CALLBACK FOR READ NODE
def createVersionKnobs():
    '''
    Add as callback to add user knobs in Read nodes.
    In menu.py or init.py:
       nuke.addOnUserCreate( assetManager.createVersionKnobs, nodeClass='Read' )        
    '''
    # CREATE USER KNOBS
    node = nuke.thisNode()
    tabKnob = nuke.Tab_Knob( 'DB', 'DB' )
    typeKnob = nuke.Enumeration_Knob( 'versionType', 'type', [ 'footage', 'graphics', 'hdri', 'render_2d', 'render_3d', 'textures' ] )
    updateKnob = nuke.PyScript_Knob( 'update', 'update' )
    updateKnob.setValue( 'assetManager.updateVersionKnob()' )
    versionKnob = nuke.Enumeration_Knob( '_version', 'version', [] ) # DO NOT USE "VERSION" AS THE KNOB NAME AS THE READ NODE ALREADY HAS A "VERSION" KNOB
    loadKnob = nuke.PyScript_Knob( 'load', 'load' )
    
    # ASSIGN PYTHON SCRIPT AS ONE LARGE STRING
    loadScript = '''#THIS ASSUMES NO WHITE SPACES IN FILE PATH
node = nuke.thisNode()
path, range = node['_version'].value().split()
first, last = range.split('-')
node['file'].setValue( path )
node['first'].setValue( int(first) )
node['last'].setValue( int(last) )'''

    loadKnob.setValue( loadScript )
    
    # ADD NEW KNOBS TO NODE
    for k in ( tabKnob, typeKnob, updateKnob, versionKnob, loadKnob ):
        node.addKnob( k )
    # UPDATE THE VERSION KNOB SO IT SHOWS WHAT'S ON DISK / IN THE DATABASE
    updateVersionKnob()
       
# KNOBCHANGED CALLBACK FOR CUSTOMISED READ NODE
def updateVersionKnob():
    '''
    Add as callback to list versions per type in Read node's user knob
    In menu.py or init.py:
       nuke.addKnobChanged( fin_assetManager.updateVersionKnob, nodeClass='Read' )  
    '''
    node = nuke.thisNode()
    knob = nuke.thisKnob()

    # RUN ONLY IF THE TYPE KNOB CHANGES OR IF THE NODE PANEL IS OPENED.
    if not knob or knob.name() in [ 'versionType', 'showPanel' ]:
        # GET THE VERSION DICTIONARY
        versionDict = getVersions()
        # POPULATE THE VERSION KNOB WITH THE VERSIONS REQUESTED THROUGH THE TYPE KNOB
        node['_version'].setValues( versionDict[ node['versionType'].value() ] )
        # SET THE A VALUE TO THE FIRST ITEM IN THE LIST
        node['_version'].setValue(0)

# BEFORERENDER CALLBACK FOR WRITE ASSET GIZMO
def createOutDirs():
    '''
    Create output directory if it doesn't exist.
    Add as callback to Write node's.    
    In menu.py or init.py:
       # CALLBACK VIA KNOB DEFAULT
       nuke.knobDefault( 'Write.beforeRender', 'fin_assetManager.createOutDirs()')
    OR:
       nuke.addBeforeRender( fin_assetManager.createOutDirs, nodeClass='Write' )
    '''
    trgDir = os.path.dirname( nuke.filename( nuke.thisNode() ) )
    if not os.path.isdir( trgDir ):
        os.makedirs( trgDir )               

def getFileSeq( dirPath ):
    '''Return file sequence with same name as the parent directory. Very loose example!!'''
    dirName = os.path.basename( dirPath )
    # COLLECT ALL FILES IN THE DIRECTORY THAT HVE THE SAME NAME AS THE DIRECTORY
    files = glob( os.path.join( dirPath, '%s.*.*' % dirName ) )
    # GRAB THE RIGHT MOST DIGIT IN THE FIRST FRAME'S FILE NAME
    firstString = re.findall( r'\d+', files[0] )[-1]
    # GET THE PADDING FROM THE AMOUNT OF DIGITS
    padding = len( firstString )
    # CREATE PADDING STRING FRO SEQUENCE NOTATION
    paddingString = '%02s' % padding
    # CONVERT TO INTEGER
    first = int( firstString )
    # GET LAST FRAME
    last = int( re.findall( r'\d+', files[-1] )[-1] )
    # GET EXTENSION
    ext = os.path.splitext( files[0] )[-1]
    # BUILD SEQUENCE NOTATION
    fileName = '%s.%%%sd%s %s-%s' % ( dirName, str(padding).zfill(2), ext, first, last )
    # RETURN FULL PATH AS SEQUENCE NOTATION
    return os.path.join( dirPath, fileName )

# PANEL TO SHOW NUKE SCRIPS FOR CURRENT SHOT
class NkPanel( nukescripts.PythonPanel ):
    def __init__( self, nkScripts ):
        nukescripts.PythonPanel.__init__( self, 'Open Nuke Script' )
        self.checkboxes = []
        self.nkScripts = nkScripts
        self.selectedScript = ''
        
        for i, n in enumerate( self.nkScripts ):
            # PUT INDEX INTO KNOB NAMES SO WE CAN IDENTIFY THEM LATER
            k = nuke.Boolean_Knob( 'nk_%s' % i, os.path.basename( n ) )
            self.addKnob( k )
            k.setFlag( nuke.STARTLINE )
            self.checkboxes.append( k )
 
    def knobChanged( self, knob ):
        if knob in self.checkboxes:
            # MAKE SURE ONLY ONE KNOB IS CHECKED
            for cb in self.checkboxes:
                if knob == cb:
                    # EXTRACT THE INDEX FORM THE NAME AGAIN
                    index = int( knob.name().split('_')[-1] )
                    self.selectedScript = self.nkScripts[ index ]
                    continue
                cb.setValue( False )

