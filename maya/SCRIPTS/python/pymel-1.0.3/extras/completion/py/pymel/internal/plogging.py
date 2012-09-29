import ConfigParser
import logging
import maya
import os
import sys
import pymel.util as util

from maya.OpenMaya import *
from logging import *
from pymel.util.enum import *
from pymel.util.decoration import *

def getConfigFile():
    pass


def getLogConfigFile():
    pass


def getLogger(name):
    """
    a convenience function that allows any module to setup a logger by simply
    calling `getLogger(__name__)`.  If the module is a package, "__init__" will
    be stripped from the logger name
    """

    pass


def levelToName(level):
    pass


def nameToLevel(name):
    pass


def pymelLogFileConfig(fname, defaults=None, disable_existing_loggers=False):
    """
    Reads in a file to set up pymel's loggers.
    
    In most respects, this function behaves similarly to logging.config.fileConfig -
    consult it's help for details. In particular, the format of the config file
    must meet the same requirements - it must have the sections [loggers],
    [handlers], and [fomatters], and it must have an entry for [logger_root]...
    even if not options are set for it.
    
    It differs from logging.config.fileConfig in the following ways:
    
    1) It will not disable any pre-existing loggers which are not specified in
    the config file, unless disable_existing_loggers is set to True.
    
    2) Like logging.config.fileConfig, the default behavior for pre-existing
    handlers on any loggers whose settings are specified in the config file is
    to remove them; ie, ONLY the handlers explicitly given in the config will
    be on the configured logger.
    However, pymelLogFileConfig provides the ability to keep pre-exisiting
    handlers, by setting the 'remove_existing_handlers' option in the appropriate
    section to True.
    """

    pass


def timed(level=10):
    pass

BASIC_FORMAT = '%(levelname)s:%(name)s:%(message)s'

CRITICAL = 50

DEBUG = 10

ERROR = 40

FATAL = 50

INFO = 20

NOTSET = 0

PYMEL_CONF_ENV_VAR = 'PYMEL_CONF'

PYMEL_LOGLEVEL_ENV_VAR = 'PYMEL_LOGLEVEL'

WARN = 30

WARNING = 30

logLevels = None

n = 50

pymelLogger = None

root = None

rootLogger = None
