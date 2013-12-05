#!/usr/bin/env python
''' sampler.py - Samples high and low pixel values and
returns values for each frame and entire framerange

Copyright (C) 2012 Miles Lauridsen

Based on BSD 2-Clause License http://opensource.org/licenses/BSD-2-Clause

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

import nuke
import time

def boundingBox(n):
    nbb = n.bbox()
    x = nbb.x()
    y = nbb.y()
    w = nbb.w() + nbb.x()
    h = nbb.h() + nbb.y()

    return x,y,w,h

def sampler(frame):
    maxVal = 0
    minVal = 1000000

    for n in nuke.selectedNodes():
        w,h,width,height = boundingBox(n)
        while w < width:
            while h < height:
                value = n.sample("red", w+0.5, h+0.5, frame=frame)
                h+=1
                if value != 0:
                    if value > maxVal:
                        maxVal = value
                    else:
                        if value < minVal:
                            minVal = value
            w += 1
            h = 0
    return minVal, maxVal

def framerangeSampler(first=int(nuke.root()['first_frame'].getValue()), \
        last=int(nuke.root()['last_frame'].getValue()) ):
    maxVal = 0
    minVal = 1000000

    for frame in range(first, last+1):
        minNew,maxNew=sampler(frame)
        print minNew, maxNew
        if minNew < mminVal:
            minVal = minNew
        else:
            pass
        if maxNew > maxVal:
            maxVal = maxNew
        else:
            pass

    return minVal, maxVal
