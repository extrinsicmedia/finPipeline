from pymel.util.testing import TestCaseExtended, setupUnittestModule, TestCase
from pymel.util import utilitytypes

aDict = {'A':1, 'a':2}
bDict = {'B':3, 'b':4}

class BasicSingleton(object):
    __metaclass__ = utilitytypes.Singleton

class DictSingleton(dict) :
    __metaclass__ = utilitytypes.Singleton
    


class TestBasicSingleton(TestCaseExtended):
    # Override this attribute in derived classes!
    # Also, should use self.testClass (as
    # opposed to just 'testClass') in derived classes,
    # in case other classes derive from them...
    testClass = BasicSingleton
    
    def setUp(self):
        self.testClass = self.__class__.testClass

    def testSameInstance(self):
        self.assertTrue(self.testClass() is self.testClass())

class __AbstractTestDict(TestBasicSingleton):
        
    def testCanInitialize(self):
        self.testClass(aDict)
        self.assertEqual(aDict, dict(self.testClass()))

    def testReferencesEqual(self):
        oldRef = self.testClass(aDict)
        newRef = self.testClass()
        self.assertTrue( oldRef == newRef)

class TestDictSingleton(__AbstractTestDict):
    testClass = DictSingleton
    def setUp(self):
        super(TestDictSingleton, self).setUp()
        self.testClass().clear()

    def testInitializeResets(self):
        self.testClass(aDict)
        self.assertTrue(len(self.testClass())>0)
        self.testClass({})
        self.assertTrue(len(self.testClass())==0)

    def testSameInstanceAfterReinitializing(self):
        oldInst = self.testClass({'A':1})
        self.assertTrue(self.testClass({}) is oldInst)        

    def testCanUpdate(self):
        self.testClass()['z'] = 3
        self.assertEqual(self.testClass()['z'], 3)
        self.testClass()['z'] = 12
        self.assertEqual(self.testClass()['z'], 12)
        
    def testNoClearOnUpdate(self):
        self.testClass()['a'] = "foobar"
        self.assertEqual(self.testClass()['a'], "foobar")
        self.testClass()['fuzzy'] = "bear"
        self.assertEqual(self.testClass()['a'], "foobar")
                
class TestFrozenDict(__AbstractTestDict):
    # In the case of static classes, need to create a new class
    # on each setup...
    
    def setUp(self):
        self._makeNewFrozenDictClass()
        
    def _makeNewFrozenDictClass(self, initialValue=None):
        class FrozenDict(dict):
            __metaclass__ = utilitytypes.metaStatic
        self.testClass = FrozenDict
            
    def _doInit(self, initialValue=None):
        if initialValue:
            return self.testClass(initialValue)
        else:
            return self.testClass()
        
    def _doAssignation(self, key, value):
        self.testClass()[key] = value

    def testNoReinitialization(self):
        self._doInit(aDict)
        self.assertRaises(TypeError, self._doInit, aDict)

    def testNoErrorIfNoArgs(self):
        self._doInit(aDict)
        self.assertNoError(self._doInit)
        self.assertNoError(self._doInit)
    
    def testNoAssignation(self):
        self.assertRaises(TypeError, self._doAssignation, 'A', 3)
        
    def testHidden(self):
        shouldBeHidden = ('clear', 'update', 'pop', 'popitem', '__setitem__', '__delitem__', 'append', 'extend' )
        for hidden in shouldBeHidden:
            self.assertFalse(hasattr(self.testClass(), hidden))

class TestEquivalencePairs(TestCaseExtended):
    def testInitPairs(self):
        ep = utilitytypes.EquivalencePairs( ((1,'foo'), (2,'bar')) )
        self.assertEqual(ep[1], 'foo')
        self.assertEqual(ep[2], 'bar')
        self.assertEqual(ep['foo'], 1)
        self.assertEqual(ep['bar'], 2)
        
    def testInitDict(self):
        ep = utilitytypes.EquivalencePairs( {1:'foo', 2:'bar'} )
        self.assertEqual(ep[1], 'foo')
        self.assertEqual(ep[2], 'bar')
        self.assertEqual(ep['foo'], 1)
        self.assertEqual(ep['bar'], 2)

    def testInitEquivPairs(self):
        otherEp = utilitytypes.EquivalencePairs( {1:'foo', 2:'bar'} )
        ep = utilitytypes.EquivalencePairs(otherEp)
        self.assertEqual(ep[1], 'foo')
        self.assertEqual(ep[2], 'bar')
        self.assertEqual(ep['foo'], 1)
        self.assertEqual(ep['bar'], 2)
        
    def testOverwritePairs(self):
        ep = utilitytypes.EquivalencePairs({1:'a', 2:'b'})
        self.assertEqual(ep[1], 'a')
        self.assertEqual(ep[2], 'b')
        self.assertEqual(ep['a'], 1)
        self.assertEqual(ep['b'], 2)
        ep[1] = 2
        self.assertRaises(KeyError, self._getIndex, ep, 'a')
        self.assertRaises(KeyError, self._getIndex, ep, 'b')
        self.assertEqual(ep[1], 2)
        self.assertEqual(ep[2], 1)
        
    def _getIndex(self, indexableObj, index):
        return indexableObj[index]
    
class TestProxyClass(TestCase):
    class MyClass(object):
        "MyClass's doc string!"
        data = 3.14
        
        def __init__(self, id):
            self.id = id
    
        @classmethod
        def clsMeth(cls):
            return cls
    
        @staticmethod
        def statMeth():
            return 'static'
    
        def instMeth(self):
            return (self, self.id)
        
    def test_wrapData(self):
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        self.assertEqual(Wrapped.data, self.MyClass.data)
        self.assertEqual(Wrapped('foo').data, self.MyClass('foo').data)

    def test_classMethod(self):
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        self.assertEqual(Wrapped.clsMeth(), self.MyClass.clsMeth())

    def test_staticMethod(self):
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        self.assertEqual(Wrapped.statMeth(), self.MyClass.statMeth())
        
    def test_instMethod(self):
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        wrappedResult = Wrapped('bar').instMeth()
        myClassResult = self.MyClass('bar').instMeth()
        self.assertEqual(wrappedResult[0].__class__, myClassResult[0].__class__)
        self.assertEqual(wrappedResult[1], myClassResult[1])

    def test_docString(self):
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        self.assertEqual(Wrapped.__doc__, self.MyClass.__doc__)
        
    def test_immutable(self):
        
        Wrapped = utilitytypes.proxyClass(''.__class__, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        self.assertEqual(Wrapped('Fun times were had by all')[3:7],
                         'Fun times were had by all'[3:7])
        
    
    def test_unboundMethod(self):
        """
        We should be able to do MyProxyClass.wrappedMethod(myProxyClassInst)
        """
        Wrapped = utilitytypes.proxyClass(self.MyClass, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        wrapInst = Wrapped('bar')
        wrappedResult = Wrapped.instMeth(wrapInst)
        myClassResult = self.MyClass('bar').instMeth()
        self.assertEqual(wrappedResult[0].__class__, myClassResult[0].__class__)
        self.assertEqual(wrappedResult[1], myClassResult[1])
        
    def test_unboundMethodDescriptor(self):
        """
        Some built-in types have fun things called method descriptors...
        ...they're like methods, but not!
        """
        Wrapped = utilitytypes.proxyClass(''.__class__, 'Wrapped',
                                          dataAttrName='_data', makeDefaultInit=True)
        theString = 'Fun times were had by all!'
        wrapInst = Wrapped(theString)
        self.assertEqual(Wrapped.__len__(wrapInst), len(theString))

setupUnittestModule(__name__)
