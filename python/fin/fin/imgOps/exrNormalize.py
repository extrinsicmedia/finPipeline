#!/usr/bin/env python

# EXR Normalize to jpg

import OpenEXR
import Imath
import Image
import array
import sys

def ConvertEXRToJPG(exrfile, jpgfile):
    File = OpenEXR.InputFile(exrfile)
    PixType = Imath.PixelType(Imath.PixelType.FLOAT)
    DW = File.header()['dataWindow']
    Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1)

    RedStr = File.channel('R', PixType)
    GreenStr = File.channel('G', PixType)
    BlueStr = File.channel('B', PixType)

    Red = array.array('f', RedStr)
    Green = array.array('f', GreenStr)
    Blue = array.array('f', BlueStr)

    for I in range(len(Red)):
        Red[I] = EncodeToSRGB(Red[I])

    for I in range(len(Green)):
        Green[I] = EncodeToSRGB(Green[I])

    for I in range(len(Blue)):
        Blue[I] = EncodeToSRGB(Blue[I])

    rgbf = [Image.fromstring("F", Size, Red.tostring())]
    rgbf.append(Image.fromstring("F", Size, Green.tostring()))
    rgbf.append(Image.fromstring("F", Size, Blue.tostring()))

    rgb8 = [im.convert("L") for im in rgbf]
    Image.merge("RGB", rgb8).save(jpgfile, "JPEG", quality=95)
    

def EncodeToSRGB(v):
    if (v <= 0.0031308):
        return (v * 12.92) * 255.0
    else:
        return (1.055*(v**(1.0/2.4))-0.055) * 255.0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: exr2jpg <exrfile> <jpgfile>"
    ConvertEXRToJPG(sys.argv[1], sys.argv[2])