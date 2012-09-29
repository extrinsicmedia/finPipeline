"""
This module is always imported during Maya's startup.  It is imported from
both the maya.app.startup.batch and maya.app.startup.gui scripts
"""
import atexit
import os.path
import sys
import traceback
import maya
import maya.app
import maya.app.commands
from maya import cmds, utils

def setupScriptPaths():
    """
    Add Maya-specific directories to sys.path
    """
    # Extra libraries
    #
    try:
        # Tkinter libraries are included in the zip, add that subfolder
        p = [p for p in sys.path if p.endswith('.zip')][0]
        sys.path.append( os.path.join(p,'lib-tk') )
    except:
        pass
    
    # Per-version prefs scripts dir (eg .../maya8.5/prefs/scripts)
    #
    prefsDir = cmds.internalVar( userPrefDir=True )
    sys.path.append( os.path.join( prefsDir, 'scripts' ) )
    
    # Per-version scripts dir (eg .../maya8.5/scripts)
    #
    scriptDir = cmds.internalVar( userScriptDir=True )
    sys.path.append( os.path.dirname(scriptDir) )
    
    # User application dir (eg .../maya/scripts)
    #
    appDir = cmds.internalVar( userAppDir=True )
    sys.path.append( os.path.join( appDir, 'scripts' ) )
    
def executeSetup(filename):
    """
    Look for the given file name in the search path and execute it in the "__main__"
    namespace
    """
    try:
        for path in sys.path[:]:
            scriptPath = os.path.join( path, filename )
            if os.path.isfile( scriptPath ):
                import __main__
                execfile( scriptPath, __main__.__dict__ )
    except Exception, err:
        # err contains the stack of everything leading to execfile,
        # while sys.exc_info returns the stack of everything after execfile
        try:
            # extract the stack trace for the current exception
            etype, value, tb = sys.exc_info()
            tbStack = traceback.extract_tb(tb)
        finally:
            del tb # see warning in sys.exc_type docs for why this is deleted here
        sys.stderr.write("Failed to execute %s\n" % filename)
        sys.stderr.write("Traceback (most recent call last):\n")
        # format the traceback, excluding our current level
        result = traceback.format_list( tbStack[1:] ) + traceback.format_exception_only(etype, value)
        sys.stderr.write(''.join(result))

def executeUserSetup():
    executeSetup('userSetup.py')

def executeSiteSetup():
    executeSetup('siteSetup.py')
    
# Set up sys.path to include Maya-specific user script directories.
setupScriptPaths()

# Set up string table instance for application
maya.stringTable = utils.StringTable()

# Set up auto-load stubs for Maya commands implemented in libraries which are not yet loaded
maya.app.commands.processCommandList()

# Set up the maya logger before userSetup.py runs, so that any custom scripts that
# use the logger will have it available
utils.shellLogHandler()

if not os.environ.has_key('MAYA_SKIP_USERSETUP_PY'):
    # Run the user's userSetup.py if it exists
    executeSiteSetup()
    executeUserSetup()

# Register code to be run on exit
atexit.register( maya.app.finalize )
# Copyright (C) 1997-2011 Autodesk, Inc., and/or its licensors.
# All rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Autodesk, Inc. ("Autodesk") and/or its licensors,
# which is protected by U.S. and Canadian federal copyright law and by
# international treaties.
#
# The Data is provided for use exclusively by You. You have the right to use,
# modify, and incorporate this Data into other products for purposes authorized 
# by the Autodesk software license agreement, without fee.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. AUTODESK
# DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTIES
# INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF NON-INFRINGEMENT,
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, OR ARISING FROM A COURSE 
# OF DEALING, USAGE, OR TRADE PRACTICE. IN NO EVENT WILL AUTODESK AND/OR ITS
# LICENSORS BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL,
# DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF AUTODESK AND/OR ITS
# LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY OR PROBABILITY OF SUCH DAMAGES.

