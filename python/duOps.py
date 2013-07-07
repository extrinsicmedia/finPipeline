#!/usr/bin/env python

'''
duOps.py - A module to do various bash 'du' commands
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

from subprocess import Popen, PIPE, STDOUT

## imports required for testing
import sys

path = sys.argv[1]

# modules
def duDir(path):
    cmd = "cd " + path + " && du -s *"
    p = subprocess.Popen(cmd, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate()
    return stdout, stderr