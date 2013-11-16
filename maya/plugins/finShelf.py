#!/usr/bin/env python

'''
finShelf.py - A plugin to create a dynamic shelf system in Maya.  Based on a
tutorial by Nicolas Koubi http://etoia.free.fr
Copyright (c) 2013  Miles Lauridsen

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

    ## SYS
try:
    import sys
except ImportError: 
    print "sys import failed"


    ## OS
try:
    import os
except ImportError: 
    print "os import failed"


    ## MAYA.MEL
try:
    import maya.mel as mel
except ImportError: 
    print "maya.mel import failed"


    ## MAYA.CMDS
try:
    import maya.cmds as cmds
except ImportError: 
    print "maya.cmds import failed"


    ## MINIDOM
try:
    from xml.dom import minidom
except ImportError: 
    print "minidom import failed"


## Set Paths ##

# Get the Maya files shared directory
sharedDir = os.environ.get('MAYA_SHARED_DIR', None)

# Get icons path from the Maya.env ICONS_PATH variable
iconsPath = os.environ.get('MAYA_ICON_PATH', None)

# Get project name from the Maya.env PRJ_NAME variable
prjName = os.environ.get('MAYA_DYN_SHELF_NAME', None)

# Set the configs folder path
prjConfFiles = os.path.join(sharedDir, "shelves", prjName, "configs")

#####################################################################
## initializePlugin
#####################################################################
##
## Initialize plug-in and create shelf.
##
#####################################################################
def initializePlugin(mobject):
    
    ## Get the shelf configuration file
    shelfConfFile = os.path.join(prjConfFiles, 'dynamicShelfConf.xml')
    
    ## Check if the file exist before continuing
    if os.path.exists(shelfConfFile) == True :
        

        ## This is a fix for the automatically saved shelf function
        ## It will delete a previously shelf created with the plugin if any exist
        mel.eval('if (`shelfLayout -exists finShelf `) deleteUI finShelf;')
        
        ## Declare the $gShelfTopLevel variable as a python variable
        ## The $gShelfTopLevel mel variable is the Maya default variable for the shelves bar UI
        shelfTab = mel.eval('global string $gShelfTopLevel;')
        ## Declare the $finShelf (the shelfLayout) as a global variable in order to unload it after
        mel.eval('global string $finShelf;')
        ## Create a new shelfLayout in $gShelfTopLevel
        mel.eval('$finShelf = `shelfLayout -cellWidth 33 -cellHeight 33 -p $gShelfTopLevel finShelf`;')
        
        

        ## Parse the menuConfFile
        xmlMenuDoc = minidom.parse(shelfConfFile)
        
        ## Loop trough each shelfItem entry in the shelfConfFile
        for eachShelfItem in xmlMenuDoc.getElementsByTagName("shelfItem"):
        
            ## Get the icon name
            getIcon = eachShelfItem.attributes['icon'].value
            ## Join the icon name to the icons path in order to get the full path of the icon
            shelfBtnIcon = os.path.join(iconsPath, getIcon)
            ## Get the annotation
            getAnnotation = eachShelfItem.attributes['ann'].value
            ## Get the command to launch
            getCommand = eachShelfItem.attributes['cmds'].value

        ## Create the actual shelf button with the above parameters
            cmds.shelfButton(command=getCommand, annotation=getAnnotation, image=shelfBtnIcon)
            
            
        ## Rename the shelfLayout with the prjName
        mel.eval('tabLayout -edit -tabLabel $finShelf "'+prjName+'" $gShelfTopLevel;')
        
     
        print "//-- "+prjName+" shelf successfully loaded --//"
    
    
    
#####################################################################
## uninitializePlugin
#####################################################################
##
## Un-Initialize plug-in and delete shelf.
##
#####################################################################
def uninitializePlugin(mobject):
    ## Delete the finShelf if it exist
    mel.eval('if (`shelfLayout -exists finShelf `) deleteUI finShelf;')
