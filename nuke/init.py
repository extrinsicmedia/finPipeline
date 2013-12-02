''' init.py for use with finPipeline
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

import os
import platform
import sys
import nuke
import re

### BEGIN FILEPATH CORRECTION ###
# Make all filepaths load without errors regardless of OS
def myFilenameFilter(filename):
    if nuke.env['MACOS']:
        filename = filename.replace( os.environ.get('WIN_SERVER', None), os.environ.get('MAC_SERVER', None) )
        filename2 = filename.replace( os.environ.get('NIX_SERVER', None), os.environ.get('MAC_SERVER', None) )

    if nuke.env['WIN32']:
        filename = filename.replace( os.environ.get('MAC_SERVER', None), os.environ.get('WIN_SERVER', None) )
        filename2 = filename.replace( os.environ.get('NIX_SERVER', None), os.environ.get('WIN_SERVER', None) )

    if nuke.env['LINUX']:
            filename = filename.replace( os.environ.get('MAC_SERVER', None), os.environ.get('NIX_SERVER', None) )
            filename2 = filename.replace( os.environ.get('WIN_SERVER', None), os.environ.get('NIX_SERVER', None) )

    return filename, filename2

# Use the filenameFilter(s)
nuke.addFilenameFilter(myFilenameFilter)
### END FILEPATH CORRECTION ###

### BEGIN PLUGIN ADDITIONS ###
nuke.pluginAddPath(os.path.join('plugins', 'all', 'pixelfudger'))

# Add OS specific paths to directories
if nuke.env['MACOS']:
    
    # Add gizmos
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'gizmos'))
    print "GIZMOS:", os.path.join(os.environ.get('NUKE_STARTUP', None), 'gizmos')
    
    # Add tcl
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'tcl'))
    
    # Add icons
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'icons'))
    
    # Add python
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'python'))
    print "PYTHON:", os.path.join(os.environ.get('NUKE_STARTUP', None), 'python')
    
    # Add OSX plugins
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'plugins', 'osx'))

    # Add Geometry plugins
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'plugins', 'osx', 'geometry'))
    
    # Add Dynamics plugins
    nuke.pluginAddPath(os.path.join(os.environ.get('NUKE_STARTUP', None), 'plugins', 'osx', 'dynamics'))

### END PLUGIN ADDITIONS ###


## get all folders in $SHARED_SERVER location and add their path to Nuke
nukeDirs = []
for dirname, dirnames, filenames in os.walk(os.environ.get('NUKE_STARTUP', None) ):
    for subdirname in dirnames:
        print "Appending:", os.path.join(dirname, subdirname)
        nukeDirs.append(os.path.join(dirname, subdirname))

for path in nukeDirs:
    nuke.pluginAddPath(path)

    
## LUMA gizmo collector
CUSTOM_GIZMO_LOCATION = os.path.join(os.environ.get('NUKE_STARTUP', None), 'gizmos')

class GizmoPathManager(object):
    def __init__(self, exclude=r'^\.', searchPaths=None):
        '''Used to add folders within the gizmo folder(s) to the gizmo path
        
        exclude: a regular expression for folders / gizmos which should NOT be
            added; by default, excludes files / folders that begin with a '.'
            
        searchPaths: a list of paths to recursively search; if not given, it
            will use the NUKE_GIZMO_PATH environment variable; if that is
            not defined, it will use the directory in which this file resides;
            and if it cannot detect that, it will use the pluginPath 
        '''
        if isinstance(exclude, basestring):
            exclude = re.compile(exclude)
        self.exclude = exclude
        if searchPaths is None:
            searchPaths = os.environ.get('NUKE_GIZMO_PATH', '').split(os.pathsep)
            if not searchPaths:
                import inspect
                thisFile = inspect.getsourcefile(lambda: None)
                if thisFile:
                    searchPaths = [os.path.dirname(os.path.abspath(thisFile))]
                else:
                    searchPaths = list(nuke.pluginPath())
        self.searchPaths = searchPaths
        self.reset()
        
    @classmethod
    def canonical_path(cls, path):
        return os.path.normcase(os.path.normpath(os.path.realpath(os.path.abspath(path))))
        
    def reset(self):
        self._crawlData = {}
        
    def addGizmoPaths(self):
        '''Recursively search searchPaths for folders to add to the nuke
        pluginPath.
        '''
        self.reset()
        self._visited = set()
        for gizPath in self.searchPaths:
            self._recursiveAddGizmoPaths(gizPath, self._crawlData,
                                         foldersOnly=True)
            
    def _recursiveAddGizmoPaths(self, folder, crawlData, foldersOnly=False):
        # If we're in GUI mode, also store away data in _crawlDatato to be used
        # later by addGizmoMenuItems
        if not os.path.isdir(folder):
            return
        
        if nuke.GUI:
            if 'files' not in crawlData:
                crawlData['gizmos'] = []
            if 'dirs' not in crawlData:
                crawlData['dirs'] = {}

        # avoid an infinite loop due to symlinks...
        canonical_path = self.canonical_path(folder)
        if canonical_path in self._visited:
            return
        self._visited.add(canonical_path)
        
        for subItem in sorted(os.listdir(canonical_path)):
            if self.exclude and self.exclude.search(subItem):
                continue
            subPath = os.path.join(canonical_path, subItem)
            if os.path.isdir(subPath):
                nuke.pluginAppendPath(subPath)
                subData = {}
                if nuke.GUI:
                    crawlData['dirs'][subItem] = subData
                self._recursiveAddGizmoPaths(subPath, subData)
            elif nuke.GUI and (not foldersOnly) and os.path.isfile(subPath):
                name, ext = os.path.splitext(subItem)
                if ext == '.gizmo':
                    crawlData['gizmos'].append(name)
                    
    def addGizmoMenuItems(self, toolbar=None, defaultTopMenu=None):
        '''Recursively create menu items for gizmos found on the searchPaths.
        
        Only call this if you're in nuke GUI mode! (ie, from inside menu.py)
        
        toolbar - the toolbar to which to add the menus; defaults to 'Nodes'
        defaultTopMenu - if you do not wish to create new 'top level' menu items,
            then top-level directories for which there is not already a top-level
            menu will be added to this menu instead (which must already exist)
        '''        
        if not self._crawlData:
            self.addGizmoPaths()
            
        if toolbar is None:
            toolbar = nuke.menu("Nodes")
        elif isinstance(toolbar, basestring):
            toolbar = nuke.menu(toolbar)
        self._recursiveAddGizmoMenuItems(toolbar, self._crawlData,
                                         defaultSubMenu=defaultTopMenu,
                                         topLevel=True)
    
    def _recursiveAddGizmoMenuItems(self, toolbar, crawlData,
                                    defaultSubMenu=None, topLevel=False):
        for name in crawlData.get('gizmos', ()):
            niceName = name
            if niceName.find('_v')==len(name) - 4:
                niceName = name[:-4]
            toolbar.addCommand(niceName,"nuke.createNode('%s')" % name)
            
        for folder, data in crawlData.get('dirs', {}).iteritems():
            import sys
            subMenu = toolbar.findItem(folder)
            if subMenu is None:
                if defaultSubMenu:
                    subMenu = toolbar.findItem(defaultSubMenu)
                else:
                    subMenu = toolbar.addMenu(folder)
            self._recursiveAddGizmoMenuItems(subMenu, data)
                    
if __name__ == '__main__':
    if CUSTOM_GIZMO_LOCATION and os.path.isdir(CUSTOM_GIZMO_LOCATION):
        gizManager = GizmoPathManager(searchPaths=[CUSTOM_GIZMO_LOCATION])
    else:
        gizManager = GizmoPathManager()
    gizManager.addGizmoPaths()
    if not nuke.GUI:
        # We're not gonna need it anymore, cleanup...
        del gizManager


### Read and Write nodes change defaults
nuke.knobDefault("Read.before", "black")
nuke.knobDefault("Read.after", "black")
    

### Image Formats
nuke.addFormat ("2048 1556 2.0 2k_anamorphic")
nuke.addFormat ("4096 3112 2.0 4k_anamorphic")
nuke.addFormat ("2048 1556 1.0 2k_super35_cc")
nuke.addFormat ("2048 1168 1.0 2k_3perf_1168")
nuke.addFormat ("2048 1162 1.0 2k_3perf_1162")
nuke.addFormat ("2048 1156 1.0 2k_3perf_1156")
nuke.addFormat ("2048 1152 1.0 2k_3perf_1152")
nuke.addFormat ("960 540 1.0 half_HD")
nuke.addFormat ("720 405 1.0 email")
