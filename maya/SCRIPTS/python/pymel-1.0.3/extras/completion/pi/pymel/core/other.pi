"""
Functions which are not listed in the maya documentation, such as commands created by plugins,
as well as the name parsing classes `DependNodeName`, `DagNodeName`, and `AttributeName`.
"""

import pymel.internal.factories as _factories
import pymel.internal.pmcmds as cmds
import inspect
import re

class NameParser(unicode):
    def __getattr__(self, attr):
        """
        >>> NameParser('foo:bar').spangle
        AttributeName(u'foo:bar.spangle')
        """
    
        pass
    
    
    def __repr__(self):
        pass
    
    
    def addPrefix(self, prefix):
        """
        addPrefixToName
        """
    
        pass
    
    
    def attr(self, attr):
        """
        access to AttributeName of a node. returns an instance of the AttributeName class for the
        given AttributeName.
        
            >>> NameParser('foo:bar').attr('spangle')
            AttributeName(u'foo:bar.spangle')
        """
    
        pass
    
    
    def namespace(self):
        """
        Returns the namespace of the object with trailing colon included
        """
    
        pass
    
    
    def namespaceList(self):
        """
        Useful for cascading references.  Returns all of the namespaces of the calling object as a list
        """
    
        pass
    
    
    def stripGivenNamespace(self, namespace, partial=True):
        """
        Returns a new instance of the object with any occurrences of the given namespace removed.  The calling instance is unaffected.
        The given namespace may end with a ':', or not.
        If partial is True (the default), and the given namespace has parent namespaces (ie, 'one:two:three'),
        then any occurrences of any parent namespaces are also stripped - ie, 'one' and 'one:two' would
        also be stripped.  If it is false, only namespaces
        
            >>> NameParser('foo:bar:top|foo:middle|foo:bar:extra:guy.spangle').stripGivenNamespace('foo:bar')
            AttributeName(u'top|middle|extra:guy.spangle')
            
            >>> NameParser('foo:bar:top|foo:middle|foo:bar:extra:guy.spangle').stripGivenNamespace('foo:bar', partial=False)
            AttributeName(u'top|foo:middle|extra:guy.spangle')
        """
    
        pass
    
    
    def stripNamespace(self, levels=0):
        """
        Returns a new instance of the object with its namespace removed.  The calling instance is unaffected.
        The optional levels keyword specifies how many levels of cascading namespaces to strip, starting with the topmost (leftmost).
        The default is 0 which will remove all namespaces.
        
            >>> NameParser('foo:bar.spangle').stripNamespace()
            AttributeName(u'bar.spangle')
        """
    
        pass
    
    
    def swapNamespace(self, prefix):
        """
        Returns a new instance of the object with its current namespace replaced with the provided one.
        The calling instance is unaffected.
        """
    
        pass
    
    
    def __new__(cls, strObj):
        """
        Casts a string to a pymel class. Use this function if you are unsure which class is the right one to use
        for your object.
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None
    
    PARENT_SEP = '|'


class DependNodeName(NameParser):
    def exists(self, **kwargs):
        """
        objExists
        """
    
        pass
    
    
    def extractNum(self):
        """
        Return the trailing numbers of the node name. If no trailing numbers are found
        an error will be raised.
        """
    
        pass
    
    
    def nextName(self):
        """
        Increment the trailing number of the object by 1
        """
    
        pass
    
    
    def nextUniqueName(self):
        """
        Increment the trailing number of the object until a unique name is found
        
        If there is no trailing number, appends '1' to the name.
        Will always return a different name than the current name, even if the
            current name already does not exist.
        """
    
        pass
    
    
    def node(self):
        """
        for compatibility with AttributeName class
        """
    
        pass
    
    
    def prevName(self):
        """
        Decrement the trailing number of the object by 1
        """
    
        pass
    
    
    def stripNum(self):
        """
        Return the name of the node with trailing numbers stripped off. If no trailing numbers are found
        the name will be returned unchanged.
        """
    
        pass


class AttributeName(NameParser):
    def __call__(self, *args, **kwargs):
        """
        # Added the __call__ so to generate a more appropriate exception when a class method is not found
        """
    
        pass
    
    
    def __getitem__(self, item):
        pass
    
    
    def __init__(self, attrName):
        pass
    
    
    def add(self, **kwargs):
        pass
    
    
    def addAttr(self, **kwargs):
        pass
    
    
    def array(self):
        """
        Returns the array (multi) AttributeName of the current element
            >>> n = AttributeName('lambert1.groupNodes[0]')
            >>> n.array()
            AttributeName(u'lambert1.groupNodes')
        """
    
        pass
    
    
    def exists(self):
        pass
    
    
    def getParent(self, generations=1):
        """
        Returns the parent attribute
        
        Modifications:
            - added optional generations flag, which gives the number of levels up that you wish to go for the parent;
              ie:
                  >>> AttributeName("Cube1.multiComp[3].child.otherchild").getParent(2)
                  AttributeName(u'Cube1.multiComp[3]')
        
              Negative values will traverse from the top, not counting the initial node name:
        
                  >>> AttributeName("Cube1.multiComp[3].child.otherchild").getParent(-2)
                  AttributeName(u'Cube1.multiComp[3].child')
        
              A value of 0 will return the same node.
              The default value is 1.
        
              Since the original command returned None if there is no parent, to sync with this behavior, None will
              be returned if generations is out of bounds (no IndexError will be thrown).
        """
    
        pass
    
    
    def item(self, asSlice=False, asString=False):
        pass
    
    
    def lastPlugAttr(self):
        """
        >>> NameParser('foo:bar.spangle.banner').lastPlugAttr()
        u'banner'
        """
    
        pass
    
    
    def node(self):
        """
        plugNode
        
        >>> NameParser('foo:bar.spangle.banner').plugNode()
        DependNodeName(u'foo:bar')
        """
    
        pass
    
    
    def nodeName(self):
        """
        basename
        """
    
        pass
    
    
    def plugAttr(self):
        """
        plugAttr
        
        >>> NameParser('foo:bar.spangle.banner').plugAttr()
        u'spangle.banner'
        """
    
        pass
    
    
    def plugNode(self):
        """
        plugNode
        
        >>> NameParser('foo:bar.spangle.banner').plugNode()
        DependNodeName(u'foo:bar')
        """
    
        pass
    
    
    def set(self, *args, **kwargs):
        pass
    
    
    def setAttr(self, *args, **kwargs):
        pass
    
    
    attrItemReg = None


class DagNodeName(DependNodeName):
    def firstParent(self):
        """
        firstParentOf
        """
    
        pass
    
    
    def getParent(self, generations=1):
        """
        Returns the parent node
        
        Modifications:
            - added optional generations flag, which gives the number of levels up that you wish to go for the parent;
              ie:
                  >>> DagNodeName("NS1:TopLevel|Next|ns2:Third|Fourth").getParent(2)
                  DagNodeName(u'NS1:TopLevel|Next')
        
              Negative values will traverse from the top, not counting the initial node name:
        
                  >>> DagNodeName("NS1:TopLevel|Next|ns2:Third|Fourth").getParent(-3)
                  DagNodeName(u'NS1:TopLevel|Next|ns2:Third')
        
              A value of 0 will return the same node.
              The default value is 1.
        
              Since the original command returned None if there is no parent, to sync with this behavior, None will
              be returned if generations is out of bounds (no IndexError will be thrown).
        """
    
        pass
    
    
    def getRoot(self):
        """
        unlike the root command which determines the parent via string formatting, this
        command uses the listRelatives command
        """
    
        pass
    
    
    def nodeName(self):
        """
        basename
        """
    
        pass
    
    
    def root(self):
        """
        rootOf
        """
    
        pass

def TanimLayer(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.TanimLayer`
    """

    pass


def adskAsset(*args, **kwargs):
    """
    Flags:
      - assetID : a                    (unicode)       []
    
      - library : l                    (unicode)       []
    
      - resolved : r                   (bool)          []
    
    
    Derived from mel command `maya.cmds.adskAsset`
    """

    pass


def adskAssetLibrary(*args, **kwargs):
    """
    The adskAssetLibrary command is provided to give control over the loading of asset libraries through scripting. Any
    number of libraries may be specified by URIs.
    
    Flags:
      - unload : ul                    (bool)          [create]
          Use this flag to unload the specified library.  The libraries must be specified by name rather than by URI when using
          this option
    
      - unloadAll : ua                 (bool)          [create]
          Unload all loaded asset libraries                                         Flag can have multiple arguments, passed
          either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.adskAssetLibrary`
    """

    pass


def adskAssetList(*args, **kwargs):
    """
    The adskAssetList command is provides information for all material assets in the loaded Autodesk asset library.
    
    Flags:
      - infoType : it                  (unicode)       [create]
          Specifies what type of information about the assets is returned.  Value values are: assetID, uiNameFlag can have
          multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.adskAssetList`
    """

    pass


def adskAssetListUI(*args, **kwargs):
    """
    Flags:
      - commandSuffix : cms            (unicode)       []
    
      - materialLoaded : mld           (bool)          []
    
      - uiCommand : uiC                (unicode)       []
    
    
    Derived from mel command `maya.cmds.adskAssetListUI`
    """

    pass


def agFormatIn(*args, **kwargs):
    """
    Flags:
      - file : f                       (unicode)       []
    
      - name : n                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.agFormatIn`
    """

    pass


def agFormatOut(*args, **kwargs):
    """
    Flags:
      - file : f                       (unicode)       []
    
    
    Derived from mel command `maya.cmds.agFormatOut`
    """

    pass


def artAttr(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.artAttr`
    """

    pass


def artFluidAttr(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.artFluidAttr`
    """

    pass


def artSelect(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.artSelect`
    """

    pass


def artSetPaint(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.artSetPaint`
    """

    pass


def blend(*args, **kwargs):
    """
    Flags:
      - autoDirection : ad             (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - crvsInFirstRail : cfr          (int)           []
    
      - flipLeft : fl                  (bool)          []
    
      - flipRight : fr                 (bool)          []
    
      - leftParameter : lp             (float)         []
    
      - multipleKnots : mk             (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - polygon : po                   (int)           []
    
      - positionTolerance : pt         (float)         []
    
      - rightParameter : rp            (float)         []
    
      - tangentTolerance : tt          (float)         []
    
    
    Derived from mel command `maya.cmds.blend`
    """

    pass


def clearShear(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.clearShear`
    """

    pass


def copyNode(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.copyNode`
    """

    pass


def dagObjectHit(*args, **kwargs):
    """
    Flags:
      - cache : ch                     (bool)          []
    
      - menu : mn                      (unicode)       []
    
      - multiple : m                   (bool)          []
    
      - targetSize : ts                (int)           []
    
    
    Derived from mel command `maya.cmds.dagObjectHit`
    """

    pass


def dbtrace(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dbtrace`
    """

    pass


def debug(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.debug`
    """

    pass


def debugNamespace(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.debugNamespace`
    """

    pass


def debugVar(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.debugVar`
    """

    pass


def dgControl(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgControl`
    """

    pass


def dgPerformance(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgPerformance`
    """

    pass


def dgcontrol(*args, **kwargs):
    """
    Flags:
      - iomode : iom                   (bool)          []
    
    
    Derived from mel command `maya.cmds.dgcontrol`
    """

    pass


def dgdebug(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgdebug`
    """

    pass


def dgfilter(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgfilter`
    """

    pass


def dgfootprint(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgfootprint`
    """

    pass


def dgstats(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.dgstats`
    """

    pass


def directConnectPath(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.directConnectPath`
    """

    pass


def dispatchGenericCommand(*args, **kwargs):
    """
    generic command dispatch function used for API commands
    
    
    Derived from mel command `maya.cmds.dispatchGenericCommand`
    """

    pass


def dynTestData(*args, **kwargs):
    """
    Flags:
      - arrayAttrs : aa                (bool)          []
    
      - verbose : v                    (bool)          []
    
    
    Derived from mel command `maya.cmds.dynTestData`
    """

    pass


def evalContinue(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.evalContinue`
    """

    pass


def extendFluid(*args, **kwargs):
    """
    Flags:
      - endD : ed                      (int)           []
    
      - endH : eh                      (int)           []
    
      - endW : ew                      (int)           []
    
      - startD : sd                    (int)           []
    
      - startH : sh                    (int)           []
    
      - startW : sw                    (int)           []
    
    
    Derived from mel command `maya.cmds.extendFluid`
    """

    pass


def flagTest(*args, **kwargs):
    """
    Flags:
      - floatRange : fr                (floatRange)    []
    
      - indexRange : ir                (indexRange)    []
    
      - multiUse : mu                  (float, int, unicode) []
    
      - noReport : nr                  (bool)          []
    
      - optionalQueryArgsFlag : oqa    (float, int, unicode) []
    
      - pythonOptionalQueryArgsFlag : poq (float, int, unicode) []
    
      - pythonQueryArgsFlag : pq       (float, int, unicode) []
    
      - queryArgsFlag : qa             (float, int, unicode) []
    
      - simpleFlag : s                 (bool)          []
    
      - stringArrayFlag : saf          (string[...])   []
    
      - stringFlag : sf                (unicode)       []
    
      - timeRange : tr                 (timeRange)     []
    
      - tripleFloat : tf               (float, float, float) []
    
    
    Derived from mel command `maya.cmds.flagTest`
    """

    pass


def flushIdleQueue(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.flushIdleQueue`
    """

    pass


def flushThumbnailCache(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.flushThumbnailCache`
    """

    pass


def fontAttributes(*args, **kwargs):
    """
    Flags:
      - faceName : fc                  (unicode)       []
    
      - font : fn                      (unicode)       []
    
      - pitch : p                      (unicode)       []
    
      - size : sz                      (int)           []
    
      - style : st                     (unicode)       []
    
      - weight : wt                    (unicode)       []
    
    
    Derived from mel command `maya.cmds.fontAttributes`
    """

    pass


def groupParts(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.groupParts`
    """

    pass


def imageWindowEditor(*args, **kwargs):
    """
    Flags:
      - autoResize : ar                (bool)          []
    
      - changeCommand : cc             (unicode, unicode, unicode, unicode) []
    
      - clear : cl                     (int, int, float, float, float) []
    
      - control : ctl                  (bool)          []
    
      - defineTemplate : dt            (unicode)       []
    
      - displayImage : di              (int)           []
    
      - displayStyle : dst             (unicode)       []
    
      - docTag : dtg                   (unicode)       []
    
      - doubleBuffer : dbf             (bool)          []
    
      - drawAxis : da                  (bool)          []
    
      - exists : ex                    (bool)          []
    
      - filter : f                     (unicode)       []
    
      - forceMainConnection : fmc      (unicode)       []
    
      - frameImage : fi                (bool)          []
    
      - frameRegion : fr               (bool)          []
    
      - highlightConnection : hlc      (unicode)       []
    
      - loadImage : li                 (unicode)       []
    
      - lockMainConnection : lck       (bool)          []
    
      - mainListConnection : mlc       (unicode)       []
    
      - marquee : mq                   (float, float, float, float) []
    
      - nbImages : nim                 (bool)          []
    
      - panel : pnl                    (unicode)       []
    
      - parent : p                     (unicode)       []
    
      - realSize : rs                  (bool)          []
    
      - removeAllImages : ra           (bool)          []
    
      - removeImage : ri               (bool)          []
    
      - saveImage : si                 (bool)          []
    
      - scaleBlue : sb                 (float)         []
    
      - scaleGreen : sg                (float)         []
    
      - scaleRed : sr                  (float)         []
    
      - selectionConnection : slc      (unicode)       []
    
      - showRegion : srg               (int, int)      []
    
      - singleBuffer : sbf             (bool)          []
    
      - stateString : sts              (bool)          []
    
      - toggle : tgl                   (bool)          []
    
      - unParent : up                  (bool)          []
    
      - unlockMainConnection : ulk     (bool)          []
    
      - updateMainConnection : upd     (bool)          []
    
      - useTemplate : ut               (unicode)       []
    
      - writeImage : wi                (unicode)       []
    
    
    Derived from mel command `maya.cmds.imageWindowEditor`
    """

    pass


def interactionStyle(*args, **kwargs):
    """
    Flags:
      - style : s                      (unicode)       []
    
    
    Derived from mel command `maya.cmds.interactionStyle`
    """

    pass


def itemFilterAttrOld(*args, **kwargs):
    """
    Flags:
      - byName : bn                    (unicode)       []
    
      - byScript : bs                  (unicode)       []
    
      - defineTemplate : dt            (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - hasCurve : hc                  (bool)          []
    
      - hasExpression : he             (bool)          []
    
      - hidden : h                     (bool)          []
    
      - intersect : intersect          (unicode, unicode) []
    
      - keyable : k                    (bool)          []
    
      - negate : neg                   (bool)          []
    
      - parent : p                     (unicode)       []
    
      - readable : r                   (bool)          []
    
      - scaleRotateTranslate : srt     (bool)          []
    
      - secondScript : ss              (unicode)       []
    
      - text : t                       (unicode)       []
    
      - union : un                     (unicode, unicode) []
    
      - useTemplate : ut               (unicode)       []
    
      - writable : w                   (bool)          []
    
    
    Derived from mel command `maya.cmds.itemFilterAttrOld`
    """

    pass


def itemFilterOld(*args, **kwargs):
    """
    Flags:
      - byName : bn                    (unicode)       []
    
      - byScript : bs                  (unicode)       []
    
      - byType : bt                    (unicode)       []
    
      - clearByType : cbt              (bool)          []
    
      - defineTemplate : dt            (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - intersect : intersect          (unicode, unicode) []
    
      - negate : neg                   (bool)          []
    
      - parent : p                     (unicode)       []
    
      - secondScript : ss              (unicode)       []
    
      - text : t                       (unicode)       []
    
      - union : un                     (unicode, unicode) []
    
      - useTemplate : ut               (unicode)       []
    
    
    Derived from mel command `maya.cmds.itemFilterOld`
    """

    pass


def itemFilterRenderOld(*args, **kwargs):
    """
    Flags:
      - anyTextures : at               (bool)          []
    
      - defineTemplate : dt            (unicode)       []
    
      - exclusiveLights : exl          (bool)          []
    
      - exists : ex                    (bool)          []
    
      - lights : l                     (bool)          []
    
      - linkedLights : ll              (bool)          []
    
      - negate : neg                   (bool)          []
    
      - nonExclusiveLights : nxl       (bool)          []
    
      - nonIlluminatingLights : nil    (bool)          []
    
      - parent : p                     (unicode)       []
    
      - postProcess : pp               (bool)          []
    
      - renderUtilityNode : run        (bool)          []
    
      - shaders : s                    (bool)          []
    
      - text : t                       (unicode)       []
    
      - textures2d : t2d               (bool)          []
    
      - textures3d : t3d               (bool)          []
    
      - texturesProcedural : tp        (bool)          []
    
      - useTemplate : ut               (unicode)       []
    
    
    Derived from mel command `maya.cmds.itemFilterRenderOld`
    """

    pass


def itemFilterTypeOld(*args, **kwargs):
    """
    Flags:
      - defineTemplate : dt            (unicode)       []
    
      - exists : ex                    (bool)          []
    
      - text : t                       (unicode)       []
    
      - type : typ                     (bool)          []
    
      - useTemplate : ut               (unicode)       []
    
    
    Derived from mel command `maya.cmds.itemFilterTypeOld`
    """

    pass


def iterOnNurbs(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.iterOnNurbs`
    """

    pass


def journal(*args, **kwargs):
    """
    Flags:
      - comment : c                    (unicode)       []
    
      - flush : fl                     (bool)          []
    
      - highPrecision : hp             (bool)          []
    
      - state : st                     (bool)          []
    
    
    Derived from mel command `maya.cmds.journal`
    """

    pass


def licenseCheck(*args, **kwargs):
    """
    Flags:
      - mode : m                       (unicode)       []
    
      - type : typ                     (unicode)       []
    
    
    Derived from mel command `maya.cmds.licenseCheck`
    """

    pass


def meshIntersectTest(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.meshIntersectTest`
    """

    pass


def mouldMesh(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.mouldMesh`
    """

    pass


def mouldSrf(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.mouldSrf`
    """

    pass


def mouldSubdiv(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.mouldSubdiv`
    """

    pass


def movieCompressor(*args, **kwargs):
    """
    Flags:
      - hardwareOptions : ho           (bool)          []
    
      - softwareOptions : so           (bool)          []
    
    
    Derived from mel command `maya.cmds.movieCompressor`
    """

    pass


def myTestCmd(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.myTestCmd`
    """

    pass


def nop(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.nop`
    """

    pass


def nurbsCurveRebuildPref(*args, **kwargs):
    """
    Flags:
      - degree : d                     (int)           []
    
      - endKnots : end                 (int)           []
    
      - fitRebuild : fr                (int)           []
    
      - keepControlPoints : kcp        (bool)          []
    
      - keepEndPoints : kep            (bool)          []
    
      - keepRange : kr                 (int)           []
    
      - keepTangents : kt              (bool)          []
    
      - rebuildType : rt               (int)           []
    
      - smartSurfaceCurve : scr        (bool)          []
    
      - spans : s                      (int)           []
    
      - tolerance : tol                (float)         []
    
    
    Derived from mel command `maya.cmds.nurbsCurveRebuildPref`
    """

    pass


def objstats(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.objstats`
    """

    pass


def ogsdebug(*args, **kwargs):
    """
    Flags:
      - count : c                      (int)           []
    
      - debug : d                      (unicode)       []
    
      - timing : t                     (unicode)       []
    
      - verbose : v                    (bool)          []
    
    
    Derived from mel command `maya.cmds.ogsdebug`
    """

    pass


def paint3d(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.paint3d`
    """

    pass


def polyIterOnPoly(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.polyIterOnPoly`
    """

    pass


def polyPrimitiveMisc(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.polyPrimitiveMisc`
    """

    pass


def polySelectEditCtxDataCmd(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.polySelectEditCtxDataCmd`
    """

    pass


def polySelectSp(*args, **kwargs):
    """
    Flags:
      - loop : l                       (bool)          []
    
      - ring : r                       (bool)          []
    
    
    Derived from mel command `maya.cmds.polySelectSp`
    """

    pass


def polySetVertices(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.polySetVertices`
    """

    pass


def polySpinEdge(*args, **kwargs):
    """
    Flags:
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - offset : off                   (int)           []
    
    
    Derived from mel command `maya.cmds.polySpinEdge`
    """

    pass


def polyTestPop(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.polyTestPop`
    """

    pass


def polyToCurve(*args, **kwargs):
    """
    Flags:
      - addUnderTransform : aut        (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - degree : dg                    (int)           []
    
      - form : f                       (int)           []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
    
    Derived from mel command `maya.cmds.polyToCurve`
    """

    pass


def polyWarpImage(*args, **kwargs):
    """
    Flags:
      - background : bg                (int, int, int) []
    
      - bilinear : b                   (bool)          []
    
      - fileFormat : ff                (unicode)       []
    
      - inputName : inputName          (unicode)       []
    
      - inputUvSetName : iuv           (unicode)       []
    
      - noAlpha : na                   (bool)          []
    
      - outputName : on                (unicode)       []
    
      - outputUvSetName : ouv          (unicode)       []
    
      - overwrite : o                  (bool)          []
    
      - tiled : t                      (bool)          []
    
      - xResolution : xr               (int)           []
    
      - yResolution : yr               (int)           []
    
    
    Derived from mel command `maya.cmds.polyWarpImage`
    """

    pass


def psdConvSolidTxOptions(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.psdConvSolidTxOptions`
    """

    pass


def rampWidget(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.rampWidget`
    """

    pass


def rampWidgetAttrless(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.rampWidgetAttrless`
    """

    pass


def readPDC(*args, **kwargs):
    """
    Flags:
      - file : f                       (unicode)       []
    
      - test : t                       (bool)          []
    
    
    Derived from mel command `maya.cmds.readPDC`
    """

    pass


def repeatLast(*args, **kwargs):
    """
    Flags:
      - addCommand : ac                (unicode)       []
    
      - addCommandLabel : acl          (unicode)       []
    
      - commandList : cl               (int)           []
    
      - commandNameList : cnl          (int)           []
    
      - historyLimit : hl              (int)           []
    
      - item : i                       (int)           []
    
      - numberOfHistoryItems : nhi     (bool)          []
    
    
    Derived from mel command `maya.cmds.repeatLast`
    """

    pass


def selectKeyframe(*args, **kwargs):
    """
    Flags:
      - animation : an                 (unicode)       []
    
      - attribute : at                 (unicode)       []
    
      - controlPoints : cp             (bool)          []
    
      - float : f                      (floatRange)    []
    
      - hierarchy : hi                 (unicode)       []
    
      - includeUpperBound : iub        (bool)          []
    
      - index : index                  (indexRange)    []
    
      - selectionWindow : sel          (float, float, float, float) []
    
      - shape : s                      (bool)          []
    
      - time : t                       (timeRange)     []
    
    
    Derived from mel command `maya.cmds.selectKeyframe`
    """

    pass


def subdDisplayMode(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.subdDisplayMode`
    """

    pass


def subdToNurbs(*args, **kwargs):
    """
    Flags:
      - addUnderTransform : aut        (bool)          []
    
      - applyMatrixToResult : amr      (bool)          []
    
      - caching : cch                  (bool)          []
    
      - constructionHistory : ch       (bool)          []
    
      - name : n                       (unicode)       []
    
      - nodeState : nds                (int)           []
    
      - object : o                     (bool)          []
    
      - outputType : ot                (int)           []
    
    
    Derived from mel command `maya.cmds.subdToNurbs`
    """

    pass


def subgraph(*args, **kwargs):
    """
    Dynamic library stub function
    
    
    Derived from mel command `maya.cmds.subgraph`
    """

    pass


def testPa(*args, **kwargs):
    """
    Derived from mel command `maya.cmds.testPa`
    """

    pass


def testPassContribution(*args, **kwargs):
    """
    Flags:
      - renderLayer : rl               (unicode)       []
    
      - renderPass : rp                (unicode)       []
    
    
    Derived from mel command `maya.cmds.testPassContribution`
    """

    pass

