import inspect
import itertools
import pymel.util.external.ply.lex as lex
import operator
import os
import re
import sys
import tempfile
import types
import warnings
import pymel.util.external.ply.yacc as yacc

from pymel.util.utilitytypes import *
from pymel.util.common import *
from pymel.util.arguments import *
from collections import *

class ProxyUni(object): pass
class Parsed(ProxyUni): pass


class NameParsed(Parsed):
    def isAttributeName(self):
        """
        True if this object is specified including one or more dag parents
        """
    
        pass
    
    
    def isComponentName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
    
        pass
    
    
    def isNodeName(self):
        """
        True if this dag path name is absolute (starts with '|')
        """
    
        pass


class Component(NameParsed):
    """
    A Maya component name of any of the single, double or triple indexed kind
    
        Rule : Component = SingleComponentName | DoubleComponentName | TripleComponentName
    
        Component Of: `MayaObjectName`
    """
    
    
    
    pass


class MayaShortName(NameParsed):
    """
    A short node name in Maya, a Maya name, possibly preceded by a Namespace
    
        Rule : MayaShortName = `Namespace` ? `MayaName`
    
        Composed Of: `Namespace`, `MayaName`
    
        Component Of: `MayaNodePath`
    """
    
    
    
    def addPrefix(self, prefix):
        """
        Add a prefix to the node name. This must produce a valid maya name (no separators allowed).
        """
    
        pass
    
    
    def addSuffix(self, suffix):
        """
        Add a suffix to the node name. This must produce a valid maya name (no separators allowed).
        """
    
        pass
    
    
    def getBaseName(self):
        """
        Get the short node name of the object
        """
    
        pass
    
    
    def getBaseNamespace(self):
        """
        Get the namespace for the current node
        """
    
        pass
    
    
    def isAbsoluteNamespace(self):
        """
        True if this object is specified in an absolute namespace
        """
    
        pass
    
    
    def setBaseName(self, name):
        """
        Set the name of the object.  Should not include namespace
        """
    
        pass
    
    
    def setNamespace(self, namespace):
        """
        Set the namespace. The provided namespace may be nested and should including a trailing colon unless it is empty.
        """
    
        pass
    
    
    basename = None
    
    first = None
    
    last = None
    
    namespace = None
    
    parts = None


class NameGroup(NameParsed):
    """
    A name group of either the NameAlphaGroup or NameNumGroup kind
    
        Rule : NameGroup = `NameAlphaGroup` | `NameNumGroup`
    
        Composed Of: `NameAlphaGroup`, `NameNumGroup`
    
        Component Of: `MayaName`
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass
    
    
    def nextName(self):
        pass
    
    
    def prevName(self):
        pass
    
    
    first = None
    
    last = None
    
    parts = None
    
    tail = None


class NamePart(NameParsed):
    """
    A name part of either the NameAlphaPart or NameNumPart kind
    
        Rule : NamePart = `NameAlphaPart` | `NameNumPart`
    
        Composed Of: `NameAlphaPart`, `NameNumPart`
    
        Component Of: `NameNumGroup`
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass


class NameSep(NameParsed):
    """
    the MayaName NameGroup separator : one or more underscores
    
        Rule : NameSep = r'_+'
    
        Component Of: `MayaName`
    """
    
    
    
    def reduced(self):
        """
        Reduce multiple underscores to one
        """
    
        pass
    
    
    def default(cls):
        pass


class AttrSep(NameParsed):
    """
    The Maya attribute separator : the dot '.'
    
        Rule : AttrSep = r'\.'
    
        Component Of: `Component`, `AttributePath`, `NodeAttribute`
    """
    
    
    
    def default(cls):
        pass


class AttributePath(NameParsed):
    """
    The full path of a Maya attribute on a Maya node, as one or more AttrSep ('.') separated Attribute
    
        Rule : AttributePath = ( `Attribute` `AttrSep` ) * `Attribute`
    
        Composed Of: `Attribute`, `AttrSep`
    
        Component Of: `NodeAttribute`
    """
    
    
    
    def isCompound(self):
        pass
    
    
    attributes = None
    
    first = None
    
    last = None
    
    parent = None
    
    parents = None
    
    parts = None
    
    path = None
    
    separator = None


class NameRangeIndex(NameParsed):
    """
    An index specification for an attribute or a component index, in the form::
        [<optional int number>:<optional int number>]
    
        Rule : NameIndex = r'\[[0-9]*:[0-9]*\]'
    """
    
    
    
    def default(cls):
        pass
    
    
    def __new__(cls, *args, **kwargs):
        """
        # to allow initialization from one or two int
        """
    
        pass
    
    
    bounds = None
    
    end = None
    
    range = None
    
    start = None


class NamespaceSep(NameParsed):
    """
    The Maya Namespace separator : the colon ':'
    
        Rule : NamespaceSep = r':'
    
        Component Of: `Namespace`
    """
    
    
    
    def default(cls):
        pass


class NodeAttribute(NameParsed):
    """
    The name of a Maya node and attribute (plug): a MayaNodePath followed by a AttrSep and a AttributePath
    
        Rule : NodeAttribute = `MayaNodePath` `AttrSep` `AttributePath`
    
        Composed Of: `MayaNodePath`, `AttrSep`, `AttributePath`
    
        Component Of: `MayaObjectName`
    
    
        >>> nodeAttr = NodeAttribute( 'persp|perspShape.focalLength' )
        >>> nodeAttr.attributes
        (Attribute('focalLength', 17),)
        >>> nodeAttr.nodePath
        MayaNodePath('persp|perspShape', 0)
        >>> nodeAttr.shortName()
        NodeAttribute('perspShape.focalLength', 0)
        >>>
        >>> nodeAttr2 = NodeAttribute( 'persp.translate.tx' )
        >>> nodeAttr2.attributes
        (Attribute('translate', 6), Attribute('tx', 16))
    """
    
    
    
    def popNode(self):
        """
        Remove a node from the end of the path, preserving any attributes (Ex. pCube1|pCubeShape1.width --> pCube1.width).
        """
    
        pass
    
    
    def shortName(self):
        """
        Just the node and attribute without the full dag path. Returns a copy.
        """
    
        pass
    
    
    attribute = None
    
    attributes = None
    
    nodePath = None
    
    parts = None
    
    separator = None


class MayaName(NameParsed):
    """
    The most basic Maya Name : several name groups separated by one or more underscores,
    starting with a NameHead or one or more underscore, followed by zero or more NameGroup
    
        Rule : MayaName = (`NameSep` * `NameAlphaGroup`) | (`NameSep` + `NameNumGroup`)  ( `NameSep` `NameGroup` ) * `NameSep` *
    
        Composed Of: `NameSep`, `NameAlphaGroup`, `NameNumGroup`, `NameGroup`
    
        Component Of: `Namespace`, `MayaShortName`, `Attribute`
    """
    
    
    
    def extractNum(self):
        """
        Return the trailing numbers of the node name. If no trailing numbers are found
        an error will be raised.
        """
    
        pass
    
    
    def nextName(self):
        """
        Increment the trailing number of the object by 1
        """
    
        pass
    
    
    def nextUniqueName(self):
        """
        Increment the trailing number of the object until a unique name is found
        """
    
        pass
    
    
    def prevName(self):
        """
        Decrement the trailing number of the object by 1
        """
    
        pass
    
    
    def reduced(self):
        """
        Reduces all separators in thet Maya Name to one underscore, eliminates head and tail separators if not needed
        """
    
        pass
    
    
    first = None
    
    groups = None
    
    last = None
    
    parts = None
    
    tail = None


class Attribute(NameParsed):
    """
    The name of a Maya attribute on a Maya node, a MayaName with an optional NameIndex
    
        Rule : Attribute = `MayaName` `NameIndex` ?
    
        Composed Of: `MayaName`, `NameIndex`
    
        Component Of: `AttributePath`
    """
    
    
    
    def isCompound(self):
        pass
    
    
    bracketedIndex = None
    
    index = None
    
    name = None
    
    parts = None


class NameIndex(NameParsed):
    """
    An index specification for an attribute or a component index, in the form [<int number>]
    
        Rule : NameIndex = r'\[[0-9]+\]'
    
        Component Of: `Attribute`
    """
    
    
    
    def __new__(cls, *args, **kwargs):
        """
        # to allow initialization from a single int
        """
    
        pass
    
    
    value = None


class MayaNodePath(NameParsed):
    """
    A node name in Maya, one or more MayaShortName separated by DagPathSep, with an optional leading DagPathSep
    
        Rule : MayaNodePath = `DagPathSep` ? `MayaShortName` (`DagPathSep` `MayaShortName`) *
    
        Composed Of: `DagPathSep`, `MayaShortName`
    
        Component Of: `Component`, `NodeAttribute`
    
    Example
        >>> import pymel.util.nameparse as nameparse
        >>> obj = nameparse.parse( 'group1|pCube1|pCubeShape1' )
        >>> obj.setNamespace( 'foo:' )
        >>> print obj
        foo:group1|foo:pCube1|foo:pCubeShape1
        >>> print obj.parent
        foo:group1|foo:pCube1
        >>> print obj.node
        foo:pCubeShape1
        >>> print obj.node.basename
        pCubeShape1
        >>> print obj.node.namespace
        foo:
    """
    
    
    
    def addNamespace(self, namespace):
        """
        Append the namespace for all nodes in this path.
        """
    
        pass
    
    
    def addNode(self, node):
        """
        Add a node to the end of the path
        """
    
        pass
    
    
    def addPrefix(self, prefix):
        """
        Add a prefix to all nodes in the path. This must produce a valid maya name (no separators allowed).
        """
    
        pass
    
    
    def addSuffix(self, suffix):
        """
        Add a suffix to all nodes in the path. This must produce a valid maya name (no separators allowed).
        """
    
        pass
    
    
    def isAbsolute(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
    
        pass
    
    
    def isDagName(self):
        """
        True if this object is specified including one or more dag parents
        """
    
        pass
    
    
    def isLongName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
    
        pass
    
    
    def isShortName(self):
        """
        True if this object node is specified as a short name (without a path)
        """
    
        pass
    
    
    def popNamespace(self, index=0):
        """
        Remove an individual namespace (no separator) from all nodes in this path. An index of 0 (default) is the shallowest (leftmost) in the list.
        Returns a tuple containing the namespace popped from each node in the path or None if the node had no namespaces.
        """
    
        pass
    
    
    def popNode(self, index=-1):
        """
        Remove a node from the end of the path
        """
    
        pass
    
    
    def setNamespace(self, namespace):
        """
        Set the namespace for all nodes in this path. The provided namespace may be nested and should including a trailing colon unless it is empty.
        """
    
        pass
    
    
    def shortName(self):
        """
        The last short name of the path
        """
    
        pass
    
    
    first = None
    
    last = None
    
    node = None
    
    nodePaths = None
    
    nodes = None
    
    parent = None
    
    parents = None
    
    parts = None
    
    root = None
    
    separator = None


class MayaObjectName(NameParsed):
    """
    An object name in Maya, can be a dag object name, a node name,
    an plug name, a component name or a ui name
    
        Rule : MayaObjectName = `MayaNodePath` | `NodeAttribute` | `Component`
    
        Composed Of: `MayaNodePath`, `NodeAttribute`, `Component`
    """
    
    
    
    def isAttributeName(self):
        """
        True if this object is specified including one or more dag parents
        """
    
        pass
    
    
    def isComponentName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
    
        pass
    
    
    def isNodeName(self):
        """
        True if this dag path name is absolute (starts with '|')
        """
    
        pass
    
    
    attribute = None
    
    attributes = None
    
    component = None
    
    node = None
    
    nodes = None
    
    object = None
    
    parts = None
    
    type = None


class DagPathSep(NameParsed):
    """
    The Maya long names separator : the pipe '|'
    
        Rule : DagPathSep = r'\|'
    
        Component Of: `MayaNodePath`
    """
    
    
    
    def default(cls):
        pass


class Namespace(NameParsed):
    """
    A Maya namespace name, one or more MayaName separated by ':'
    
        Rule : Namespace = `NamespaceSep` ? (`MayaName` `NamespaceSep`) +
    
        Composed Of: `NamespaceSep`, `MayaName`
    
        Component Of: `MayaShortName`
    """
    
    
    
    def append(self, namespace):
        """
        Append a namespace. Can include separator and multiple namespaces. The new namespace will be the shallowest (leftmost) namespace.
        """
    
        pass
    
    
    def isAbsolute(self):
        """
        True if this namespace is an absolute namespace path (starts with ':')
        """
    
        pass
    
    
    def pop(self, index=0):
        """
        Remove an individual namespace (no separator). An index of 0 (default) is the shallowest (leftmost) in the list
        """
    
        pass
    
    
    def setSpace(self, index, space):
        """
        Set the namespace at the given index
        """
    
        pass
    
    
    def default(cls):
        pass
    
    
    first = None
    
    last = None
    
    parent = None
    
    parents = None
    
    parts = None
    
    path = None
    
    separator = None
    
    space = None
    
    spaces = None


class NameNumGroup(NameGroup):
    """
    A name group starting with an alphabetic part
    
        Rule : NameAlphaGroup  = `NameAlphaPart` `NamePart` *
    
        Composed Of: `NameAlphaPart`, `NamePart`
    
        Component Of: `MayaName`
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass


class NameAlphaPart(NamePart):
    """
    A name part made of alphabetic letters
    
        Rule : NameAlphaPart = r'([a-z]+)|([A-Z]+[a-z]*)'
    
        Component Of: `NameNumGroup`, `NameAlphaGroup`
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass


class NameNumPart(NamePart):
    """
    A name part made of numbers
    
        Rule : NameNumPart = r'[0-9]+'
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass
    
    
    def __new__(cls, *args, **kwargs):
        """
        # to allow initialization from a single int
        """
    
        pass
    
    
    value = None


class NameAlphaGroup(NameGroup):
    """
    A name group starting with an alphabetic part
    
        Rule : NameAlphaGroup  = `NameAlphaPart` `NamePart` *
    
        Composed Of: `NameAlphaPart`, `NamePart`
    
        Component Of: `NameNumGroup`
    """
    
    
    
    def isAlpha(self):
        pass
    
    
    def isNum(self):
        pass

def getBasicPartList(name):
    """
    convenience function for breaking apart a maya object to the appropriate level for pymel name parsing
    
        >>> getBasicPartList('thing|foo:bar.attr[0].child')
        [MayaNodePath('thing|foo:bar', 0), MayaName('attr', 14), NameIndex('[0]', 18), MayaName('child', 22)]
    """

    pass


def parse(name):
    """
    main entry point for parsing a maya node name
    """

    pass

__all__ = ['NamePart',
 'NameAlphaPart',
 'NameNumPart',
 'NameGroup',
 'NameAlphaGroup',
 'NameNumGroup',
 'NameSep',
 'MayaName',
 'NamespaceSep',
 'Namespace',
 'MayaShortName',
 'DagPathSep',
 'MayaNodePath',
 'AttrSep',
 'NameIndex',
 'NameRangeIndex',
 'Component',
 'Attribute',
 'AttributePath',
 'NodeAttribute',
 'MayaObjectName',
 'getBasicPartList',
 'parse']
