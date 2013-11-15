#!/usr/bin/env python

'''
userSetup.py - startup file for Maya users
Copyright (C) 2012  Miles Lauridsen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl.html/>.
'''

### Copy this file to the user script directory
### On MacOSX - /Users/<userName>/Library/Preferences/Autodesk/maya/2012-x64/scripts
### On Windows - 

import sys
import os
import maya.cmds as cmds
import maya.OpenMaya as api
import maya.mel as mel
import maya.utils as mu

## get environment variables
scriptsPath = os.environ.get('MAYA_SCRIPT_PATH', None)
mayaPythonPath = os.environ.get('MAYA_PYTHON_PATH', None)
startupPath = os.path.join(os.environ.get('MAYA_SHARED_DIR', None) , 'STARTUP')

sys.path.append( startupPath )
sys.path.append( mayaPythonPath )

import finUserSetup as fus

## Print Confirmation that userSetup.py worked
def printConfirm():
    print "FIN Startup Complete"

mu.executeDeferred( 'fus.loadPlugins()' )
mu.executeDeferred( 'fus.initialStructure()' )
mu.executeDeferred( 'fus.newStuff()' )
mu.executeDeferred( 'fus.startupMenu()' )
mu.executeDeferred( 'printConfirm()' )

