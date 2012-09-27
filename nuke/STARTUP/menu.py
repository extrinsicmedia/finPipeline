''' menu.py for use with finPipeline
Copyright (C) 2012  Miles Lauridsen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl.html/>.'''


import os
import re
import sys
import nuke
import finTools
import Send2Rush as s2r
import os.path
import djv_this

## get ENV vars
finServer = os.environ.get('SERVER', None)
if finServer == None:
  try:
    finServer = os.environ.get('MOBILE_SERVER', None)
  except:
    print "Set Environment Variables"
  
jobServer = os.environ.get('JOB_SERVER', None)
if jobServer == '':
  jobServer = os.environ.get('MOBILE_JOB_SERVER', None)

user = os.environ.get('USER', None)

### Use DJView as playback
menu = nuke.menu('Nuke')
m = menu.findItem('Render')
m.addCommand('Flipbook Selected in &DJV', 'nukescripts.flipbook( djv_this.djv_this, nuke.selectedNode() )', 'Ctrl+F', index=9)

### Add Favorites directories
nuke.addFavoriteDir('Job Server', jobServer )

toolbar = nuke.toolbar("Nodes")

## LUMA Pictures gizmo collector

if __name__ == '__main__':
  # Just in case they didn't use the supplied init.py
  gizManager = globals().get('gizManager', None)
  if gizManager is None:
      print 'Problem finding GizmoPathManager - check that init.py was setup correctly'
  else:
      gizManager.addGizmoMenuItems()
      # Don't need it no more...
      del gizManager

### Send job to RUSH
## Uncomment this if RUSH is used
#m = menubar.addMenu("Render")
#m.addCommand("Create Paths", "fin_Tools.createPaths()")
#m.addCommand("Fix Paths", "fixPath.fixPath()")
#m.addCommand("Send2Rush", "s2r.Nuke2Rush()")

## Presets Backdrop
presetBackdropMenu = nuke.menu('Nuke').addMenu('presetBackdrop')
presetBackdropMenu.addCommand('Preset Backdrop', 'presetBackdrop.presetBackdrop()', 'ctrl+alt+b')

### End