#!/usr/bin/env python

'''
finCam.py - Maya camera and render resolution functions
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

import fin_rmvList as rmv
import maya.cmds as cmds
import maya.mel as mel

### Helper functions
    
def cameraCheck():
    # test to see whether current selection is a camera
    global selectCam
    selectCam = cmds.ls( selection=True )
    a = 0
    for x in selectCam:
        selectCam[a] = selectCam[a] + "Shape"
        a = a + 1
    allCams = cmds.ls( cameras=True )
    isCam = rmv.matchList( selectCam, allCams )
    if isCam == True:
        camMatch = True
    else:
        print "Please select only cameras"
    del selectCam, allCams, isCam
    return camMatch


### The main scripts
        
def renderResolution():
    ## make a new camera based on user selection
    def closeWindow(window):
        cmds.deleteUI('renderRes')
    
    # check for existing window first
    if cmds.window('renderRes', exists=True):
        cmds.deleteUI('renderRes')
        # create the new window
    window = cmds.window('renderRes', width=250, bgc=(.2, .2, .2) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.frameLayout( marginHeight=5, marginWidth=5, labelVisible=False )
    cmds.button( label='2k_1556', command= twoK1556 )
    cmds.button( label='2k_1168', command= twoK1168 )
    cmds.button( label='2k_1162', command= twoK1162 )
    cmds.button( label='2k_1156', command= twoK1156 )
    cmds.button( label='2k_1152', command= twoK1152 )
    cmds.button( label='highDef', command= highDef )
    cmds.button( label='halfRes', command= halfRes )
    cmds.button(label="Cancel", command = closeWindow )
    cmds.showWindow("renderRes")
   
def newCam():
    ## make a new camera based on user selection
    def closeWindow(window):
        cmds.deleteUI('fin_cam')
    
    # check for existing window first
    if cmds.window('fin_cam', exists=True):
        cmds.deleteUI('fin_cam')
        # create the new window
    window = cmds.window('fin_cam', width=250, bgc=(.2, .2, .2) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.frameLayout( marginHeight=5, marginWidth=5, labelVisible=False )
    cmds.button( label='2k_1556_Cam', command= twoK1556Cam )
    cmds.button( label='2k_1168_Cam', command= twoK1168Cam )
    cmds.button( label='2k_1162_Cam', command= twoK1162Cam )
    cmds.button( label='2k_1156_Cam', command= twoK1156Cam )
    cmds.button( label='2k_1152_Cam', command= twoK1152Cam )
    cmds.button( label='highDef_Cam', command= highDefCam )
    cmds.button(label="Close", command = closeWindow )
    cmds.showWindow("fin_cam")
    
    
### Camera and resolution definitions

def twoK1556(self):
    mel.eval( 'setAttr "defaultResolution.width" 2048;' )
    mel.eval( 'setAttr "defaultResolution.height" 1556;' )
    
    
def twoK1168(self):
    mel.eval( 'setAttr "defaultResolution.width" 2048;' )
    mel.eval( 'setAttr "defaultResolution.height" 1168;' )
    
def twoK1162(self):
    mel.eval( 'setAttr "defaultResolution.width" 2048;' )
    mel.eval( 'setAttr "defaultResolution.height" 1162;' )
    
def twoK1156(self):
    mel.eval( 'setAttr "defaultResolution.width" 2048;' )
    mel.eval( 'setAttr "defaultResolution.height" 1156;' )
    
def twoK1152(self):
    mel.eval( 'setAttr "defaultResolution.width" 2048;' )
    mel.eval( 'setAttr "defaultResolution.height" 1152;' )
    
def highDef(self):
    mel.eval( 'setAttr "defaultResolution.width" 1920;' )
    mel.eval( 'setAttr "defaultResolution.height" 1080;' )
    
def halfRes(self):
    curWidth = mel.eval( 'getAttr "defaultResolution.width";' )
    curHeight = mel.eval( 'getAttr "defaultResolution.height";' )
    halfWidth = curWidth/2
    halfHeight = curHeight/2
    mel.eval( 'setAttr "defaultResolution.width" ' + str(halfWidth) + ';' )
    mel.eval( 'setAttr "defaultResolution.height" ' + str(halfHeight) + ';' )
    del curWidth, curHeight, halfWidth, halfHeight
    
def twoK1556Cam(self):
    camName= "fin_01_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.98, vfa=0.745 )
    twoK1556(self)
    del camName, camMake, camShape

def twoK1168Cam(self):
    camName= "fin_02_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.98, vfa=0.559 )
    twoK1168(self)
    del camName, camMake, camShape
    
def twoK1162Cam(self):
    camName= "fin_03_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.98, vfa=0.556 )
    twoK1162(self)
    del camName, camMake, camShape
    
def twoK1156Cam(self):
    camName= "fin_04_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.98, vfa=0.553 )
    twoK1156(self)
    del camName, camMake, camShape

def twoK1152Cam(self):
    camName= "fin_05_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.98, vfa=0.551 )
    twoK1152(self)
    del camName, camMake, camShape
    
def highDefCam(self):
    camName= "fin_06_shotCAM_01"
    camMake = cmds.camera(name=camName)
    camShape = camMake[1]
    cmds.camera( camShape, e=True, ff='horizontal', hfa=0.792, vfa=0.446 )
    highDef(self)
    del camName, camMake, camShape