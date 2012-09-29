import internal as _internal
import os
import platform
import re
import sys
import versions

from logging import *
from pymel.util.path import *

def executeDeferred(func, *args, **kwargs):
    """
    This is a wrap for maya.utils.executeDeferred.  Maya's version does not execute at all when in batch mode, so this
    function does a simple check to see if we're in batch or interactive mode.  In interactive it runs maya.utils.executeDeferred,
    and if we're in batch mode, it just executes the function.
    
    Use this function in your userSetup.py file if:
        1. you are importing pymel there
        2. you want to execute some code that relies on maya.cmds
        3. you want your userSetup.py to work in both interactive and standalone mode
    
    Example userSetup.py file::
    
        from pymel.all import *
        def delayedStartup():
           print "executing a command"
           pymel.about(apiVersion=1)
        mayautils.executeDeferred( delayedStartup )
    
    Takes a single parameter which should be a callable function.
    """

    pass


def getMayaAppDir(versioned=False):
    """
    Determine the Maya application directory, first by checking MAYA_APP_DIR, then by
    trying OS-specific defaults.
    
    if versioned is True, the current Maya version including '-x64' suffix, if applicable, will be appended.
    """

    pass


def getMayaLocation(version=None):
    """
    Remember to pass the FULL version (with extension if any) to this function!
    """

    pass


def getUserPrefsDir():
    pass


def getUserScriptsDir():
    pass


def recurseMayaScriptPath(roots=[], verbose=False, excludeRegex=None, errors='warn', prepend=False):
    """
    Given a path or list of paths, recurses through directories appending to the MAYA_SCRIPT_PATH
    environment variable
    
    :Parameters:
        roots
            a single path or list of paths to recurse. if left to its default, will use the current
            MAYA_SCRIPT_PATH values
    
        verobse : bool
            verbose on or off
    
        excludeRegex : str
            string to be compiled to a regular expression of paths to skip.  This regex only needs to match
            the folder name
    """

    pass


def source(file, searchPath=None, recurse=False):
    """
    Looks for a python script in the specified path (uses system path if no path is specified)
    and executes it if it's found
    """

    pass

sep = ':'
