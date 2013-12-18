#!/usr/bin/env python
''' rvrc.py - RV Prefs and settings. Save as ~/.rvrc.py to use.
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

import rv.rvui
import rv.rvtypes
import rv.commands
import rv.extra_commands
import pymu
import os

## Set initial matte opacity as env var
os.environ["RV_MATTE_OPACITY"] = '0.33'


def initialize():
    print "initialize"
    rv.rvui.defineDefaultBindings()
    return rv.rvui.newStateObject();

def setup():

   
    def matte(event):
        matte = pymu.MuSymbol("rvui.setMatteValue")
        opacity = pymu.MuSymbol("rvui.setMatteOpacityValue")
        opacity (str(0.65))
        matte (str(2.40))

    def nomatte(event):
        matte = pymu.MuSymbol("rvui.setMatteValue")
        matte ("No Matte")

        ### Get the LUT and turn it on
        #rv.rvui.fileLUTState( jgkLut )
   
       
    def noLUT(event):
        sRGB = pymu.MuSymbol("rvui.toggleSRGBDisplay")
        sRGB (event)

    def opacityCheck():
            curVal = float(os.getenv("RV_MATTE_OPACITY") )
            if curVal < 1.0:
                os.environ["RV_MATTE_OPACITY"] = str( maxVal(curVal + 0.33))
                return curVal
            else:
                os.environ["RV_MATTE_OPACITY"] = "0"
                return 0
   
    def maxVal(value):
       if value > 1.0:
           return 0
       else:
           return value

       

    rv.commands.bind("default", "global", "key-down--M", matte, "")
    rv.commands.bind("default", "global", "key-down--N", nomatte, "")
    rv.commands.bind("default", "global", "key-down--B", noLUT, "")
   
    if os.getenv("RVRC_CONFIG") == '1':
        return
    else:
        pass
