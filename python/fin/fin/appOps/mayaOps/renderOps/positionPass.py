#!/usr/bin/env python

import os
import pymel.core as pm
import fin_renderPass as frp
import time

def posPassWorldSetup():
    # create the required shaders and nodes
    pm.shadingNode( 'surfaceShader', name='posPassWorldShader', asShader=True)
    pm.shadingNode( 'samplerInfo', name='samplerInfo01', asShader=True )
    pm.shadingNode( 'writeToColorBuffer', name='posPassWorldBuffer', asShader=True )
    
    # connect our shaders
    pm.connectAttr( 'samplerInfo01.pointWorld', 'posPassWorldShader.outColor' )
    pm.connectAttr( 'posPassWorldShader.outColor', 'posPassWorldBuffer.color' )
    
    # create our render pass using presets for colorBuffer
    frp.customColorPass('posPassWorld')
    pm.setAttr( 'posPassWorld.frameBufferType', 512 )
    
    # connect our render pass to the customBuffer and use it for the current render layer
    pm.connectAttr( 'posPassWorld.message', 'posPassWorldBuffer.renderPass' )
    pm.connectAttr( 'defaultRenderLayer.renderPass', 'posPassWorld.owner' )
    
    
    