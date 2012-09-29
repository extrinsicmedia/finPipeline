#! /usr/autodesk/maya2008-x64/bin/mayapy

import sys, os, inspect, unittest
from pymel.all import *

class test_PMTypes(unittest.TestCase):

    def setUp(self):
        self.eu = datatypes.Vector(1,2,3)
        self.r = datatypes.Point([0.25, 0.5, 1.0, 0.5])
        self.u = datatypes.Vector()
        self.v = datatypes.Vector()
        self.n = datatypes.Vector()
        self.w = datatypes.Vector()
        self.p = datatypes.Point()
        self.q = datatypes.Quaternion()
        self.m = datatypes.Matrix()
        self.M = api.MTransformationMatrix()
        self.V = datatypes.VectorN()
        self.t = api.MTransformationMatrix()


    def tearDown(self):
        pass

############################################################# 
## MVector tests 

    #def testMVector_dir(self):
    #    self.assertEqual(dir(self.u), dir(datatypes.Vector)) # currently errors - 'this' is not present in Vector

    def testMVector_attrs(self):
        self.assertEqual(self.u.shape, datatypes.Vector.shape)
        self.assertEqual(self.u.ndim, datatypes.Vector.ndim)
        self.assertEqual(self.u.size, datatypes.Vector.size)
        self.u.assign(datatypes.Vector(1, 2, 3))
        self.assertEqual(self.u.x, 1.0)
        self.assertEqual(self.u.y, 2.0)
        self.assertEqual(self.u.z, 3.0)

    def testMVector_instance(self):
        # The default class constructor. Creates a null vector. 
        self.u = datatypes.Vector()
        self.assertEqual(self.u, datatypes.Vector())

        # The copy constructor. Create a new vector and initialize it to the same values as the given vector.
        self.u.assign(datatypes.Vector(4, 5, 6))
        self.assertEqual(self.u, datatypes.Vector([4.0, 5.0, 6.0]))

        # The copy constructor. Create a new vector and initialize it to the same values as the given vector.
        self.u = datatypes.Vector(1, 2, 3)
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

        # Class constructor. Initializes the vector with the explicit x, y and z values provided as arguments.
        self.u = datatypes.Vector(x=1, y=2, z=3)
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

        # Class constructor. Initializes the vector with the explicit x, y and z values provided in the given double array.
        self.u = datatypes.Vector([1, 2], z=3)
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

        # Class constructor. Initializes the vector with the explicit x, y and z values provided in the given double array.
        self.u[0:2] = [1,1]
        self.assertEqual(self.u, datatypes.Vector([1.0, 1.0, 3.0]))

        # The index operator. If its argument is 0 it will return the x component of the vector. If its argument is 1 it will return the y component of the vector. Otherwise it will return the z component of the vector.
    def testMVector_indexOperatorAccess(self):
        self.assertEqual(self.eu(0), 1)
        self.assertEqual(self.eu(1), 2)
        self.assertEqual(self.eu(2), 3)
        self.assertEqual(self.eu(21), 3)

        self.assertEqual(self.eu[0], 1)
        self.assertEqual(self.eu[1], 2)
        self.assertEqual(self.eu[2], 3)

        # Vector from Point
    def testMVector_instanceFromPoint(self):
        self.u = datatypes.Vector(datatypes.Point(1, 2, 3))
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))  

        # vector from API point
    def testMVector_instanceMPoint(self):
        self.u = datatypes.Vector(api.MPoint(1, 2, 3))
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

        # Vector from VectorN
    def testMVector_instanceVectorN(self):
        self.u = datatypes.Vector(datatypes.VectorN(1, 2, 3))
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

        # Vector from Single Float
    def testMVector_instance_from_singleFloat(self):
        self.u = datatypes.Vector(1)
        self.assertEqual(self.u, datatypes.Vector([1.0, 1.0, 1.0]))

        # 
    def testMVector_instance_from_VectorOfLengthTwo(self):
        # Z defaults to 0.0
        self.u = datatypes.Vector(1,2)
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 0.0]))

    def testMVector_instanceVectorN2(self):
        self.u = datatypes.Vector(datatypes.VectorN(1, shape=(2,)))
        self.assertEqual(self.u, datatypes.Vector([1.0, 1.0, 0.0])) 

        # construct from Point, overriding individual axis values
    def testMVector_instancePoint2(self):
        self.u = datatypes.Vector(datatypes.Point(1, 2, 3, 1), y=20, z=30)
        self.assertEqual(self.u, datatypes.Vector([1.0, 20.0, 30.0]))

        # assign value through index access
    def testMVector_indexAssign(self):
        self.u = datatypes.Vector(1, 20, 30)
        self.u[0] = 10
        self.assertEqual(self.u, datatypes.Vector([10.0, 20.0, 30.0]))

    def testMVector_IOBAssign(self):
        def IOBtest(): 
            self.u = datatypes.Vector(datatypes.VectorN(1, 2, 3, 4))
        self.failUnlessRaises(TypeError,IOBtest)  # fails with TypeError, was expecting ValueError

    def testMVector_in(self):
        self.assert_(1.0 in self.eu) 

    def testMVector_list(self):
        self.assertEqual(list(self.eu),[1.0, 2.0, 3.0] )

    def testMVector_len(self):
        self.assertEquals(len(self.eu), 3)

    # Ensure that isInstance recognizes u, tests inheritance
    def testMVector_isInstances(self):
        self.assertTrue( isinstance(self.eu, datatypes.VectorN))
        self.assertTrue( isinstance(self.u, datatypes.Array))
        self.assertTrue( isinstance(self.u, api.MVector))        

    # Create Vector from api.MPoint
    def testMVector_instanceAPI(self):
        self.u = datatypes.Vector(api.MPoint(1, 2, 3))
        self.assertEqual(self.u, datatypes.Vector([1.0, 2.0, 3.0]))

#    def testMVector_translateAPI(self):
#        self.u = datatypes.Vector(api.MPoint(1, 2, 3))
#        #self.M.setTranslation ( self.u, api.MSpace.kWorld )
#        self.u = Vector(self.M.getTranslation ( api.MSpace.kWorld ))
#        self.assertEqual(self.u, Vector([1.0, 2.0, 3.0]))

    def testMVector_Axis(self):
        self.u = datatypes.Vector.xAxis
        self.v = datatypes.Vector.yAxis
        self.assertEqual(self.u, datatypes.Vector([1.0, 0.0, 0.0]))
        self.assertEqual(self.v, datatypes.Vector([0.0, 1.0, 0.0]))  

    def testMVector_crossProduct(self):
        self.u = datatypes.Vector.xAxis
        self.v = datatypes.Vector.yAxis
        self.n = self.u ^ self.v
        self.assertEqual(self.n, datatypes.Vector([0.0, 0.0, 1.0]))
        self.n = self.u ^ datatypes.VectorN(self.v)
        self.assertEqual(self.n, datatypes.Vector([0.0, 0.0, 1.0]))
        self.n = self.u ^ [0, 1, 0]
        self.assertEqual(self.n, datatypes.Vector([0.0, 0.0, 1.0]))

    def testMVector_dotProduct(self):
        self.n = datatypes.Vector([1.0, 1.0, 1.0])
        self.n = self.n * 2
        self.assertEqual(self.n, datatypes.Vector([2.0, 2.0, 2.0]))
        self.n = self.n * [0.5, 1.0, 2.0]
        self.assertEqual(self.n, datatypes.Vector([1.0, 2.0, 4.0]))
        self.n = self.n * self.n
        self.assertEqual(self.n, 21)

    def testMVector_clamp(self):
        self.n = datatypes.Vector([1.0, 3.0, 4.0])
        self.assertEqual((self.n.clamp(1.0, 2.0)),datatypes.Vector([1.0, 2.0, 2.0]))

    def testMVector_neg(self):
        self.n = datatypes.Vector([1.0, 3.0, 4.0])
        self.assertEqual(-self.n,datatypes.Vector([-1.0, -3.0, -4.0]))

    def testMVector_add(self):
        self.u = datatypes.Vector.xAxis
        self.v = datatypes.Vector.yAxis
        self.w = self.u + self.v
        self.assertEqual(self.w,datatypes.Vector([1.0, 1.0, 0.0]))
        
        self.u = datatypes.Vector.xAxis
        self.assertEquals(self.u + 2,datatypes.Vector([3.0, 2.0, 2.0]))
        self.assertEquals(2 + self.u,datatypes.Vector([3.0, 2.0, 2.0]))
        self.assertEquals((self.u + [0.01, 0.01, 0.01]), datatypes.Vector([1.01, 0.01, 0.01]))        

    def testMVectorPoint_add(self):
        self.u = datatypes.Vector.xAxis
        self.p = datatypes.Point(1, 2, 3)

        self.q = self.u + self.p
        self.assertEqual(self.q, datatypes.Point([2.0, 2.0, 3.0]))
        self.q = self.p + self.u
        self.assertEquals(self.q, datatypes.Point([2.0, 2.0, 3.0]))

        self.assertEquals((self.q + self.p), datatypes.Point([3.0, 4.0, 6.0]))
        self.assertEquals((self.p + self.q), datatypes.Point([3.0, 4.0, 6.0]))
        self.assertEquals((self.p + self.u), datatypes.Point([2.0, 2.0, 3.0]))

        self.assertEquals(datatypes.VectorN(1, 2, 3, 4) + self.u, datatypes.VectorN([2.0, 2.0, 3.0, 4])) # TODO want Point returned, rather than VectorN
        self.assertEquals([1, 2, 3] + self.u, datatypes.Vector([2.0, 2.0, 3.0])) # TODO want Point returned, rather than Vector

    def testMVector_and_VectorN(self):
        self.u = datatypes.Vector.xAxis
        self.w = self.u + datatypes.VectorN(1, 2, 3, 4)
        self.assertEquals(self.w, datatypes.VectorN([2.0, 2.0, 3.0, 4])) 

    def testMVector_length(self):  
        self.u = datatypes.Vector(1, 2, 3)
        self.assertEquals(self.u, datatypes.Vector([1.0, 2.0, 3.0]))
        self.assertAlmostEquals(self.u.length(), 3.74165738677 ) 
        self.assertAlmostEquals(datatypes.Vector.length(self.u), 3.74165738677 ) 
        #self.assertAlmostEquals(datatypes.Vector.length([1,2,3]), 3.74165738677 )  # TODO :: TypeError: unbound method length() must be called with Vector instance as first argument (got list instance instead)
        self.assertAlmostEquals(datatypes.length(datatypes.VectorN(1,2,3)), 3.74165738677) 
        self.assertAlmostEquals(datatypes.VectorN(1,2,3).length(), 3.74165738677) 
        self.assertAlmostEquals(datatypes.VectorN.length(datatypes.VectorN(1,2,3,4)), 5.47722557505) 
        self.assertAlmostEquals(datatypes.VectorN(1, 2, 3, 4).length(), 5.47722557505)
        self.assertEquals(datatypes.length(1), 1.0) 
        self.assertAlmostEquals(datatypes.length([1,2]),2.2360679775)
        self.assertAlmostEquals(datatypes.length([1,2,3]), 3.74165738677)
        self.assertAlmostEquals(datatypes.length([1,2,3,4]), 5.47722557505)
        self.assertAlmostEquals(datatypes.length([1,2,3,4], 0), 5.47722557505)
        self.assertAlmostEquals(datatypes.length([1,2,3,4], (0,)), 5.47722557505)

        def AxisValTest(): # Axis must be value '0' for all Vectors
            datatypes.length([1, 2, 3, 4], 1)
        self.failUnlessRaises(ValueError,AxisValTest)  # ValueError: axis 0 is the only valid axis for a VectorN, 1 invalid

    def testMVector_sqlength(self):
        self.u = datatypes.Vector(1,2,3)
        self.assertEquals(self.u.sqlength(), 14.0)

    def testMVector_axis(self):
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707)
        self.assertEqual(datatypes.axis(self.u, self.v), datatypes.Vector([-0.0, 0.707, 0.0]))
        self.assertEqual(self.u.axis(self.v), datatypes.Vector([-0.0, 0.707, 0.0]))
        self.assertEqual(datatypes.axis(datatypes.VectorN(self.u), datatypes.VectorN(self.v)), datatypes.VectorN([-0.0, 0.707, 0.0]))
        self.assertEqual(datatypes.axis(datatypes.VectorN(self.u), datatypes.VectorN(self.v)), datatypes.VectorN([-0.0, 0.707, 0.0]))
        first = datatypes.axis(self.u, self.v, normalize=True)
        last = datatypes.Vector([-0.0, 1.0, -0.0])
        self.assert_(first.isEquivalent(last))
        
        first = self.v.axis(self.u, normalize=True)
        last = datatypes.Vector([-0.0, -1.0, 0.0])
        self.assert_(first.isEquivalent(last))
        
        first = datatypes.axis(datatypes.VectorN(self.u), datatypes.VectorN(self.v), normalize=True)
        last = datatypes.VectorN([-0.0, 1.0, 0.0])
        self.assert_(first.isEquivalent(last))

    def testMVector_angle(self):
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707)
        self.assertAlmostEquals(datatypes.angle(self.u,self.v), 0.785398163397 )
        self.assertAlmostEquals(self.v.angle(self.u), 0.785398163397 )
        self.assertAlmostEquals(datatypes.angle(datatypes.VectorN(self.u),datatypes.VectorN(self.v)),0.785398163397 )
        self.assertEquals(datatypes.cotan(self.u, self.v), 1.0)

    def testMVector_angleRotateTo(self):
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707)
        
        first = self.u.rotateTo(self.v)
        last = datatypes.Quaternion([-0.0, 0.382683432365, 0.0, 0.923879532511])
        self.assert_(first.isEquivalent(last))

    def testMVector_angleRotateBy(self):
        u = datatypes.Vector(1, 0, 0)
        v = datatypes.Vector(0.707, 0, -0.707)

        first = u.rotateBy(u.axis(v), u.angle(v))
        last = datatypes.Vector([0.707106781187, 0.0, -0.707106781187])

        self.assert_(first.isEquivalent(last))
                          
        q = datatypes.Quaternion([-0.0, 0.382683432365, 0.0, 0.923879532511])
        
        first = u.rotateBy(q)
        last = datatypes.Vector([0.707106781187, 0.0, -0.707106781187])
        self.assert_(first.isEquivalent(last))


    def testMVector_angleDistanceTo(self):
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707)
        self.assertAlmostEquals(self.u.distanceTo(self.v),0.765309087885)

    def testMVector_angleParallel(self):
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707)  
        self.assertFalse(self.u.isParallel(self.v))
        self.assertTrue(self.u.isParallel(2*self.u))

    def testMVector_normal(self):
        self.u = datatypes.Vector(1,2,3)
        first = self.u.normal()
        last = datatypes.Vector([0.267261241912, 0.534522483825, 0.801783725737])
        self.assert_(first.isEquivalent(last))

    def testMVector_normalize(self): 
        self.u = datatypes.Vector(1,2,3)
        self.u.normalize()
        last = datatypes.Vector([0.267261241912, 0.534522483825, 0.801783725737])
        self.assert_(self.u.isEquivalent(last))   

    def testMVector_equality(self): 
        self.u = datatypes.Vector(1,2,3)
        self.w = self.u + datatypes.VectorN(1, 2, 3, 4)
        self.assert_(self.u == self.u)
        self.assert_(self.u != self.w)
        self.assert_(self.u == datatypes.Vector(1.0, 2.0, 3.0))
        #self.failIfEqual(self.u == [1.0, 2.0, 3.0])
        self.assert_(self.u != [1.0, 2.0, 3.0])
        self.assert_(self.u != datatypes.Point(1.0, 2.0, 3.0))
        self.assertTrue(self.u.isEquivalent([1.0, 2.0, 3.0]))
        self.assertTrue(self.u.isEquivalent(datatypes.Vector(1.0, 2.0, 3.0)))
        self.assertTrue(self.u.isEquivalent(datatypes.Point(1.0, 2.0, 3.0)))
        #self.assertFalse(self.u.isEquivalent(self.w)) # TODO :: TypeError: super(type, obj): obj must be an instance or subtype of type
        #self.assertTrue(self.u.isEquivalent(self.w, 0.1)) # TODO :: TypeError: super(type, obj): obj must be an instance or subtype of type

    def testMVector_angleBlend(self): 
        self.u = datatypes.Vector(1, 0, 0)
        self.v = datatypes.Vector(0.707, 0, -0.707) 
        goop = datatypes.Vector([0.8535, 0.0, -0.3535])
        self.assert_(self.u.blend(self.v).data.isEquivalent(goop.data))
 
############################################################# 
## MPoint tests
         
    def testMPoint_hasAttr(self):
        self.assertTrue(hasattr(datatypes.Point,'data'))

    def testMPoint_list(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(list(self.p),[1.0, 2.0, 3.0] )

    def testMPoint_len(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(len(self.p),3)

    def testMPoint_size(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(self.p.size,4)

    def testMPoint_indiceAccess(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(self.p.x, 1.0)
        self.assertEquals(self.p.y, 2.0)
        self.assertEquals(self.p.z, 3.0)
        self.assertEquals(self.p.w, 1.0)

        self.assertEquals(self.p[0], 1.0)
        self.assertEquals(self.p[1], 2.0)
        self.assertEquals(self.p[2], 3.0)
        self.assertEquals(self.p[3], 1.0)

    def testMPoint_get(self):
        self.p = datatypes.Point(1,2,3)
        got = self.p.get()
        self.assert_(got == (1.0, 2.0, 3.0, 1.0))

    def testMPoint_distanceTo(self):
        self.q = api.MPoint()
        self.p = datatypes.Point(1,2,3)
        self.assertAlmostEquals(self.q.distanceTo(self.p), 3.74165738677)


    def testMPoint_NonCartesion_instance(self):
        # support for non cartesian points still there
        self.p = datatypes.Point(1, 2, 3, 2)
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0, 2.0]))

        self.v = datatypes.Vector(self.p)
        self.assertEquals(self.v, datatypes.Vector([0.5, 1.0, 1.5]))

        self.V = datatypes.VectorN(self.p)
        self.assertEquals(self.V,datatypes.VectorN([1.0, 2.0, 3.0, 2.0]))

    def testMPoint_NonCartesion_list(self):
        self.p = datatypes.Point(1, 2, 3, 2)
        self.assertEquals(list(self.p), [1.0, 2.0, 3.0, 2.0])

    def testMPoint_NonCartesion_len(self):
        self.p = datatypes.Point(1, 2, 3, 2)
        self.assertEquals(len(self.p),4)

    def testMPoint_NonCartesion_size(self):
        self.p = datatypes.Point(1, 2, 3, 2)
        self.assertEquals(self.p.size,4)

    def testMPoint_NonCartesion_indexLetterAccess(self):
        self.p = datatypes.Point(1, 2, 3, 2)
        self.assertEquals(self.p.x, 1.0)
        self.assertEquals(self.p.y, 2.0)
        self.assertEquals(self.p.z, 3.0)
        self.assertEquals(self.p.w, 2.0)

        self.assertEquals(self.p[0], 1.0)
        self.assertEquals(self.p[1], 2.0)
        self.assertEquals(self.p[2], 3.0)
        self.assertEquals(self.p[3], 2.0)

    def testMPoint_NonCartesion_Get(self):
        got = ""
        self.p = datatypes.Point(1, 2, 3, 2)
        got = self.p.get()
        self.assert_(got == (1.0, 2.0, 3.0, 2.0))


##############################################################

#        self.q = api.MPoint()
#        self.assertEquals(self.q.distanceTo(self.p), 1.87082869339)

##############################################################


        self.p = datatypes.Point (api.MPoint())
        self.assertEquals(self.p, datatypes.Point([0.0, 0.0, 0.0]))

        self.p = datatypes.Point(1)
        self.assertEquals(self.p, datatypes.Point([1.0, 1.0, 1.0]))

        self.p = datatypes.Point(1, 2)
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 0.0]))

        self.p = datatypes.Point(1, 2, 3)
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

        self.p = datatypes.Point(api.MPoint(1, 2, 3))
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

        self.p = datatypes.Point(datatypes.VectorN(1,2))
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 0.0]))

        self.p = datatypes.Point(datatypes.VectorN(1, 2, 3))
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

    def testMPoint_instance(self):
        self.p = datatypes.Point()
        self.assertEquals(self.p, datatypes.Point([0.0, 0.0, 0.0]))
        self.assert_("<maya.OpenMaya.MPoint; proxy of <Swig Object of type 'MPoint *' at" in repr(self.p.data))

        self.p = datatypes.Point(1,2,3)
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

        self.v = datatypes.Vector(self.p)
        self.assertNotEqual(self.p, self.v)
        self.assertTrue(self.p.isEquivalent(self.v))
        self.assertTrue(self.v.isEquivalent(self.p))
        self.assertEquals(self.v, datatypes.Vector([1.0, 2.0, 3.0]))

        self.V = datatypes.VectorN(self.p)
        self.assertEquals(self.V, datatypes.VectorN([1.0, 2.0, 3.0, 1.0]))
        
        # Point from MVector
        self.p = datatypes.Point(api.MVector(1, 2, 3))
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

        # Point from datatypes.VectorN
        self.p = datatypes.Point(datatypes.VectorN(1, 2, 3, 4))
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0, 4.0]))

        # Point from datatypes.Vector from Point
        self.p = datatypes.Point(datatypes.Vector(self.p))
        self.assertEquals(self.p, datatypes.Point([0.25, 0.5, 0.75])) 

        # VectorN from Point from VectorN
        self.p = datatypes.Point(datatypes.VectorN(1, 2, 3, 4))
            # notice the last minute, sneak conversion to VectorN. 
        self.assertEquals(datatypes.VectorN(self.p), datatypes.VectorN([1.0, 2.0, 3.0, 4.0])) 

        # Copy Constructor
        self.p = datatypes.Point(self.p, w=1)
        self.assertEquals(self.p, datatypes.Point([1.0, 2.0, 3.0]))

        # datatypes.Vector from Point
        self.assertEquals(datatypes.Vector(self.p), datatypes.Vector([1.0, 2.0, 3.0])) # test Vector from Point

        # datatypes.VectorN from Point
        self.assertEquals(datatypes.VectorN(self.p), datatypes.VectorN([1.0, 2.0, 3.0, 1.0]))         

        # origin test
        self.p = datatypes.Point.origin
        self.assertEquals(self.p, datatypes.Point([0.0, 0.0, 0.0]))

        # xAxis test
        self.p = datatypes.Point.xAxis
        self.assertEquals(self.p, datatypes.Point([1.0, 0.0, 0.0]))

        # yAxis test
        self.p = datatypes.Point.yAxis
        self.assertEquals(self.p, datatypes.Point([0.0, 1.0, 0.0]))

        # zAxis test
        self.p = datatypes.Point.zAxis
        self.assertEquals(self.p, datatypes.Point([0.0, 0.0, 1.0]))


    def testMPoint_add(self):
        self.p = datatypes.Point(1, 2, 3, 1)
        self.assertEquals(self.p + 2, datatypes.Point([3.0, 4.0, 5.0, 1.0]))
        self.assertEquals(2 + self.p, datatypes.Point([3.0, 4.0, 5.0, 1.0]))

        #reset vals
        self.p = datatypes.Point(1, 2, 3)

        # Point and Vector :: returns Point
        self.assertEquals(self.p + datatypes.Vector([1, 2, 3]), datatypes.Point([2.0, 4.0, 6.0]))

        # Point and Point :: returns Point
        self.assertEquals(self.p + datatypes.Point([1, 2, 3]), datatypes.Point([2.0, 4.0, 6.0]))

        # Point and list(3,) :: returns Point
        self.assertEquals(self.p + [1, 2, 3], datatypes.Point([2.0, 4.0, 6.0]))

        # Point(3,) and Point(4,) :: returns Point
        self.assertEquals(self.p + datatypes.Point([1, 2, 3, 1]), datatypes.Point([2.0, 4.0, 6.0]))
        self.assertEquals(self.p + datatypes.Point([1, 2, 3, 2]), datatypes.Point([1.5, 3.0, 4.5]))

        # Vector and Point :: returns Point
        self.assertEquals((datatypes.Vector([1, 2, 3]) + self.p), datatypes.Point([2.0, 4.0, 6.0]))

        # Point and List(4,) :: returns Point
        self.assertEquals(self.p + [1, 2, 3, 2], datatypes.Point([2.0, 4.0, 6.0, 3.0]))

        # Point(3,) and Point :: returns Point
        self.assertEquals((datatypes.Point([1, 2, 3]) + self.p), datatypes.Point([2.0, 4.0, 6.0]))

        # List and Point :: returns Point
        self.assertEquals(([1, 2, 3] + self.p), datatypes.Point([2.0, 4.0, 6.0]))

        # TODO : returns Vector - expected Point([2.0, 4.0, 6.0])) :: if w=1, it returns type Vector,otherwise returns Point
        self.assertEquals(([1, 2, 3, 1] + self.p), datatypes.Vector([2.0, 4.0, 6.0])) 

        # not sure what ths chunk is testing for?
        #self.p = datatypes.Point(1, 2, 3)  # reset for all 
        #self.assertEquasls((datatypes.Point([1,2,3]) + self.p), datatypes.Point([2.0, 4.0, 6.0]))
        #self.assertEquals([1,2,3,2] + self.p, datatypes.Point([2.0, 4.0, 6.0, 3.0]))
        #self.assertEquals((datatypes.Point([1, 2, 3, 2]) + self.p), datatypes.Point([1.5, 3.0, 4.5]))

    def testMPoint_operations(self):
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.25, 0.5, 1.0)

        # divide point by scalar
        self.assertEquals((self.p / 2),datatypes.Point([0.5, 1.0, 1.5]))

        # multiply point by scalar
        self.assertEquals((self.p * 2),datatypes.Point([2.0, 4.0, 6.0]))

        # add point by scalar
        self.assertEquals(self.q + 2,datatypes.Point([2.25, 2.5, 3.0]))

        # divide point by scalar
        self.assertEquals(self.q / 2,datatypes.Point([0.125, 0.25, 0.5]))

        # add point to point
        #self.assertEquals(self.p + self.q, datatypes.Point([1.25, 2.5, 4.0]))

        # subtract point from point :: successfully returns Vector instance 
        self.assertEquals(self.p - self.q, datatypes.Vector([0.75, 1.5, 2.0]))
        self.assertEquals(self.q - self.p, datatypes.Vector([-0.75, -1.5, -2.0]))

        # subtract point from (point subtracted from point) :: nested/transitive subtraction
        self.assertEquals(self.p-(self.p - self.q), datatypes.Point([0.25, 0.5, 1.0]))

        # Multiply Vectors from Points
        self.assertEquals(datatypes.Vector(self.p) * datatypes.Vector(self.q), 4.25)

        # Point multiplication
        self.assertEquals(self.p*self.q, 4.25)

        # divide point by point
        self.assertEquals(self.p / self.q, datatypes.Vector([4.0, 4.0, 3.0])) # TODO : Original expected Point([4.0, 4.0, 3.0])

        # divide point by scalar
        self.assertEquals(self.p / 2, datatypes.Point([0.5, 1.0, 1.5]))

        # multiply point by scalar
        self.assertEquals(self.p * 2, datatypes.Point([2.0, 4.0, 6.0]))

    def testMPoint_cartesianize(self):
        locCop = datatypes.Point(self.r)       
        self.assertEquals(locCop.cartesian(),datatypes.Point([0.5, 1.0, 2.0]))
        self.assertEquals(locCop.cartesianize(),datatypes.Point([0.5, 1.0, 2.0]))
 
#    def testMPoint_deepcopy(self):
#        self.assertEquals(self.r, datatypes.Point([0.25, 0.5, 1.0, 0.5]))
#        self.assertEquals(self.r, self.qc) 

    def testMPoint_rationalize(self):
        locCop = datatypes.Point(self.r)
        self.assertEquals(locCop.rational(), datatypes.Point([0.5, 1.0, 2.0, 0.5]))
        self.assertEquals(locCop.rationalize(), datatypes.Point([0.5, 1.0, 2.0, 0.5])) # TODO :: currently returns Point([1.0, 2.0, 4.0, 0.5]

    def testMPoint_homegenize(self):
        locCop = datatypes.Point(self.r)
        self.assertEquals(locCop.homogen(), datatypes.Point([0.125, 0.25, 0.5, 0.5]))
        self.assertEquals(locCop.homogenize(), datatypes.Point([0.125, 0.25, 0.5, 0.5])) # TODO :: homogen leaves self.r intact, returns homogenized
 
    def testMPoint_VectorFromCartesianizedPoint(self):
        locCop = datatypes.Point(self.r)
        self.assertEquals(datatypes.Vector(locCop.cartesian()), datatypes.Vector([0.5, 1.0, 2.0])) #ignores 'w'

    def testMPoint_dividePointByScalar(self):
        self.assertEquals(self.r / 2, datatypes.Point([0.125, 0.25, 0.5, 0.5]))

    def testMPoint_multPointByScalar(self):
        self.assertEquals(self.r * 2, datatypes.Point([0.5, 1.0, 2.0, 0.5]))

    def testMPoint_addPointToScalar(self):
        self.assertEquals(self.r + 2, datatypes.Point([2.5, 3.0, 4.0]))  # cartesianize is done by datatypes.Vector's add

    def testMPoint_VectorInst_addition(self):
        self.p = datatypes.Point(1,2,3)
        #self.q = datatypes.Point(0.25, 0.5, 1.0)
        self.assertEquals((self.p + datatypes.Vector(1, 2, 3)), datatypes.Point([2.0, 4.0, 6.0]))
        self.assertEquals((self.r + datatypes.Vector(1, 2, 3)), datatypes.Point([1.5, 3.0, 5.0]))

    def testMPoint_cartesion_VectorInst_addition(self):
        self.assertEquals((self.r.cartesian() + datatypes.Vector(1,2,3)), datatypes.Point([1.5, 3.0, 5.0]))

    def testMPoint_subtractPointFromPoint(self):
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.25, 0.5, 1.0)
        self.assertEquals((self.p - self.r), datatypes.Vector([0.5, 1.0, 1.0]))
        self.assertEquals((self.r - self.p), datatypes.Vector([-0.5, -1.0, -1.0]))
        self.assertEquals(self.p - (self.p - self.r), datatypes.Point([0.5, 1.0, 2.0]))

    def testMPoint_cartesian_subtraction(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals((self.p-self.r.cartesian()), datatypes.Vector([0.5, 1.0, 1.0]))

    def testMPoint_VectorMultiply_from_Points(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(datatypes.Vector(self.p) * datatypes.Vector(self.r), 8.5)

    def testMPoint_mult(self):
        self.p = datatypes.Point(1,2,3)
        self.assertEquals(self.p * self.r, 8.5) 

 #   def testMPoint_dividePoints(self):  # TODO : need explicit homogenize as division not handled by api
 #       homoP = self.p.homogenize()
 #       homoQ = self.q.homogenize()
 #       self.assertEquals(homoP / homoQ, datatypes.Vector([2.0, 2.0, 1.5])) # used to be Point([4.0, 4.0, 3.0, 2.0])
        #  TODO : what do we want here ?

    def testMPoint_length(self):
        self.p = datatypes.Point(1,2,3)
        self.assertAlmostEquals(self.p.length(),3.74165738677)
        self.assertEquals(self.p[:1].length(), 1.0)
        self.assertEquals(datatypes.length(self.p[:1]), 1.0)
        self.assertAlmostEquals(self.p[:2].length(), 2.2360679775)
        self.assertAlmostEquals(self.p[:3].length(), self.p.length()) 
        self.assertAlmostEquals(datatypes.length(self.p),3.74165738677)


    def testMPoint_axis(self):
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.707, 0.0, -0.707)
        # returns Vector(- + -)
        self.assertEquals(datatypes.axis(datatypes.Point.origin, self.p, self.q), datatypes.Vector([-1.414, 2.828, -1.414]))
        # returns Vector(- + -)
        self.assertEquals(datatypes.Point.origin.axis(self.p, self.q), datatypes.Vector([-1.414, 2.828, -1.414]))
        # returns Vector(+ - +)
        self.assertEquals(datatypes.Point.origin.axis(self.q, self.p), datatypes.Vector([1.414, -2.828, 1.414]))

    def testMPoint_angle(self): # TODO :: WONKY ass vals returned - do the math again
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.707, 0.0, -0.707)       
        self.assertAlmostEquals(datatypes.angle(datatypes.Point.origin, self.p, self.q), 1.9583930134500773)
        self.assertAlmostEquals(datatypes.angle(datatypes.Point.origin, self.q, self.p), 1.9583930134500773)

        self.assertAlmostEquals(datatypes.angle(datatypes.Point.origin, self.p, self.r), 0.13078263384791716)
        self.assertAlmostEquals(datatypes.angle(datatypes.Point.origin, self.r, self.p), 0.13078263384791716)

        self.assertAlmostEquals(datatypes.Point.origin.angle(self.p, self.q), 1.9583930134500773)
        self.assertAlmostEquals(datatypes.Point.origin.angle(self.p, self.r), 0.13078263384791716)
        # self.assertEquals(datatypes.cotan(datatypes.Point.origin, self.p, self.q), 1.0)

    def testMPoint_distance(self):
        self.q = datatypes.Point(0.707, 0.0, -0.707)
        self.p = datatypes.Point(1,2,3)
        self.assertAlmostEquals(self.p.distanceTo(self.q), 4.2222858737892199)

    def testMPoint_differenceLengthForDistance(self):
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.707, 0.0, -0.707)
        self.assertAlmostEquals((self.q-self.p).length(), 4.2222858737892199)

    def testMPoint_planar(self):
        self.p = datatypes.Point(1,2,3)
        self.q = datatypes.Point(0.707, 0.0, -0.707)
        self.assertTrue( datatypes.planar( datatypes.Point.origin, self.p, self.q ))
        #self.assertTrue( datatypes.planar( datatypes.Point.origin, self.p, self.q, self.r )) # TODO :: currently evaluates to false whenever you pass in mor than three args
        #self.assertFalse(datatypes.planar( datatypes.Point.origin, self.p, self.q, self.r + datatypes.Vector(0.0, 0.1, 0.0)))

    def testMPoint_center(self):
        locP = datatypes.Point([1.0, 2.0, 3.0])
        locQ = datatypes.Point([1.0, 2.0, 3.0, 1.0])
        first = datatypes.center(datatypes.Point.origin, locP, locP)
        last = datatypes.Point([0.666666666667, 1.33333333333, 2.0])
        self.assert_(first, last) #TODO # Point([0.569, 0.0, -0.235666666667, 1.0])

    def testMPoint_bWeights(self):
        locP = datatypes.Point([1.0, 2.0, 3.0])
        locQ = datatypes.Point([1.0, 2.0, 3.0, 1.0])
        
        self.assertEquals(datatypes.bWeights(self.r, datatypes.Point.origin, locP, locQ), (0.0, 0.5, 0.5))
        self.assertEquals(datatypes.bWeights((.5,0,0), (0,0,0),(1,0,0),(1,1,0),(0,1,0)), (.5, .5, 0, 0))

    def testMPoint_round(self):
        self.p = datatypes.Point([0.33333, 0.66666, 1.333333, 0.33333])
        self.assertEquals(datatypes.round(self.p, 3), datatypes.Point([0.333, 0.667, 1.333, 0.333]) )


################################################################## 
## MColor tests 

    def testMColor_hasattr(self):
        self.assertTrue(hasattr(datatypes.Color, 'data'))

    def testMColor_instance_hasattr(self):        
        self.c = datatypes.Color()
        self.assertTrue(hasattr(self.c, 'data'))

    def testMColor_instance(self):
        self.c = datatypes.Color()
        self.assertEquals(self.c, datatypes.Color([0.0, 0.0, 0.0, 1.0]))

        self.c = datatypes.Color(api.MColor())
        self.assertEquals(self.c, datatypes.Color([0.0, 0.0, 0.0, 1.0])) # TODO - using api convention of single value would mean alpha
        # instead of datatypes.VectorN convention of filling all with value
        # which would yield # Color([0.5, 0.5, 0.5, 0.5]) instead
        # This would break coerce behavior for Color  

        self.c = datatypes.Color(0.5)
        self.assertEquals(self.c ,datatypes.Color([0.5, 0.5, 0.5, 0.5]))

        self.c = datatypes.Color(1, 1, 1)
        self.assertEquals(self.c , datatypes.Color([1.0, 1.0, 1.0, 1.0]))

        self.c = datatypes.Color(1, 0.5, 2, 0.5)
        self.assertEquals(self.c,datatypes.Color([1.0, 0.5, 2.0, 0.5]))

        self.c = datatypes.Color(128, quantize=255)
        self.assertEquals(self.c , datatypes.Color([0.501960813999, 0.501960813999, 0.501960813999, 0.501960813999]))

        self.c = datatypes.Color(255, 128, b=64, a=32, quantize=255)
        self.assertEquals(self.c , datatypes.Color([1.0, 0.501960813999, 0.250980407, 0.1254902035]))

        self.c = datatypes.Color(0, 65535, 65535, quantize=65535, mode='hsv')
        self.assertEquals(self.c , datatypes.Color([1.0, 0.0, 0.0, 1.0]))

        self.c = datatypes.Color(self.c, v=0.5, mode='hsv')
        self.assertEquals(self.c , datatypes.Color([0.5, 0.0, 0.0, 1.0]))

    def testMColor_CopyConstructor(self):
        self.c = datatypes.Color(datatypes.Color.blue, v=0.5)
        self.assertEquals(self.c , datatypes.Color([0.0, 0.0, 0.5, 1.0]))

    def testMColor_round(self):
        self.c = datatypes.round(datatypes.Color(255, 0, 255, g=128, quantize=255, mode='rgb'), 2)
        self.assertEquals(self.c , datatypes.Color([1.0, 0.5, 1.0, 1.0]))

        self.c = datatypes.round(datatypes.Color(255, b=128, quantize=255, mode='rgb'), 2)
        self.assertEquals(self.c , datatypes.Color([1.0, 1.0, 0.5, 1.0]))

    def testMColor_rgb(self):
        self.c = datatypes.Color(0, 65535, 65535, quantize=65535, mode='hsv')
        self.assertEquals(self.c.rgb, (1.0, 0.0, 0.0))

    def testMColor_hsv(self):
        self.c = datatypes.Color(0, 65535, 65535, quantize=65535, mode='hsv')
        self.assertEquals(self.c.hsv, (0.0, 1.0, 1.0))

        self.d = datatypes.Color(self.c, v=0.5, mode='hsv')
        self.assertEquals(self.d.hsv,(0.0, 1.0, 0.5))

        self.c = datatypes.Color(datatypes.Color.blue, v=0.5)
        self.assertEquals(self.c.hsv,(0.66666666666666663, 1.0, 0.5))

    def testMColor_rgbIndex_access(self):
        self.c = datatypes.Color(datatypes.Color.blue, v=0.5)
        self.c.r = 1.0
        self.c.g = 2.0
        self.c.b = 3.0
        self.c.a = 0.5

        self.assertEquals(self.c , datatypes.Color([1.0, 2.0, 3.0, 0.5]))
        self.assertEquals(self.c.hsv, (0.0, 0.0, 1.0))

    def testMColor_RGB_Constructor_Clamp(self):
        self.c = datatypes.Color(1, 0.5, 2, 0.5).clamp()
        self.assertEquals(self.c, datatypes.Color([1.0, 0.5, 1.0, 0.5]) )
        self.assertEquals(self.c.hsv, (0.83333333333333337, 0.5, 1.0))

    def testMColor_Copy_Constructor(self):
        self.c = datatypes.Color(1, 0.5, 2, 0.5).clamp()
        self.d = datatypes.Color(self.c,v=0.5)
        self.assertEquals(self.d, datatypes.Color([0.5, 0.25, 0.5, 0.5]))
        self.assertEquals(self.d.hsv, (0.83333333333333337, 0.5, 0.5))

    def testMColor_RGB_Constructor(self):
        self.c = datatypes.Color(0.0, 0.5, 1.0, 0.5)
        self.assertEquals(self.c, datatypes.Color(0.0, 0.5, 1.0, 0.5))

    def testMColor_Gamma(self):
        self.c = datatypes.Color(0.0, 0.5, 1.0, 0.5)
        self.d = self.c.gamma(2.0)
        self.assertEquals(self.d, datatypes.Color([0.0, 0.25, 1.0, 0.5]))

    def testMColor_Blend(self):
        self.c = datatypes.Color.red.blend(datatypes.Color.blue, 0.5)
        self.assertEquals(self.c.hsv, (0.83333333333333337, 1.0, 0.5))

    def testMColor_HsvBlend(self):
        self.c = datatypes.Color.red.hsvblend(datatypes.Color.blue, 0.5)
        self.assertEquals(self.c.hsv, (0.83333333333333337, 1.0, 1.0))

    def testMColor_Over(self):
        self.c = datatypes.Color(0.25, 0.5, 0.75, 0.5)
        self.d = datatypes.Color.black
        self.assertEquals(self.c.over(self.d), datatypes.Color([0.125, 0.25, 0.375, 1.0]) )
        self.assertEquals(self.d.over(self.c), datatypes.Color([0.0, 0.0, 0.0, 0.5]))

    def testMColor_RGB_Constructor_Premult(self):
        self.c = datatypes.Color(0.25, 0.5, 0.75, 0.5)
        self.assertEquals(self.c.premult(), datatypes.Color([0.125, 0.25, 0.375, 1.0]))

    def testMColor_VectorInheritance(self):
        self.c = datatypes.Color(0.25, 0.5, 1.0, 1.0)
        self.d = datatypes.Color(2.0, 1.0, 0.5, 0.25)
        self.assertEquals(self.c, datatypes.Color([0.25, 0.5, 1.0, 1.0]))
        self.assertEquals(self.d, datatypes.Color([2.0, 1.0, 0.5, 0.25]))

        # Negative assignment
        self.assertEquals(-(self.c), datatypes.Color([-0.25, -0.5, -1.0, 1.0]))

        # Multiply two colors
        self.e = self.c * self.d
        self.assertEquals(self.e, datatypes.Color([0.5, 0.5, 0.5, 0.25]))

        # Addition with constant
        self.assertEquals((self.e + 2), datatypes.Color([2.5, 2.5, 2.5, 0.25]))

        # Multiply by scalar float 
        # (defined in api for colors and also multiplies alpha)
        self.assertEquals((self.e * 2.0), datatypes.Color([1.0, 1.0, 1.0, 0.5]))

        # Divide by scalar float
        # TODO as is divide, that ignores alpha now for some reason
        self.assertEquals((self.e/2.0), datatypes.Color([0.25, 0.25, 0.25, 0.25]))

        # Addition with Vector Instance
        self.assertEquals(self.e + datatypes.Vector(1,2,3), datatypes.Color([1.5, 2.5, 3.5, 0.25]))
        # TODO Come correct? Here, behaves like API.

        # Addition with self
        self.assertEquals((self.c + self.c), datatypes.Color([0.5, 1.0, 2.0, 1.0]))
        # Addition with Color
        self.assertEquals((self.c + self.d), datatypes.Color([2.25, 1.5, 1.5, 1.0]))
        # Subtraction with Color
        self.assertEquals((self.d - self.c), datatypes.Color([1.75, 0.5, -0.5, 0.25]))
        #print "end tests Color" - TODO go through classes and make sure all methods are represented

#===============================================================================
# Euler Tests
#===============================================================================
    def testEuler_units(self):
        oldUnit = datatypes.Angle.getUIUnit()
        try:
            datatypes.Angle.setUIUnit('degrees')
            inDegrees = [10,20,30]
            eDeg = datatypes.EulerRotation(inDegrees)
            self.assertEquals(eDeg, datatypes.EulerRotation(inDegrees, unit='degrees'))
            eRad = datatypes.EulerRotation(eDeg)
            eRad.unit = 'radians'
            self.assertEquals(eDeg, eRad)
            inRadians = [datatypes.Angle(x, unit='degrees').asRadians() for x in inDegrees]
            eRad2 = datatypes.EulerRotation(inRadians, unit='radians')
            self.assertEqual(eRad2, eDeg)
            self.assertNotEqual(eRad2.x, eDeg.x)
            self.assertEqual(list(eDeg), [datatypes.Angle(x, unit='radians').asDegrees() for x in eRad2])
        finally:
            datatypes.Angle.setUIUnit(oldUnit)
            
    def testEuler_rotationOrder(self):
        rot = datatypes.EulerRotation(10,20,30, 'XYZ')
        self.assertEqual(rot.order, 'XYZ')
        rot.order = 'ZYX'
        self.assertEqual(rot.order, 'ZYX')
        other = datatypes.EulerRotation(10,20,30, 'ZYX')
        self.assertEqual(other.order, 'ZYX')
        self.assertEqual(rot, datatypes.EulerRotation(10,20,30, 'ZYX'))
        rot.assign( (6,7,8) )
        self.assertEqual(rot.order, 'ZYX')
        
    def testEuler_setItem(self):
        rot = datatypes.EulerRotation(10,20,30, 'XYZ')
        self.assertAlmostEqual(rot.y, 20)
        rot.y = 50
        self.assertAlmostEqual(rot.y, 50)
        self.assertAlmostEqual(rot.z, 30)
        rot['z'] = 60
        self.assertAlmostEqual(rot.z, 60)
        self.assertAlmostEqual(rot.x, 10)
        rot[0] = 70
        self.assertAlmostEqual(rot.x, 70)


################################################################## 
## MMatrix tests 

    def testMatrix_Instance(self) :
        self.m = datatypes.Matrix()
        self.assertEquals(self.m.shape, datatypes.Matrix.shape)
        self.assertEquals(self.m.ndim,  datatypes.Matrix.ndim)
        self.assertEquals(self.m.size,  datatypes.Matrix.size)

    def testIdentityMatrix_IsInstance(self) :
        self.m = datatypes.Matrix.identity
        self.assertTrue(isinstance(self.m, datatypes.MatrixN))
        self.assertTrue(isinstance(self.m, datatypes.Array))
        self.assertTrue(isinstance(self.m, api.MMatrix))

    def testMatrix_False_Instances(self) : 
        def Matrix_fromRange_Test(): 
            self.m = datatypes.Matrix(range(20)) # TODO should fail
            self.m.formated()
        #   cannot initialize a Matrix of shape (4, 4) from list of 20,  
        #   would cause truncation errors, use an explicit resize or trim"     
        self.failUnlessRaises(TypeError, Matrix_fromRange_Test)
        
#        self.m = datatypes.Matrix()
#        def MatrixSetTest1(): 
#            self.m.shape = (4,4) # TODO should fail
#        def MatrixSetTest2(): 
#            self.m.shape = 2
#
#        self.failUnlessRaises(ValueError, MatrixSetTest1)
#        self.failUnlessRaises(ValueError, MatrixSetTest2)

    def testMatrix_formated(self) :
        self.m = datatypes.Matrix()
        self.assertEquals(self.m.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

    def testMatrix_IndexAccess(self) :
        self.m = datatypes.Matrix()


        # Single Index
        self.assertEquals(self.m[0][0], 1.0)
        #self.assertEquals(self.m[0:0][0:2],[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]) ## TODO :: WTF?
        # Multi Index
        self.assertEquals(self.m[1:2][0:1], datatypes.MatrixN([[0.0, 1.0, 0.0, 0.0]]))

        # paren indice access
        self.assertEquals(self.m(0,0), 1.0)

    def testMMatrix_API_Calls(self) :        
        # should be accepted directly by API methods
        self.n = api.MMatrix()

        # SetToProduct # TODO returns MMatrix() ?
        self.m = self.n.setToProduct(self.m,self.m)
        self.assert_("<maya.OpenMaya.MMatrix; proxy of <Swig Object of type 'MMatrix *' at" in repr(self.m)) #TODO - 

        # Make MAtrix instance from range()
        self.m = datatypes.Matrix(range(16))
        self.assertEquals(self.m.formated(), '[[0.0, 1.0, 2.0, 3.0],\n [4.0, 5.0, 6.0, 7.0],\n [8.0, 9.0, 10.0, 11.0],\n [12.0, 13.0, 14.0, 15.0]]')

        # Make Matrix instance from Array from range()     
        self.M = datatypes.Array(range(16), shape=(8, 2))
        self.m = datatypes.Matrix(self.M)
        self.assertEquals(self.m.formated(), '[[0.0, 1.0, 2.0, 3.0],\n [4.0, 5.0, 6.0, 7.0],\n [8.0, 9.0, 10.0, 11.0],\n [12.0, 13.0, 14.0, 15.0]]')

        # Make Matrix instance from MatrixN from range() 
        self.M = datatypes.MatrixN(range(9), shape=(3, 3))
        self.m = datatypes.Matrix(self.M)
        self.assertEquals(self.m.formated(),'[[0.0, 1.0, 2.0, 0.0],\n [3.0, 4.0, 5.0, 0.0],\n [6.0, 7.0, 8.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

        # inherits from Array and MatrixN
        self.assertTrue(isinstance(self.m, datatypes.MatrixN))
        self.assertTrue(isinstance(self.m, datatypes.Array))

        # as well as _api_Matrix
        self.assertTrue(isinstance(self.m, api.MMatrix))

        # create transformationmatrix and translate, yo :: TODO
        self.n = api.MMatrix()
        self.m = self.n.setToProduct(self.m, self.m)
        self.t = api.MTransformationMatrix()
        self.t.setTranslation(datatypes.Vector(1,2,3), api.MSpace.kWorld)
        self.m = datatypes.Matrix(self.t)
        self.assertEquals(self.m.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [1.0, 2.0, 3.0, 1.0]]')

        self.m = datatypes.Matrix(self.m, a30=10)
        self.assertEquals(self.m.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [10.0, 2.0, 3.0, 1.0]]')


    def testMatrix_Trimmed(self):
        self.m = datatypes.Matrix.identity
        self.M = self.m.trimmed(shape=(3, 3))
        self.assertEquals(self.M.formated(),'[[1.0, 0.0, 0.0],\n [0.0, 1.0, 0.0],\n [0.0, 0.0, 1.0]]') # TODO goto the docs, tool

    def testMatrix_issingular(self):
        self.M = datatypes.Matrix.identity
        self.M = self.m.trimmed(shape=(3,3))
        self.assertEquals(self.M, datatypes.MatrixN([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]))

        def Matrix_badTrim_Test(): 
            self.m.trim(shape=(3,3)) # TODO should fail
        self.failUnlessRaises(TypeError, Matrix_badTrim_Test) # new shape (3, 3) should not be compatible with class Matrix

    def testMatrix_columnAccess(self):
        self.m = datatypes.Matrix.identity
        self.assertEquals(self.m.ncol, 4)

        def Matrix_badRow():
            self.m.nrow = 3
        self.failUnlessRaises(TypeError, Matrix_badRow)

    def testMatrix_rowAccess(self):
        self.assertEquals(self.m.nrow, 4)

# for i in range(0,4):print m.col[i]

    def testMatrix_list(self):
        self.assertEquals(list(self.m.row), [datatypes.Array([1.0, 0.0, 0.0, 0.0]), datatypes.Array([0.0, 1.0, 0.0, 0.0]), datatypes.Array([0.0, 0.0, 1.0, 0.0]), datatypes.Array([0.0, 0.0, 0.0, 1.0])] )

        self.assertEquals(list(self.m.col), [datatypes.Array([1.0, 0.0, 0.0, 0.0]), datatypes.Array([0.0, 1.0, 0.0, 0.0]), datatypes.Array([0.0, 0.0, 1.0, 0.0]), datatypes.Array([0.0, 0.0, 0.0, 1.0])] )

    def testMMatrix_fromTrimmedMatrixN(self):
        self.m  = datatypes.Matrix(datatypes.MatrixN(range(9), shape=(3,3)).trimmed(shape=(4,4), value=10))
        self.assertEquals(self.m.formated(), '[[0.0, 1.0, 2.0, 10.0],\n [3.0, 4.0, 5.0, 10.0],\n [6.0, 7.0, 8.0, 10.0],\n [10.0, 10.0, 10.0, 10.0]]')

    def testMMatrix_getAccess(self):
        self.m = datatypes.Matrix(datatypes.MatrixN(range(9), shape=(3,3)).trimmed(shape=(4,4), value=10))
        self.assertEquals(self.m.get(), ((0.0, 1.0, 2.0, 10.0), (3.0, 4.0, 5.0, 10.0), (6.0, 7.0, 8.0, 10.0), (10.0, 10.0, 10.0, 10.0)))

    def testMMatrix_indexAccess(self):
        self.m = datatypes.Matrix(datatypes.MatrixN(range(9), shape=(3,3)).trimmed(shape=(4,4), value=10))
        self.assertEquals(self.m[0], datatypes.Array([0.0, 1.0, 2.0, 10.0]))

        self.m[0] = 10
        self.assertEquals(self.m.formated(), '[[10.0, 10.0, 10.0, 10.0],\n [3.0, 4.0, 5.0, 10.0],\n [6.0, 7.0, 8.0, 10.0],\n [10.0, 10.0, 10.0, 10.0]]')

        # list
        self.assertTrue(10 in self.m)
        self.assertEquals(list(self.m), [datatypes.Array([10.0, 10.0, 10.0, 10.0]), datatypes.Array([3.0, 4.0, 5.0, 10.0]), datatypes.Array([6.0, 7.0, 8.0, 10.0]), datatypes.Array([10.0, 10.0, 10.0, 10.0])])

        # list flat
        self.assertEquals(list(self.m.flat), [10.0, 10.0, 10.0, 10.0, 3.0, 4.0, 5.0, 10.0, 6.0, 7.0, 8.0, 10.0, 10.0, 10.0, 10.0, 10.0])

    def testMMatrix_AxisAccess(self):
        self.u = datatypes.Vector.xAxis
        self.v = datatypes.Vector.yAxis
        self.assertEquals(self.v, datatypes.Vector.yAxis)
        self.assertEquals(self.u, datatypes.Vector.xAxis)

    def testMMatrix_rounded(self):
        ## TODO round(m, 2) returns 
            #Traceback (most recent call last):
            #  File "<stdin>", line 1, in <module>
            #  File "/Volumes/luma/_globalSoft/python/thirdParty/pymel/util/mathutils.py", line 43, in round
            #    return _round(value, ndigits)
            #TypeError: a float is required

        # trans matrix : t: 1, 2, 3, r: 45, 90, 30, s: 0.5, 1.0, 2.0
        #self.m = datatypes.Matrix([0.0, 4.1633363423443383e-17, -0.5, 0.0, 0.25881904510252079, 0.96592582628906831, 1.3877787807814459e-16, 0.0, 1.9318516525781366, -0.51763809020504159, 0.0, 0.0, 1.0, 2.0, 3.0, 1.0])
        #(round(self.m, 2).formated(),'[[0.0, 0.0, -0.5, 0.0],\n [0.26, 0.97, 0.0, 0.0],\n [1.93, -0.52, 0.0, 0.0],\n [1.0, 2.0, 3.0, 1.0]]' )
        pass

    def testMMatrix_operations(self):
        self.m = datatypes.Matrix([[0.0, 4.16333634234e-17, -0.5, 0.0], [0.258819045103, 0.965925826289, 1.38777878078e-16, 0.0], [1.93185165258, -0.517638090205, 0.0, 0.0], [1.0, 2.0, 3.0, 1.0]])
        self.x = datatypes.Vector.xAxis
        self.y = datatypes.Vector.yAxis
        self.z = datatypes.Vector.zAxis
        self.u = datatypes.Vector(1, 2, 3)

        # start check
        self.assertEquals(self.u, datatypes.Vector([1, 2, 3]))

        # multiply Matrix by Vector
        first = self.u * self.m
        last = datatypes.Vector([6.31319304795, 0.378937381963, -0.5])
        self.assert_(first.isEquivalent(last))
        
        first = self.m * self.u
        last = datatypes.Vector([-1.5, 2.19067069768, 0.896575472168])
        self.assert_(first.isEquivalent(last))       

        #  multiply Matrix by Point
        self.p = datatypes.Point(1,10,100,1)
        
        first = self.p * self.m
        last = datatypes.Point([196.773355709, -40.1045507576, 2.5, 1.0])
        self.assert_(first.isEquivalent(last))
         
        first = self.m * self.p
        last = datatypes.Point([-50.0, 9.91807730799, -3.24452924947, 321.0])
        self.assert_(first.isEquivalent(last))        

        # multiplication by datatypes.VectorN:3
        first = datatypes.VectorN([1, 2, 3])* self.m
        last = datatypes.VectorN([6.31319304795, 0.378937381963, -0.5])
        #self.assert_(self.v.isEquivalent(last)) # AssertionError
        #self.assertEquals(first, last) # AssertionError: VectorN([6.31319304795, 0.378937381963, -0.5]) != VectorN([6.31319304795, 0.378937381963, -0.5])
        
        fd = first.data
        ld = last.data
        for i in range(0,2): # used assertAlmostEquals since we were getting some rounding errors for the list items after the eighth decimal
            self.assertAlmostEquals(fd[i], ld[i])
       
        # multiplication by datatypes.VectorN:5 Should fail, because 
        # datatypes.Vector:5 and matrix:shape(4,4) are not able to conform for a 'VectorN * MatrixN' multiplication 
        def VectorN_test():
            self.v = datatypes.VectorN([1, 2, 3, 4, 5])* self.m 
        self.failUnlessRaises(ValueError, VectorN_test) 

        # element wise multiplication
        self.m = datatypes.Matrix(range(1, 17))
        self.assertEquals(self.m.formated(), '[[1.0, 2.0, 3.0, 4.0],\n [5.0, 6.0, 7.0, 8.0],\n [9.0, 10.0, 11.0, 12.0],\n [13.0, 14.0, 15.0, 16.0]]')
        self.assertEquals(([1, 10, 100] * self.m), datatypes.Matrix([[1.0, 20.0, 300.0, 0.0], [5.0, 60.0, 700.0, 0.0], [9.0, 100.0, 1100.0, 0.0], [13.0, 140.0, 1500.0, 0.0]]) )

        self.M = datatypes.MatrixN(range(1, 21), shape=(4, 5))
        self.assertEquals(self.M.formated(), '[[1, 2, 3, 4, 5],\n [6, 7, 8, 9, 10],\n [11, 12, 13, 14, 15],\n [16, 17, 18, 19, 20]]')
        
        self.n = self.m * self.M
        self.assertEquals(self.n.formated(),'[[110.0, 120.0, 130.0, 140.0, 150.0],\n [246.0, 272.0, 298.0, 324.0, 350.0],\n [382.0, 424.0, 466.0, 508.0, 550.0],\n [518.0, 576.0, 634.0, 692.0, 750.0]]')

        # check class name
        self.assertEquals(util.clsname(self.n), 'MatrixN')     

        # multiply by integer - should return a Matrix
        self.n = (self.m * 2)
        self.assertEquals(self.n.formated(), '[[2.0, 4.0, 6.0, 8.0],\n [10.0, 12.0, 14.0, 16.0],\n [18.0, 20.0, 22.0, 24.0],\n [26.0, 28.0, 30.0, 32.0]]')
        # and then double-check class
        self.assertEquals(util.clsname(self.n), 'Matrix')

        # multiply integer by matrix - should return a Matrix
        self.n = (2 * self.m)
        self.assertEquals(self.n.formated(), '[[2.0, 4.0, 6.0, 8.0],\n [10.0, 12.0, 14.0, 16.0],\n [18.0, 20.0, 22.0, 24.0],\n [26.0, 28.0, 30.0, 32.0]]')
        self.assertEquals(util.clsname(self.n), 'Matrix')

        # add matrix to integer - should return a Matrix
        self.n = self.m + 2
        self.assertEquals(self.n.formated(),'[[3.0, 4.0, 5.0, 6.0],\n [7.0, 8.0, 9.0, 10.0],\n [11.0, 12.0, 13.0, 14.0],\n [15.0, 16.0, 17.0, 18.0]]')
        self.assertEquals(util.clsname(self.n), 'Matrix')

         # add integer to matrix   
        self.n = 2 + self.m 
        self.assertEquals(self.n.formated(),'[[3.0, 4.0, 5.0, 6.0],\n [7.0, 8.0, 9.0, 10.0],\n [11.0, 12.0, 13.0, 14.0],\n [15.0, 16.0, 17.0, 18.0]]')
        self.assertEquals(util.clsname(self.n), 'Matrix')

        def setToProduct_test():
            self.m.setToProduct(self.m, self.M)
        # cannot initialize a Matrix of shape (4, 4) from shape (4, 5) - truncation errors
        self.failUnlessRaises(TypeError, setToProduct_test)

        # isEquivalent() should evaluate as false
        self.assertFalse(self.m.isEquivalent(self.m * self.M))

        # trans matrix : t: 1, 2, 3, r: 45, 90, 30, s: 0.5, 1.0, 2.0
        self.m = datatypes.Matrix([0.0, 4.1633363423443383e-17, -0.5, 0.0, 0.25881904510252079, 0.96592582628906831, 1.3877787807814459e-16, 0.0, 1.9318516525781366, -0.51763809020504159, 0.0, 0.0, 1.0, 2.0, 3.0, 1.0])

        # round() matrix values # TODO round from chad
        #self.assertEquals(round(self.m, 2).formated(), '[[0.0, 0.0, -0.5, 0.0],\n [0.26, 0.97, 0.0, 0.0],\n [1.93, -0.52, 0.0, 0.0],\n [1.0, 2.0, 3.0, 1.0]]')

        # round() the transposed() the matrix # TODO round from chad
        #self.assertEquals(round(self.m.transpose(),2).formated(), '[[0.0, 0.26, 1.93, 1.0],\n [0.0, 0.97, -0.52, 2.0],\n [-0.5, 0.0, 0.0, 3.0],\n [0.0, 0.0, 0.0, 1.0]]')

        # issingular() - make sure (not) no inverse - yay, assertFalse!
        self.assertFalse(self.m.isSingular())

        # so lets check that inverse matrix# TODO round from chad
        #self.assertEquals(round(self.m.inverse(),2).formated(), '[[0.0, 0.26, 0.48, 0.0],\n [0.0, 0.97, -0.13, 0.0],\n [-2.0, 0.0, 0.0, 0.0],\n [6.0, -2.19, -0.22, 1.0]]')

        # adjoint() - should be the same as the inverse, as they are *almost the same thing # TODO round from chad
        #self.assertEquals(round(self.m.adjoint(),2).formated(), '[[0.0, 0.26, 0.48, 0.0],\n [0.0, 0.97, -0.13, 0.0],\n [-2.0, 0.0, -0.0, 0.0],\n [6.0, -2.19, -0.22, 1.0]]')

        # adjugate() - should be identical to the adoint matrix# TODO round from chad
        #self.assertEquals(round(self.m.adjugate(),2).formated(), '[[0.0, 0.26, 0.48, 0.0],\n [0.0, 0.97, -0.13, 0.0],\n [-2.0, 0.0, -0.0, 0.0],\n [6.0, -2.19, -0.22, 1.0]]')

        # homogenize()# TODO round from chad
        #self.assertEquals(round(self.m.homogenize(),2).formated(), '[[0.0, 0.0, -1.0, 0.0],\n [0.26, 0.97, 0.0, 0.0],\n [0.97, -0.26, -0.0, 0.0],\n [1.0, 2.0, 3.0, 1.0]]')

        # determinant()
        self.assertEquals(self.m.det(), 1.0)

        # determinant for this matrix:4x4
        self.assertEquals(self.m.det4x4(), 1.0)

        # determinant of the upper left 3x3 submatrix of this matrix instance
        self.assertEquals(self.m.det3x3(), 1.0)

        # TODO round from chad
        #self.assertEquals(round(m.weighted(0.5),2).formated(), '[[0.53, 0.0, -0.53, 0.0],\n [0.09, 0.99, 0.09, 0.0],\n [1.05, -0.2, 1.05, 0.0],\n [0.5, 1.0, 1.5, 1.0]]')

        # blend() # TODO round from chad
        #self.assertEquals(round(m.blend(Matrix.identity, 0.5),2).formated(), '[[0.53, 0.0, -0.53, 0.0],\n [0.09, 0.99, 0.09, 0.0],\n [1.05, -0.2, 1.05, 0.0],\n [0.5, 1.0, 1.5, 1.0]]')


################################################################## 
## MTransformationMatrix tests


    def testMTransformationMatrix_QuatInstance(self) :
        q = datatypes.Quaternion()
        self.assertEquals(q, datatypes.Quaternion([0.0, 0.0, 0.0, 1.0]))

        q = datatypes.Quaternion(1, 2, 3, 0.5)
        last = datatypes.Quaternion([1.0, 2.0, 3.0, 0.5])
        self.assert_(q.isEquivalent(last))

        q = datatypes.Quaternion(0.785, 0.785, 0.785, "XYZ", unit='radians')
        last = datatypes.Quaternion([0.191357439088, 0.461717715523, 0.191357439088, 0.844737481223])
        self.assert_(q.isEquivalent(last))

    def testMTransformationMatrix_rotate(self):
        self.m = datatypes.Matrix()
        self.q = datatypes.Quaternion(1, 2, 3, 0.5)
        self.m.rotate = self.q
        last = datatypes.Matrix([[-0.824561403509, 0.491228070175, 0.280701754386, 0.0], [0.0701754385965, -0.40350877193, 0.912280701754, 0.0], [0.561403508772, 0.771929824561, 0.298245614035, 0.0], [0.0, 0.0, 0.0, 1.0]])
        self.assert_(self.m.isEquivalent(last))

        self.t = datatypes.Matrix()
        self.q = datatypes.Quaternion(1, 2, 3, 0.5)
        self.t.rotate = self.q
        last = datatypes.Matrix([[-0.824561403509, 0.491228070175, 0.280701754386, 0.0], [0.0701754385965, -0.40350877193, 0.912280701754, 0.0], [0.561403508772, 0.771929824561, 0.298245614035, 0.0], [0.0, 0.0, 0.0, 1.0]])
        self.assert_(self.t.isEquivalent(last))
        
    def testMTransformationMatrix_rotation(self):
        tm = datatypes.TransformationMatrix()
        self.assertEqual(tm.getRotation(), datatypes.EulerRotation(0,0,0) )
        tm.setRotation(90,0,0, 'XYZ')
        last = datatypes.Matrix([[1,0,0,0], [0,0,1,0], [0,-1,0,0], [0,0,0,1]])
        self.assertTrue(tm.isEquivalent(last))
        self.assertEqual(tm.getRotation(), datatypes.EulerRotation(90,0,0, 'XYZ'))
        tm.setRotation(10,20,30, 'XYZ')
        last = dt.Matrix([[0.81379768134937369, 0.46984631039295421, -0.34202014332566871, 0.0,],
                   [-0.44096961052988248, 0.8825641192593856, 0.16317591116653482, 0.0,],
                   [0.37852230636979256, 0.018028311236297268, 0.92541657839832336, 0.0,],
                   [0.0, 0.0, 0.0, 1.0]])
        self.assertTrue(tm.isEquivalent(last))
        tm.setRotation(10,20,30, 'YZX')
        last = dt.Matrix([0.81379768134937369,
                         0.52209946381304628,
                         -0.25523613325019773,
                         0.0,
                         -0.49999999999999994,
                         0.85286853195244317,
                         0.15038373318043533,
                         0.0,
                         0.29619813272602386,
                         0.0052361332501977423,
                         0.95511216570526569,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         1.0])
        self.assertTrue(tm.isEquivalent(last))
        tm.setRotation(10,20,30, 'ZYX')
        last = dt.Matrix([0.81379768134937369,
                         0.54383814248232565,
                         -0.2048741287028622,
                         0.0,
                         -0.46984631039295427,
                         0.82317294464550095,
                         0.31879577759716787,
                         0.0,
                         0.34202014332566871,
                         -0.16317591116653482,
                         0.92541657839832336,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         1.0])
        self.assertTrue(tm.isEquivalent(last))
    
    def testMTransformationMatrix_rotateTo(self):
        self.t = datatypes.TransformationMatrix()
        self.t.rotateTo([1, 2, 3, 0.5])
        last = datatypes.Matrix([[-0.824561403509, 0.491228070175, 0.280701754386, 0.0], [0.0701754385965, -0.40350877193, 0.912280701754, 0.0], [0.561403508772, 0.771929824561, 0.298245614035, 0.0], [0.0, 0.0, 0.0, 1.0]])
        self.assert_(self.t.isEquivalent(last))
    
    def testMTransformationMatrix_formatted(self):    
        self.m = datatypes.TransformationMatrix()
        self.assertEquals(self.m.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

    def testMTransformationMatrix_indiceAccess(self):
        self.m = datatypes.TransformationMatrix()
        self.assertEquals(self.m[0, 0], 1.0)
        self.assertEquals(self.m[0:2, 0:3], datatypes.MatrixN([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]))

    def testMTransformationMatrix_instanceEquality(self):
        self.m = datatypes.TransformationMatrix()
        self.assertEquals(datatypes.TransformationMatrix.shape, self.m.shape)
        self.assertEquals(datatypes.TransformationMatrix.ndim, self.m.ndim)
        self.assertEquals(datatypes.TransformationMatrix.size, self.m.size)

    def testMTransformationMatrix_inheritance(self):
        self.m = datatypes.TransformationMatrix.identity
        self.assertTrue(isinstance(self.m, datatypes.MatrixN))
        self.assertTrue(isinstance(self.m, datatypes.Array)) # inherits from MatrixN --> Array

    def testMTransformationMatrix_API_instances(self):
        # as well as api.TransformationMatrix and api.Matrix
        self.m = datatypes.TransformationMatrix.identity 
        self.assertTrue(isinstance(self.m, api.MTransformationMatrix))
        self.assertTrue(isinstance(self.m, api.MMatrix))

    def testMTransformationMatrix_isEquivalent(self):
        self.n = datatypes.TransformationMatrix.identity
        self.m = datatypes.TransformationMatrix.identity

        self.assertTrue(self.m.isEquivalent(self.n))

        # Should Fail TODO :: does not currently fail
        def setShape_test1():
            self.m.shape = (4,4)
        def setShape_test2():
            self.m.shape = 2
        # these currently don't error out the way they should. TODO
        self.failUnlessRaises(TypeError, setShape_test1())
        self.failUnlessRaises(TypeError, setShape_test2())

        # setToProduct # TODO :: File "<stdin>", line 1, in <module> TypeError: in method 'MMatrix_setToProduct', argument 2 of type 'MMatrix const &'
        self.n = api.MMatrix()
        #self.n = self.n.setToProduct(self.m, self.m)
        #self.assert_("<maya.OpenMaya.MMatrix; proxy of <Swig Object of type 'MMatrix *" in repr(self.n))

        # assign
        self.n = api.MTransformationMatrix()
        self.n = self.n.assign(self.m)
        self.assert_("<maya.OpenMaya.MTransformationMatrix; proxy of <Swig Object of type 'MTransformationMatrix *" in repr(self.n))

        # rotation
        self.m = datatypes.TransformationMatrix.identity
        self.m.rotation = datatypes.Quaternion()
        self.assertEquals(self.m.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

        # translations
        self.n = datatypes.TransformationMatrix.identity 
        self.n.translation = datatypes.Vector(1, 2, 3)
        self.assertEquals(self.n.formated(), '[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

        # identity multiplied by identity
        self.o = self.m * self.n
        self.assertEquals(self.o.formated(),'[[1.0, 0.0, 0.0, 0.0],\n [0.0, 1.0, 0.0, 0.0],\n [0.0, 0.0, 1.0, 0.0],\n [0.0, 0.0, 0.0, 1.0]]')

    def test_constants(self):
        # TODO : come up with a programatic way of finding constants
        s = """
        Vector.xAxis
        Vector.one
        Vector.zero
        Vector.yNegAxis
        Vector.zNegAxis
        Vector.xNegAxis
        Vector.zAxis
        Vector.yAxis
        FloatVector.xAxis
        FloatVector.one
        FloatVector.zero
        FloatVector.yNegAxis
        FloatVector.zNegAxis
        FloatVector.xNegAxis
        FloatVector.zAxis
        FloatVector.yAxis
        Point.origin
        Point.xAxis
        Point.yNegAxis
        Point.zero
        Point.zNegAxis
        Point.yAxis
        Point.zAxis
        Point.one
        Point.xNegAxis
        FloatPoint.origin
        FloatPoint.yNegAxis
        FloatPoint.yAxis
        FloatPoint.zNegAxis
        FloatPoint.xNegAxis
        FloatPoint.zAxis
        FloatPoint.xAxis
        FloatPoint.one
        FloatPoint.zero
        Color.xAxis
        Color.yNegAxis
        Color.zero
        Color.zNegAxis
        Color.yAxis
        Color.zAxis
        Color.one
        Color.xNegAxis
        FloatMatrix.identity
        TransformationMatrix.identity
        EulerRotation.identity
        Quaternion.identity
        """
        
        for x in s.split('\n'):
            x = x.strip()
            if x:
                c, at = x.split('.')
                val  = getattr( getattr( datatypes, c ), at )

if __name__ == '__main__':
    unittest.main()
