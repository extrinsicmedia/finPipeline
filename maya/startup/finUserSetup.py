#!/usr/bin/env python

'''
finUserSetup.py - startup file for Maya using FIN pipeline workflow
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

## IMPORTS ##
import sys
import os
import platform
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm

## Set Plugin Paths for specific OS
def osPlugins():
    try:
        # Load Maya 2013 plugins
        if pm.versions.current() in ( 201350, 2013 ):
            if platform.system() in ( 'Darwin', 'Apple' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'osx_maya2013'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'osx_maya2013')])
                
            if platform.system() in ( 'Windows', 'Microsoft' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'win_maya2013'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'win_maya2013')])
                
            if platform.system() in ( 'Linux', 'Linux2' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'linux_maya2013'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'linux_maya2013')])
                
        # Load Maya 2014 plugins
        elif pm.versions.current() in ( 201402, 2014 ):
            if platform.system() in ( 'Darwin', 'Apple' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'osx_maya2014'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'osx_maya2014')])
                
            if platform.system() in ( 'Windows', 'Microsoft' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'win_maya2013'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'win_maya2013')])
                
            if platform.system() in ( 'Linux', 'Linux2' ):
                os.environ['MAYA_PLUG_IN_PATH'] = os.pathsep.join( \
                            [ os.environ.get('MAYA_PLUG_IN_PATH'), \
                            os.path.join(os.environ.get('MAYA_EXTERNAL_PLUGIN_PATH', None), 'linux_maya2013'), \
                            os.path.join(os.environ.get('MAYA_FIN_PLUGIN_PATH', None), 'linux_maya2013')])
                
    except:
        raise RuntimeError('Please make sure plugin path is set correctly')

## Load Plugins ##
def loadPlugins():
    cmds.loadPlugin( 'finShelf.py' )
    mel.eval( 'if(!`pluginInfo -query -l -n Mayatomr`) loadPlugin "Mayatomr";')
    mel.eval( 'if(!`pluginInfo -query -l -n OpenEXRLoader`) loadPlugin "OpenEXRLoader";')
    mel.eval( 'if(!`pluginInfo -query -l -n stereoCamera`) loadPlugin "stereoCamera";')
    mel.eval( 'if(!`pluginInfo -query -l -n objExport`) loadPlugin "objExport";')
    mel.eval( 'if(!`pluginInfo -query -l -n fbxmaya`) loadPlugin "fbxmaya";')
    
    # external plugins
    try:
        cmds.loadPlugin( 'SOuP.bundle')
        mel.eval( 'if(!`pluginInfo -query -l -n "SOuP"`) loadPlugin "SOuP";')
        mel.eval('if (`shelfLayout -exists soup `) deleteUI soup;')
        mel.eval('loadNewShelf "shelf_soup.mel"')
        
        if pm.versions.current() in ( 201402, 2014 ):
            mel.eval( 'if(!`pluginInfo -query -l -n "MASH-2014"`) loadPlugin "MASH-2014";')
            mel.eval('if (`shelfLayout -exists MASH `) deleteUI MASH;')
            mel.eval('loadNewShelf "shelf_MASH.mel"')
    
    except:
        print "Check external plugin paths"
    
    # set the optionVar that enables hidden mentalray shaders   
    pm.optionVar['MIP_SHD_EXPOSE'] = 1
    pm.runtime.SavePreferences()
    
    cmds.setAttr('defaultRenderGlobals.ren', 'mentalRay', type='string' )


## Create group structure for initial organization
def initialStructure():
    cmds.group( em=True, name='___CAM___' )
    cmds.group( em=True, name='___LGT___' )
    cmds.group( em=True, name='___ENV___' )
    cmds.group( em=True, name='___GEO___' )
    cmds.group( em=True, name='___DYN___' )

def newStuff():
    # test stuff goes here
    pass
    
    
def startupCheck():
    #import finMayaToolsInstall
    pass