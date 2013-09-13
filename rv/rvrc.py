#!/usr/bin/env python

## RV Prefs and settings
## Save as .rvrc.py in user directory

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

       

    rv.commands.bind("default", "global", "key-down--J", matte, "")
    rv.commands.bind("default", "global", "key-down--K", nomatte, "")
    rv.commands.bind("default", "global", "key-down--M", noLUT, "")
   
    if os.getenv("RVRC_CONFIG") == '1':
        return
    else:
        pass
