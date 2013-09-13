#!/usr/bin/env python
import nuke
import time

def check_bb(n):
    nbb = n.bbox()
    x = nbb.x()
    y = nbb.y()
    w = nbb.w() + nbb.x()
    h = nbb.h() + nbb.y()

    return x,y,w,h

def sampler(frame):
    maxVal = 0
    minVal = 1000000

    print frame

    for n in nuke.selectedNodes():
        w,h,width,height = check_bb(n)
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
