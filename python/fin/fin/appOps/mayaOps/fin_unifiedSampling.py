#!/usr/bin/env python

'''
fin_unifiedSampling.py - adds unified sampling to mentalRay render globals
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
import maya.mel as mel

def unifiedRender():
    mel.eval( 'select miDefaultOptions;')
    mel.eval( 'setAttr "miDefaultOptions.scanline" 3;' )

def miDefNum():
    
    miDef = pm.PyNode( 'miDefaultOptions' )
    num = 0

    for n in miDef.stringOptions:
        num = num + 1
    
    return num

def setUnifRen():
    unifiedRender()
    num = miDefNum()
    print num
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "unified sampling";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "true";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "boolean";' )
    num = num + 1
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "samples quality";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "1.0";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "scalar";' )
    num = num + 1
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "samples min";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "1.0";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "scalar";' )
    num = num + 1
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "samples max";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "100.0";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "scalar";' )
    num = num + 1
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "samples error cutoff";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "0.0";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "scalar";' )
    num = num + 1
    
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].name "samples per object";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].value "false";' )
    mel.eval( 'setAttr -type "string" miDefaultOptions.stringOptions[' + str(num) + '].type "boolean";' )
    num = num + 1
    