#!/usr/bin/env python
''' dirOps.py - A module to read/write xml files that contain directory trees.
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
import sys
import argparse
import subprocess

try:
    import xml.etree.ElementTree as ET
except Exception as e:
    print e.message, e.args

### Set up our commandline parser
parser = argparse.ArgumentParser(description='Create or Read a directory structure from an XML file.')
parser.add_argument( '-w', action="store_true", default=False, dest="writexml",
                    help="Set dirToXML to true" )
parser.add_argument( '-rw', action="store_true", default=False, dest="xmltodir",
                    help="Set xmlToDir to true" )
parser.add_argument( '--dir', action="store", dest="dir",
                    help="Directory to parse and generate a tree from as a path." )
parser.add_argument( '--outfile', action="store", dest="outfile",
                    help="File name to save tree output to as xml." )
parser.add_argument( '--prjname', action="store", dest="prjname",
                    help="Project name to create directory structure for." )
parser.add_argument( '--infile', action="store", dest="infile",
                    help="XML file to generate directory structure from." )
results = parser.parse_args()

### Set the variables we get from argparse and do some dir and file checking
if results.dir:
    dir = results.dir

if results.outfile:
    if os.path.split(results.outfile)[0] in ['', None]:
        outfile = os.path.join( os.environ.get("DB_SERVER", None), "xml",
                               results.outfile )
        print "Outfile is: " + outfile
        
    else:
        if os.path.isdir(os.path.split(results.outfile)[0]):
            outfile = results.outfile
            print "Outfile is: " + outfile

if results.prjname:
    prjname = os.path.join( os.environ.get("JOB_SERVER", None), results.prjname)
    print "Prjname is: " + prjname

if results.infile:
    if os.path.split(results.infile)[0] in ['', None]:
        infile = os.path.join( os.environ.get("DB_SERVER", None), "xml", results.infile )
        if os.path.isfile(infile):
            print "Infile is: " + infile
    else:
        if os.path.isfile(results.infile):
            infile = results.infile
            print "Infile is: " + infile

### Set the definitions

def dirToXML(dir, outfile):
    
    cmd = ["tree", "-X", "-o", outfile ]
    p = subprocess.Popen( cmd,
                         cwd=dir,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE )
    stdout, stderr = p.communicate()
    
    try:
        subprocess.check_output(["tree", "-X", "-o", outfile ])
    except Exception as e:
        print e.message, e.args

def xmlToDir(infile, prjname):
    element = ET.parse(infile)
    tree = ET.ElementTree(element)
    root = tree.getroot()
    if os.path.isdir( os.path.split(prjname)[0] ):
        if os.path.exists(prjname):
            print "Error: This directory already exists"
            sys.exit
        else:
            os.mkdir(prjname)
            createDir( root, basedir=prjname)
 
def createDir(elem, basedir = None):
    """Creates directory structure from XML."""
    lDirs = elem.findall("directory")
    for i, each in enumerate(lDirs):
        # skip the ./ folder that's saved in the xml as the current directory
        if each.get('name') == ".":
            createDir(each, basedir = basedir)
        else:
            oNewDir = os.path.join(basedir, each.get('name'))
            if not os.path.isdir(oNewDir):
                os.mkdir(oNewDir)
                print "Created directory: " + oNewDir
            else:
                print oNewDir + " already exists"
            createDir(each, basedir = oNewDir)
    return

if results.writexml==True:
    dirToXML(dir, outfile)
elif results.xmltodir==True:
    xmlToDir(infile, prjname)
else:
    print "Please select either write mode or read/write mode"
