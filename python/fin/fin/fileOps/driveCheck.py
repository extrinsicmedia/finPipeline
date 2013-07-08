#!/usr/bin/env python

'''
driveCheck.py - A module to list all files recursively in all sub-folders of a
user provided path.
Copyright (C) 2013 FIN VFX Inc.

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

import os
import sys

path = sys.argv[1]
print "Path is: " + path

skip = [ ".DS_Store", ".Spotlight-V100", ".fseventsd", ".Trashes" ]

for (path, dirs, files) in os.walk(path):
    for file in files:
        if file in skip:
            pass
        else:
            f = os.path.join( path, file )
            statinfo = os.stat(f)
            print f, str(round(float(statinfo.st_size)/1024/1024, 5) ) + "MB"