#!/bin/sh

# OCIO example converting from linear EXR to OCIO sRGB jpeg
ocioconvert test.0001.exr lnf test_lin2srgb.1001.jpg srgb8

# OCIO example converting from log DPX to OCIO sRGB jpeg
ocioconvert test.0001.dpx lgf test_log2srgb.1001.jpg srgb8

# OCIO example from linear EXR to standard sRGB (vd8) jpeg
ocioconvert test.0001.exr lnf test_lin2vd8.1001.jpg vd8

#OCIO example from linear EXR to custom sRGB display jpeg
ocioconvert test.0001.exr lnf test_lin2srgb.1001.jpg fuji3519
