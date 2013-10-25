#!/usr/bin/env python

for n in nuke.allNodes(recurseGroups=True):
    for knob in n.knobs():
        if n[knob].hasExpression():
            origExpression = n[knob].toScript()
            if "$gui" in origExpression:
                print n.name()
