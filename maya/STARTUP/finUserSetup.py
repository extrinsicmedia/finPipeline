#!/usr/bin/env python

'''
finUserSetup.py - startup file for Maya
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

## IMPORTS ##
import sys
import os
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

## Load Plugins ##
def loadPlugins():
    cmds.loadPlugin( 'finShelf.py' )
    mel.eval( 'if(!`pluginInfo -query -l -n Mayatomr`) loadPlugin "Mayatomr";')
    mel.eval( 'if(!`pluginInfo -query -l -n OpenEXRLoader`) loadPlugin "OpenEXRLoader";')
    mel.eval( 'if(!`pluginInfo -query -l -n stereoCamera`) loadPlugin "stereoCamera";')
    mel.eval( 'if(!`pluginInfo -query -l -n objExport`) loadPlugin "objExport";')
    mel.eval( 'if(!`pluginInfo -query -l -n fbxmaya`) loadPlugin "fbxmaya";')
    
    # set the optionVar that enables hidden mentalray shaders   
    pm.optionVar['MIP_SHD_EXPOSE'] = 1
    pm.runtime.SavePreferences()


## Create group structure for initial organization
def initialStructure():
    cmds.group( em=True, name='___CAM___' )
    cmds.group( em=True, name='___LGT___' )
    cmds.group( em=True, name='___ENV___' )
    cmds.group( em=True, name='___GEO___' )
    cmds.group( em=True, name='___DYN___' )

def newStuff():
    # change render drop down
    cmds.setAttr('defaultRenderGlobals.ren', 'mentalRay', type='string' )
    
def startupMenu():
    pass