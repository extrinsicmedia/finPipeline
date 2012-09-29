"""
There are a number of pymel objects which must be converted to a "mel-friendly"
representation. For example, in versions prior to 2009, some mel commands (ie, getAttr) which expect
string arguments will simply reject custom classes, even if they have a valid string representation.
Another Example is mel's matrix inputs, which expects a flat list of 16 flaots, while pymel's Matrix has a more typical
4x4 representation.

If you're having compatibility issues with your custom classes when passing them to maya.cmds,
simply add a __melobject__ function that returns a mel-friendly result and pass them to pymel's wrapped commands.

The wrapped commands in this module are the starting point for any other pymel customizations.
"""

import inspect
import maya
import os
import re
import sys
import pymel.util as util
import pymel.versions as versions
import warnings

from exceptions import *
from maya.cmds import *

def getMelRepresentation(args, recursionLimit=None, maintainDicts=True):
    """
    Will return a list which contains each element of the iterable 'args' converted to a mel-friendly representation.
    
    :Parameters:
        recursionLimit : int or None
            If an element of args is itself iterable, recursionLimit specifies the depth to which iterable elements
            will recursively search for objects to convert; if ``recursionLimit==0``, only the elements
            of args itself will be searched for PyNodes -  if it is 1, iterables within args will have getMelRepresentation called
            on them, etc.  If recursionLimit==None, then there is no limit to recursion depth.
    
        maintainDicts : bool
            In general, all iterables will be converted to tuples in the returned copy - however, if maintainDicts==True,
            then iterables for which ``util.isMapping()`` returns True will be returned as dicts.
    """

    pass

__all__ = ['getMelRepresentation']
