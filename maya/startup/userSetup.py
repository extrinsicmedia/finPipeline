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
sys.path.append( os.path.join(os.environ.get('MAYA_SHARED_DIR', None) , 'startup') )
sys.path.append( os.environ.get('MAYA_PYTHON_PATH', None))

import finUserSetup as fus

## Print Confirmation that userSetup.py worked
def printConfirm():
    print "FIN Startup Complete"

pm.mayautils.executeDeferred( 'fus.osPlugins()' )
pm.mayautils.executeDeferred( 'fus.loadPlugins()' )
pm.mayautils.executeDeferred( 'fus.initialStructure()' )
pm.mayautils.executeDeferred( 'fus.newStuff()' )
pm.mayautils.executeDeferred( 'fus.startupCheck()' )
pm.mayautils.executeDeferred( 'printConfirm()' )

