import maya.cmds as cmds
import inspect
import keyword
import pymel.mayautils as mayautils
import maya.mel as mm
import os
import plogging
import re
import startup
import pymel.util as util
import pymel.versions as versions

from logging import *

class CmdExamplesCache(startup.PymelCache):
    DESC = 'the list of Maya command examples'
    
    
    NAME = 'mayaCmdsExamples'
    
    
    USE_VERSION = True


class CmdDocsCache(startup.PymelCache):
    DESC = 'the Maya command documentation'
    
    
    NAME = 'mayaCmdsDocs'


class CmdCache(startup.SubItemCache):
    def build(self):
        pass
    
    
    def rebuild(self):
        """
        Build and save to disk the list of Maya Python commands and their arguments
        """
    
        pass
    
    
    CACHE_TYPES = None
    
    
    DESC = 'the list of Maya commands'
    
    
    NAME = 'mayaCmdsList'


class CmdProcessedExamplesCache(CmdExamplesCache):
    USE_VERSION = False

def cmdArgMakers(force=False):
    pass


def fixCodeExamples(style='maya', force=False):
    """
    cycle through all examples from the maya docs, replacing maya.cmds with pymel and inserting pymel output.
    
    NOTE: this can only be run from gui mode
    WARNING: back up your preferences before running
    
    TODO: auto backup and restore of maya prefs
    """

    pass


def getCallbackFlags(cmdInfo):
    """
    used parsed data and naming convention to determine which flags are callbacks
    """

    pass


def getCmdInfo(command, version='8.5', python=True):
    """
    Since many maya Python commands are builtins we can't get use getargspec on them.
    besides most use keyword args that we need the precise meaning of ( if they can be be used with
    edit or query flags, the shortnames of flags, etc) so we have to parse the maya docs
    """

    pass


def getCmdInfoBasic(command):
    pass


def getModuleCommandList(category, version=None):
    pass


def nodeCreationCmd(func, nodeType):
    pass


def testNodeCmd(funcName, cmdInfo, nodeCmd=False, verbose=False):
    pass

UI_COMMANDS = None

cmdlistOverrides = None

moduleCommandAdditions = None

moduleNameShortToLong = None

nodeTypeToNodeCommand = None

secondaryFlags = None
