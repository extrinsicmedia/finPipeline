"""
from pymel.api.plugins import Command
class testCmd(Command):
    def doIt(self, args):
        print "doIt..."

testCmd.register()
cmds.testCmd()
testCmd.deregister()
"""

import inspect
import maya
import maya.OpenMayaMPx as mpx
import sys

class Command(mpx.MPxCommand):
    def __init__(self):
        pass
    
    
    def creator(cls):
        pass
    
    
    def deregister(cls, object=None):
        """
        if using from within a plugin's initializePlugin or uninitializePlugin callback, pass along the
        MObject given to these functions
        """
    
        pass
    
    
    def register(cls, object=None):
        """
        by default the command will be registered to a dummy plugin provided by pymel.
        
        If you
        if using from within a plugin's initializePlugin or uninitializePlugin callback, pass along the
        MObject given to these functions
        """
    
        pass
    
    
    registeredCommands = None

def initializePlugin(mobject):
    """
    # allow this file to be loaded as its own dummy plugin
    # Initialize the script plug-in
    """

    pass


def uninitializePlugin(mobject):
    """
    # Uninitialize the script plug-in
    """

    pass

registeredCommands = None
