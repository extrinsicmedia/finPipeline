#!/usr/bin/env python

# example of iterating through selected nodes
for n in nuke.selectedNodes():
    print n.name()

# same example but only using a specific node class
for n in nuke.selectedNodes("Camera2"):
    print n.name()

# get current script path
print nuke.root().name()

# get selected node class
print nuke.selectedNode().Class()

# looking through all nodes
for n in nuke.allNodes():
    if n.Class() == "Read":
        print n.name()

# select a node by name
nuke.toNode("Noise1")

# running tcl commands in python
nuke.tcl("value label")

# setting defaults in menu.py or init.py. http://docs.thefoundry.co.uk/nuke/63/pythondevguide/basics.html
nuke.knobDefault("Blur.size", "20")
nuke.knobDefault("Read.exr.compression", "2")

# Return an expression on a knob if it eists
if knob.hasExpression():
    origExpression = knob.toScript()

# List all knobs on a node
for i in nuke.selectedNodes().knobs():
    print i

# Set value on all Read nodes within a selected group
for n in nuke.selectedNodes():
    if n.Class() == "Group":
        for s in n.nodes():
            if s.Class() == "Read":
                s['postage_stamp'].setValue(True)

# Code for Tagging system
for n in nuke.allNodes():
    if "LUT_CORRECT" in n['label'].getValue():
        n['disable'].setValue(True)

for n in nuke.selectedNodes():
    n['label'].setValue("{PULSE}")
