==================================
Version 1.0.3
==================================

----------------------------------
Changes
----------------------------------

- UI classes that have 'with' statement support now set parent back to previous
  'with' object if there are nested with statements; if not in a nested with
  statement, resets parent back to UI element's parent (or more precisely, the
  first element that is not a rowGroupLayout element)
- ``with OptionMenuGrp()`` will set parent menu properly
- 'Unit' support for Quaternion objects is now removed (as it doesn't make
  any sense)
- can now pass in PyNode class objects to functions / methods that expect a
  mel node class name - ie:

     listRelatives(allDescendents=True, type=nt.Joint)

  is equivalent to:

     listRelatives(allDescendents=True, type='joint')
- other: NameParser(dagObj) now always gives a DagNodeName even if shortName has no |


----------------------------------
Non-Backward Compatible Changes
----------------------------------

- PyNode('*') - or any other non-unique name - now returns an error
  use ls('*') if you wish to return a list of possible nodes
- By default, the root pymel logger outputs to sys.__stdout__ now, instead of
  sys.stderr; can be overriden to another stream in sys (ie, stdout, stderr,
  __stderr__, __stdout__) by setting the MAYA_SHELL_LOGGER_STREAM environment
  variable
- tangentConstraint, poleVectorConstraint, and pointOnPolyConstraint commands
  now return a PyNode when creating, instead of a list with one item
- skinCluster command / node's methods / flags for querying deformerTools, 
  influence, weightedInfluence now return PyNodes, not strings
- Attribute.elements now returns an empty list instead of None
- general: Attribute.affects/affected return empty list when affects returns None
- setParent returns PyUI / None; menu(itemArray) returns [] for None
- general: make Attribute.elements() return empty list for None
- shape attribute lookup on all child shapes (like mel does)

----------------------------------
Additions
----------------------------------

- Shape.setParent automatically adds --shape flag
- nodetypes: added isVisible
- added MGlobal.display* methods to pymel.core.system namespace
- other: added NameParser.stripGivenNamespace()
- language: OptionVarList has more helpful error message when __setitem__ attempted
- nodetypes: getSiblings can now take kwargs
- Added MainProgressBar context manager
- Added isUsedAsColor method to Attribute class
- Added wrapper for listSets function
- Added method listSets to PyNode class
- Add a folderButtonGrp
- core.system: added Namespace.move
- core.system: added Namespace.listNodes
- mel2py: python mel command now translated to pymel.python (ie, maya.cmds.python)
- general: added Attribute.indexMatters
- language: added animStart/EndTime to Env
- system: add in a 'breadth'-first recursive search mode to iterReferences
- general: added ability to set enum Attributes with string values (issue 35)
- plogging: set logging level with PYMEL_LOGLEVEL env var
- Added isRenderable() method to object set.
- deprecate PyNode.__getitem__
- mayautils: executeDeferred now takes args, like maya.utils.executeDeferred

----------------------------------
Bugfixes
----------------------------------

- py2mel failing with functions that take \*args/\*\*kwargs
- eliminated / fixed various 'warning' messages on pymel startup
- MayaNodeError / MayaAttributeError not being raised when a node / attribute not found
- some maya cmds were not handling 'stubFunc' correctly
- renderLayer.listAdjustments() was not functioning
- MainProgressBar fixed
- language: OptionVarList __init__ no longer raises deprecation warning
- listSets() throws away non-existant 'defaultCreaseDataSet' that maya.cmds.listSets() returns
- fix for dealing with maya bug where constraint angle offsets always returned in radians (but set in degrees)
- fixes for incorrect formatting of error strings in some cases
- fixes for unloading of commands/nodetypes when plugins unloaded (and pymel.all was imported first)
- miscellaneous documentation fixes
- fix for mayautils.executeDeferred when invoked with args
- fix for Attribute.getAllParents()
- fix for aliased multi/compound attributes
- fix for Attribute.isSettable with multi/compound attributes
- fix for Attribute.exists with multi/compound attributes
- fix for Attribute.type with multi/compound attributes dynamic attributes
- fix for published container node attributes / aliases
- fixes for plugin callback failing when plugin has uncreate-able nodes
- fixes for multiple iterators of a mutli-attribute not being independent
- fix for MeshVertex.setColor
- fix for MeshVertex.isConnectedTo
- fix for MeshVertex.getColor
- fix for MeshEdge.isConnectedTo
- fix for MeshFace.isConnectedTo
- fix for plogging handling case where various env. variables exist, but are empty
- Fix for Layout.children() Layout.children() now returns empty list if layout has no kids intead of raising error.
- listConnections: fix so rotatePivot always Attribute (not component)
- uitypes: bugfixes to AETemplates.  corrected UITemplate to represent an existing uiTemplate if instantiated with the name of an existing template
- nodetypes: fixed a bug where Transform.setScalePivot was internally using MFnTransform.setScalePivotTranslation
- fixed a bug in pythonToMel where python booleans were not converted to integer. this caused the Mel class to not work properly with booleans.
- core.general: fix a bug with sets command where noWarnings was interpreted as a set flag, instead of a boolean flag
- Namespace: fix for getParent()
- general: various attr name fixes (stripping of [-1] indices, etc)
- nameparse: enable parsing of [-1] indices (for attributes)
- nodetypes: enable parsing of [-1] indices (for attributes)
- nodetypes: setParent to current parent no longer errors
- util.enum: fix for repr of EnumDict
- fixes for referenceQuery
- attr.exists() should return False if the node no longer exists
- datatypes: fixed bug to allow Point * FloatMatrix
- general: bugfix for Attribute.attrName
- utilitytypes: EquivalencePairs.get now correctly retrieves value=>key
- nodetypes: fixed setParent(world=1) bug
- uitypes: Fix issues with the popup and with support.
- pm.mel.command translation would fail with no-arg bool flags (like -q, -e)
- language: mel command translation makes no assumptions for unknown commands; None is translated to empty string, not 'None'
- bugfix for uiTemplate(exists=1)
- general: Attribute.elements() now correctly works with array and element plugs
- fix get/set rotation by using eulerRotation
- startup: changes to fix issues with maya -prompt and plugins loading pymel
- fix for TransformationMatrix.get/setRotation, removed Quaternion units
- datatypes: fixes for EulerRotation
- fix for ui heights for pymelControlPanel
- uitypes: bugfix for with statement parent setting on exit
- mesh: fixes to allow creating component objects for empty meshes (ie, createNode('mesh').vtx)
- mesh: made more num* functions work with empty meshes
- core.general: fix for move with no object
- datatypes: fix for EulerRotation comparison/len
- fix for menu('someOptionMenu')
- FileReference: initialize correctly from a path
- windows: bugfix - informBox wasn't using 'ok' kwarg
- plogging: bugfix for 182 - crash due to creating loggers as iterating over dict
- arrays: fix for dot/outer product error messages (issue 158)
- fix for 'no useName' and MfknSkinCluster.setBlendWeights warnings on startup
- Fixed language import in MainProgressBar
- fix for Issue 216: renderLayer.listAdjustments()
- docfix for issue 192
- fix for constraint angle offset query always being in radians
- nodetypes: fix for multi/compound alias attrs
- nodetypes: fixes for published container node attributes / aliases
- general: made attribute iterator independent
- general: fix for isSettable with multi/compound attributes
- general: fix so getAllParents doesn't return orig object
- general: fix for Attribute.exists with multi/compound attrs
- Attribute.type() now works with multi/compound, dynamic attrs
- fixes for mesh components

==================================
Version 1.0.2
==================================

----------------------------------
Changes
----------------------------------

- rolled back ``listConnections()`` change from 1.0.1

commands wrapped to return PyNodes
----------------------------------
- ``container()``

----------------------------------
Additions
----------------------------------

- added functions for converting strings to PyQt objects: ``toQtObject()``, ``toQtLayout()``, ``toQtControl()``, ``toQtMenuItem()``, ``toQtWindow()``
- added method for converting PyMEL UI objects to PyQt objects: ``UI.asQtObject()``

----------------------------------
Bugfixes
----------------------------------

- fixed a bug where ``nt.Conditions()`` created a script condition


==================================
Version 1.0.1
==================================

----------------------------------
Changes
----------------------------------

- ``listConnections``: when destination is shape, always returns shape (not transform)
- ``select([])`` only clears selection if mode is replace
- deprecated ``Attribute.firstParent()``

----------------------------------
Additions
----------------------------------

- ``mel2py``: now does packages/subpackages for recursed mel subdirectories
- added various dict-like methods to OptionVarDict
- added new EnumDict support which ``Attribute.getEnum`` returns
- added support to ``getAttr()`` / ``Attribute.get()`` for getting message attributes, which are returned as DependNodes
- added ``core.system.saveFile()``
- added ``pymel.versions.is64bit()``
- added new directory helpers to mayautils: ``getMayaAppDir()``, ``getUserPrefsDir()``, and ``getUserScriptsDir()``
- added ``DependNode.longName()``, ``DependNode.shortName()``, and ``DependNode.nodeName()`` for easy looping through mixed lists of DependNodes and DagNodes
- added ``FileInfo.__delitem__()``
- added ``DependNode.deleteAttr()``

----------------------------------
Bugfixes
----------------------------------

- unloading plugins no longer raises an error
- python AE templates were not being found. fixed.
- fixed a bug in api wrap, where ``MScriptUtil`` was not allocating space
- fixed a bug with ``Transform.setMatrix()``
- ``pymel.versions.installName()`` is more reliable on 64-bit systems, which were sometimes detecting the installName incorrectly
- ``Attribute('mytransform.scalePivot')`` now returns an the scalePivot attribute
- ``getAttr()`` / ``Attribute.get()`` bugfix with multi-attr
- ``nodetypes``: fixed bug 172 where nested selection sets were raising an error when getting members
- ``getPanel`` now always return panels
- ``uitypes``: all panel classes now properly inherit from Panel
- fixed some keywords that had been mistakenly refactored
- ``core.general``: fixed a bug where dependNodes were not returned when duplicated


==================================
Version 1.0.0
==================================

----------------------------------
Non-Backward Compatible Changes
----------------------------------

- pymel no longer has 'everything' in namespace - use ``pymel.all`` for this
- ``pymel.core.nodetypes`` now moved to it's own namespace
- ``pymel.mayahook.Version`` functionality moved to ``pymel.versions`` module. to compare versions, instead of Version class, use, for example, ``pymel.versions.current()`` >= ``pymel.versions.v2008``
- ``pymel.mayahook.mayautils.getMayaVersion()`` / ``getMayaVersion(extension=True)`` replaced with ``pymel.versions.installName()``
- ``pymel.mayahook.mayautils.getMayaVersion(extension=True)`` replaced with ``pymel.versions.shortName()``
- removed 0_7_compatibility_mode

- removed deprecated and inapplicable string methods from , base of all PyNodes: 

- removed Smart Layout Creator in favor of 'with' statement support
- ``DagNode.getParent()`` no longer accepts keyword arguments
- Renamed ``UI`` base class to ``PyUI``
- ``sceneName()`` now returns a Path class for an empty string when the scene is untitled. this makes it conform more to ``cmds.file(q=1, sceneName=1)``
- replaced listNamespace with listNamespace_new from 0.9 line

removed deprecated methods
--------------------------
- ``Attribute``: ``__setattr__``, ``size``
- ``Camera``: ``getFov``, ``setFov``, ``getFilmAspect``
- ``Mesh``: ``vertexCount``, ``edgeCount``, ``faceCount``, ``uvcoordCount``, ``triangleCount``
- ``SelectSet``: ``issubset``, ``issuperset``, ``update``
- Mesh components: ``toEdges``, ``toFaces``, ``toVertices``
- ``ProxiUnicode``: ``__contains__,  __len__, __mod__, __rmod__, __mul__, __rmod__, __rmul__, expandtabs, translate, decode, encode, splitlines, capitalize, swapcase, title, isalnum, isalpha, isdigit, isspace, istitle, zfill``

----------------------------------
Features
----------------------------------

- added support for creation of class-based python Attribute Editor templates, using ``ui.AETemplate``
- added 'with statement' compatibility to UI Layout and Menu classes
- added the ability to generate completion files for IDEs like Wing, Eclipse, and Komodo

----------------------------------
Tools
----------------------------------

- ``ipymel``: added colorization to dag command
- ``py2mel``: now works with lambdas and methods.  new option to provide a list or dictionary of mel types.
- re-added missing scriptEditor files
- added upgradeScripts, a tool for converting 0.9 scripts to be 1.0 compatible

----------------------------------
Changes
----------------------------------

- moved functions for working with the shell into ``util.shell``
- split out ui classes from ``core.windows`` into ``core.uitypes`` for lazy loading
- for versions >= 2009, use open/close undo chunks instead of mel hack to ensure that an entire callback can be undone in one go
- improved ``lsUI()``
- moved component types out of nodetypes and into general
- ``__repr__`` for nodetypes, uitypes, and datatypes reflect their location so as not to cause confusion.  using short module names nt, ui, and dt.
- caches are now compressed for speed
- allow setting ``pymel.conf`` location via environment variable PYMEL_CONF
- ``DagNode.getBoundingBox()`` now allows you to specify space
- ensured that the 'name' flag for surface and curve operates on shape as well
- changes to allow ``myCube.vtx[1,3,5]``
- commands wrapped by pmcmds that raise a standard TypeError for a non-existent object will now raise a MayaObjectError
- simplified getParent code on Attribute and DagNode to improve function signatures.
- fixed a bug with ``ls(editable=1)``
- fixed a bug with ObjectSets containing DagNodes
- callbacks: extra debug information is printed in tracebacks

commands wrapped to return PyNodes
----------------------------------
- ``skinCluster(q=1, geometry=1)``
- ``addAttr(q=1, geometry=1)``
- ``addDynamic()``
- ``addPP()``
- ``constraint()``
- ``animLayer()``
- ``annnotate()``
- ``arclen()``
- ``art3dPaintCtx()``
- ``artAttrCtx()``
- ``modelEditor(q=1,camera=1)``
- ``dimensionShape()``

----------------------------------
Additions
----------------------------------

- added ``TwoWayDict``/``EquivalencePair`` to ``utilitytypes``
- added ``preorder()``, ``postorder()``, and``breadth()`` functions in ``util.arguments``, which have more intuitive arguments
- added new ``Layout`` class that all layouts inherit from
- added ``UITemplate`` class
- added usable ``__iter__`` to workspace dict / file dict objects
- added two tier setup scripts for maya (user/site) just like with python. This new ``siteSetup.py`` is intended for studio setup of maya and reserved ``userSetup.py`` for user level scripts.
- added a partial replacement maya package with a logger with a shell and gui handler qne changed plogging to use the new default maya logger
- added ``setAttr``/``getAttr`` support for all numeric datatypes, along with tests
- added ``Transform.getShapes()`` for returning a list of shapes
- added ``FileReference`` comparison operators
- added ``DependNode.longName(stripNamespace=False,level=0)``
- added ``SkinCluster.setWeights()``
- added ``AnimCurve.addKeys()``
- added regex flag to ls command
- added ``FileInfo.get()``
- added ``util.common.subpackages()`` function for walking package modules
- added ``util.conditions.Condition`` class for creating object-oriented condition testing
- ``pymel.conf``: added a fileLogger
- added ``Path.canonicalpath()`` and ``Path.samepath()``
- mel2py: added command-line flags, ability to recurse

added support for attribute aliases
-----------------------------------
- ``DependNode.attr()`` now casts aliases to Attributes properly (PyNode already does)
- added ``DependNode.listAliases()``
- added 'alias' keyword to ``DependNode.listAttr()``
- added ``Attribute.setAlias()``, ``Attribute.getAlias()``

----------------------------------
Bugfixes
----------------------------------

- fixed instantiation of PyNode from MPlug instance
- fixed a bug where Maya version was incorrectly detected when Maya was installed to a custom location 
- fixed bug where wrap of function which took multiple refs all pointed to same ``MScriptUtil``
- fixed wrapping of unsigned ptr api types
- fixed negative comp indices
- ``mel2py``: bugfix with ``mel2pyStr()``


==================================
Version 0.9.2
==================================

----------------------------------
Changes and Additions
----------------------------------

- added support for 2010 and python 2.6
- added basic support for all component types
- added a 'removeNamespace' flag to ``FileReference.importContents()``
- added support for open-ended time ranges for command like keyframes (Issue 82)
- enhanced ``keyframe`` function: if both valueChange and timeChange are queried, the result will be a list of (time,value) pairs
- added ability to pass a list of types to ``ls`` 'type' argument, as you can with ``listRelatives``
- added checkLocalArray and checkOtherArray arguments to ``Attribute.isConnectedTo`` which will cause the function to also test mulit/array elements
- improved ``core.language.pythonToMel()`` reliability on lists
- improved custom virtual class workflow
- added functionality to ``pymel.tools.py2mel`` for dynamically creating MEL commands based on python functions/classes
- added a new module ``pymel.api.plugins`` for working with api plugins in a more reasonable and automated fashion
- updated eclipse integration documentation

easy_install improvements
-------------------------
- setup now copies over a readline library for 2010 OSX using ``readline.so`` from toxik which is more compatible
- changed ipymel to be part of the default install instead of an extra package
- fixed interpreter path of ipymel and other executable scripts on OSX
- setup now detects and fixes invalid python installations on Linux which previously caused ``distutils`` and thus ``setup.py`` to fail


----------------------------------
Bugfixes
----------------------------------

- ``importFile()``, ``createReference()``, ``loadReference()``, and ``openFile()`` now return PyNodes when passed returnNewNodes flag (Issue 85)
- fixed rare bug with Vista where ``platform.system`` was failing during startup (Issue 87)
- fixed a bug with plugin loading to intelligently handle when callback does not get a name
- fixed ``optionMenu`` and ``optionMenuGrp`` to return empty lists instead of None
- restored ``core.other.AttributeName.exists()`` method
- fixed a bug in 0.7_compatibility_mode
- fixed minor bug in ``listRelatives()``
- fixed a bug where curve command was returning a string instead of a PyNode (Issue 96)


==================================
Version 0.9.1
==================================

----------------------------------
Changes and Additions
----------------------------------

- new feature:  virtual subclasses.  allows the user to create their own subclasses which are returned by ``PyNode``
- added ``v2009sp1`` and ``v2009sp1a`` to ``Version``
- changed ``MelGlobals.__getitem__`` to raise a KeyError on missing global, instead of a typeError
- ``util.path`` now supports regular expression filtering in addition to globs.  
- moved ``moduleDir()`` from ``util`` to ``mayahook`` since it is explicitly for pymel.  
- ensured that all default plugins are loaded when creating the api cache so that we can avoid calculating those each time the plugins are loaded
- added a new `errors` flag to recurseMayaScriptPath for controlling how to handle directory walking errors: warn or ignore
- moved ``pwarnings`` to ensure that ``pymel.util`` is completely separated from maya
- adding new sphinx documentation. modifying source docstrings where necessary.
- setParent now allows ``None`` arg to specify world parent
- adopted a standard setuptools-compliant package layout, with pymel as a subdirectory of the top level
- forced line numbers on for ``Mel.eval``
- changed ipymel to use $MAYA_LOCATION to find mayapy instead of /usr/bin/env
- changed datatypes examples to demonstrate the necessity to include a namespace
- added ``groupname``, ``get_groupname``, and ``chgrp`` to ``Path`` class for dealing with unix groups as strings instead of as gid's
- added alias ``path.Path`` for ``path.path`` so as to follow PEP8
- added a new option to ``pymel.conf`` to allow disabling of mel initialization in standalone mode.
- added ability to set logger verbosity using PYMEL_LOGLEVEL environment variable.  great for quick testing.

----------------------------------
Bugfixes
----------------------------------

- fixed a bug in ``undoInfo()``
- fixed a bug that was breaking ``mel2py``
- fixed a bug with logging that was locking it to INFO level.  INFO is now the default, but it can be properly changed in ``pymel.conf``
- fixed input casting of ``datatypes.Time`` 
- bug fixes in error handling within path class
- fixed issue 65: ``DependencyNode.listAttr()`` broken
- made sure ``NameParse`` objects are stringified before fed to ``MFnDependencyNode.findPlug()``
- added a few more reserved types so as to avoid creating them, which can lead to crashes on some setups
- fixed issue 66 where nodes could be created twice when using PEP8 style class instantiation: ``pm.Locator``
- ``path.walk*`` methods now properly prune all directories below those that do not match the supplied patterns
- maya bug workaround: changed pluginLoaded callback to API-based for 2009 and later
- fixed bug in ``hasAttr()``
- removed bug in ``arrays.dot`` where incorrect duplicate definition was taking precedence
- fixed bug in ``PyNode.__ne__()`` when comparing DagNodes to DependNodes
- fixed Issue 72: cannot select lists of components
- fixed bug with startup on windows (backslashes not escaped)
- fix for ``Component('pCube1.vtx[3]')``
- fix for nurbsCurveCV('nurbsCircle1') failing
- pythonToMel and Mel now properly convert ``datatypes.Vectors`` to mel vectors ( <<0,0,0>> ). ``MelGlobals`` now returns ``datatypes.Vectors``
- fixed bug with ``duplicate(addShape=1)``
- fixed a bug where selectionSets can't be selected
- fixed a bug with ``sets()`` when it returns lists
- fixed issue 76, where non-unique joint names were returned by ``pymel.joint`` and thus were unsuccessfully cast to ``nodetypes.Joint``
- fixed issue 80, regading incorrect association of ``nodetypes.File`` with ``cmds.file.`` 
- fixed a bug in ``connectAttr()`` that was preventing connection errors from being raised when the force flag was used






