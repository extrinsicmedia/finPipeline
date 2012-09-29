import plogging as _plogging
import pymel.util as _util
import pymel.api as api
import inspect
import os
import startup
import sys
import time
import pymel.versions as versions

from pymel.util.arguments import *
from logging import *

class ApiEnum(tuple):
    def __repr__(self):
        pass
    
    
    def __str__(self):
        pass
    
    
    def pymelName(self):
        pass
    
    
    __dict__ = None


class ApiMelBridgeCache(startup.SubItemCache):
    CACHE_TYPES = None
    
    
    COMPRESSED = True
    
    
    DESC = 'the API-MEL bridge'
    
    
    NAME = 'mayaApiMelBridge'
    
    
    STORAGE_TYPES = None
    
    
    USE_VERSION = False


class ApiCache(startup.SubItemCache):
    def __init__(self):
        pass
    
    
    def addMayaType(self, mayaType, apiType=None, updateObj=None):
        """
        Add a type to the MayaTypes lists. Fill as many dictionary caches as we have info for.
        
            - mayaTypesToApiTypes
            - mayaTypesToApiEnums
            
        if updateObj is given, this instance will first be updated from it,
        before the mayaType is added.
        """
    
        pass
    
    
    def build(self):
        """
        Used to rebuild api cache, either by loading from a cache file, or rebuilding from scratch.
        """
    
        pass
    
    
    def extraDicts(self):
        pass
    
    
    def melBridgeContents(self):
        pass
    
    
    def read(self, raw=False):
        pass
    
    
    def rebuild(self):
        """
        Rebuild the api cache from scratch
        
        Unlike 'build', this does not attempt to load a cache file, but always
        rebuilds it by parsing the docs, etc.
        """
    
        pass
    
    
    def removeMayaType(self, mayaType, updateObj=None):
        """
        Remove a type from the MayaTypes lists.
        
            - mayaTypesToApiTypes
            - mayaTypesToApiEnums
            
        if updateObj is given, this instance will first be updated from it,
        before the mayaType is added.
        """
    
        pass
    
    
    COMPRESSED = True
    
    
    DESC = 'the API cache'
    
    
    EXTRA_GLOBAL_NAMES = None
    
    
    NAME = 'mayaApi'
    
    
    RESERVED_TYPES = None
    
    
    USE_VERSION = True

