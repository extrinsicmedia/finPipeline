#!/usr/bin/env python

'''
userSetup.py - startup file for Maya users
Copyright (C) 2012  Miles Lauridsen

Based on BSD 2-Clause License  http://opensource.org/licenses/BSD-2-Clause

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

### Symlink this file to the user script directory
### On MacOSX - ln -s $SYSTEMS_SERVER/maya/startup/userSetup.py /Users/<userName>/Library/Preferences/Autodesk/maya/2012-x64/scripts/userSetup.py
### On Windows - 

import sys
import os
import maya.cmds as cmds
import maya.OpenMaya as api
import maya.mel as mel
import maya.utils as mu
import pymel as pm

## Set environment variables
sys.path.append( os.path.join(os.environ.get('MAYA_SHARED_DIR', None), 'startup'))
sys.path.append( os.environ.get('MAYA_PYTHON_PATH', None))
sys.path.append( os.path.join(os.environ.get('MAYA_SHARED_DIR', None), 'external', 'python'))

import finUserSetup as fus

## Print Confirmation that userSetup.py worked
def printConfirm():
    print "FIN Startup Complete"

#pm.mayautils.executeDeferred( 'fus.loadPlugins()' ) # this was the old way of loading
cmds.evalDeferred( 'fus.osPlugins()' )
cmds.evalDeferred('lowestPriority')
cmds.evalDeferred('fus.loadPlugins()')
cmds.evalDeferred( 'fus.initialStructure()' )
cmds.evalDeferred( 'fus.newStuff()' )
cmds.evalDeferred( 'fus.startupCheck()' )
cmds.evalDeferred( 'printConfirm()' )

