#!/usr/bin/env python

'''
fin_exr.py - a function to change the render global settings
to use EXR as file format for rendering.
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

import pymel.core as pm

def fin_exr():
    
    dRG = pm.PyNode( 'defaultRenderGlobals' )
    dRG.setAttr( 'imageFormat', 51 )
    dRG.setAttr( 'imfkey', 'exr' )
    dRG.setAttr( 'outFormatControl', 0 )
    dRG.setAttr( 'animation', 1 )
    dRG.setAttr( 'putFrameBeforeExt', 1 )
    dRG.setAttr( 'extensionPadding', 4 )
    
    # TODO - Get the framerange from a db
    #dRG.setAttr( 'startFrame', startFrame )
    #dRG.setAttr( 'endFrame', endFrame )
    
    dRG.setAttr( 'imageFilePrefix', "<Scene>/<RenderLayer>" )
    dRG.setAttr( 'multiCamNamingMode', 1 )
    dRG.setAttr( 'bufferName', "<RenderPass>" )
    
    mDF = pm.PyNode( 'miDefaultFramebuffer' )
    mDF.setAttr( 'datatype', 5 )
    
    mRG = pm.PyNode( 'mentalrayGlobals' )
    mRG.setAttr('imageCompression', 4)