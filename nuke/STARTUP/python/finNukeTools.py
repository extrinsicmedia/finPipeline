''' finNukeTools.py - various python functions for use in Nuke
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

import nuke
import os
import nukescripts
import re
import operator
import random
        
def postageStampOff():
    for n in nuke.selectedNodes():
        n.knob("postage_stamp").setValue(0)
        
def postageStampOn():
    for n in nuke.selectedNodes():
        n.knob("postage_stamp").setValue(1)
        
### Create paths
def createPaths():
    n = nuke.allNodes()
    for x in n:
        if x.Class() == "Write":
            path = x.knob("file").value()
            path = path.split("/")
            pathNum = len(path)
            pathNum = pathNum - 1
            del path[pathNum]
            path = "/".join(path)
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
                create = True
    if create == True:
        nuke.message( "Paths have been created" )