"""
Contains functions for easily comparing versions of Maya with the current running version.
Class for storing apiVersions, which are the best method for comparing versions. ::

    >>> from pymel import versions
    >>> if versions.current() >= versions.v2008:
    ...     print "The current version is later than Maya 2008"
    The current version is later than Maya 2008
"""

import re
import struct

from maya.OpenMaya import *

def bitness():
    """
    The bitness of python running inside Maya as an int.
    """

    pass


def current():
    pass


def flavor():
    pass


def fullName():
    pass


def installName():
    pass


def is64bit():
    pass


def isComplete():
    pass


def isEval():
    pass


def isRenderNode():
    pass


def isUnlimited():
    pass


def parseVersionStr(versionStr, extension=False):
    """
    >>> from pymel.all import *
    >>> versions.parseVersionStr('2008 Service Pack1 x64')
    '2008'
    >>> versions.parseVersionStr('2008 Service Pack1 x64', extension=True)
    '2008-x64'
    >>> versions.parseVersionStr('2008x64', extension=True)
    '2008-x64'
    >>> versions.parseVersionStr('8.5', extension=True)
    '8.5'
    >>> versions.parseVersionStr('2008 Extension 2')
    '2008'
    >>> versions.parseVersionStr('/Applications/Autodesk/maya2009/Maya.app/Contents', extension=True)
    '2009'
    >>> versions.parseVersionStr('C:\Program Files (x86)\Autodesk\Maya2008', extension=True)
    '2008'
    """

    pass


def shortName():
    pass

v2008 = 200800

v2008_EXT2 = 200806

v2008_SP1 = 200806

v2009 = 200900

v2009_EXT1 = 200904

v2009_SP1A = 200906

v2010 = 201000

v2011 = 201100

v2011_HOTFIX1 = 201101

v2011_HOTFIX2 = 201102

v2011_HOTFIX3 = 201103

v2011_SP1 = 201104

v2012 = 201200

v85 = 200700

v85_SP1 = 200701
