#! /usr/local/bin/python

"""

Created from the ansi c example included with ply, which is based on the grammar in K&R, 2nd Ed.

"""



import sys, os, re, os.path, tempfile, string
import mellex

try:
    from pymel.util.external.ply import *
    import pymel.util.external.ply.lex
except ImportError:
    from ply import *
    import ply.lex

from pymel.util import unescape
from pymel.util.utilitytypes import TwoWayDict
import pymel
import pymel.util as util
import pymel.internal.factories as factories
import melscan

try:
    from pymel.core import *
except ImportError:
    print "maya.cmds module cannot be found. be sure to run this script through maya and not from the command line. Continuing, but without command support"

#mutableStr = proxyClass(str, 'mutableStr')

class Token(str):
    def __new__(cls, val, type, lineno=None, **kwargs):
        self=str.__new__(cls,val)
        self.type = type
        self.lineno = lineno
        self.array = False
        self.__dict__.update( kwargs )
        return self
    def __getslice__(self, start, end):
        return Token( str.__getslice__(self, start, end), self.type, self.__dict__ )
    def __add__(self, other ):
        newdict = self.__dict__
        try:
            newdict.update( other.__dict__ )
        except: pass
        return Token( str.__add__( self, other ), **newdict  )


# commands which should not be brought into main namespace
filteredCmds = ['file','filter','help','quit','sets','move','scale','rotate']
builtin_module = __import__('__main__').__builtins__
pythonReservedWords = ['and', 'del', 'from', 'not', 'while', 'as', 'elif', 'global', 'or',
                       'with', 'assert', 'else', 'if', 'pass', 'yield', 'break', 'except',
                       'import', 'print', 'class', 'exec', 'in', 'raise', 'continue',
                       'finally', 'is', 'return', 'def', 'for', 'lambda', 'try']

reserved= set( dir(builtin_module) )
reserved.update( pythonReservedWords )

def format_substring(x, t):
    """convert:
            substring( var, 2, (len(var)) )
        to:
            var[1:]

        or:
            substring( var, 2, var2 )
        to:
            var[1:var2]

        or:
            substring( var, 3, var2 )
        to:
            var[1:var2]
            """
    def makeSlice( var, arg, offset=0):
        if arg.startswith('(') and arg.endswith(')'):
            arg = arg[1:-1]
        try:
            return str( int(arg)+offset )
        except ValueError:
            m = re.match( '\(*\s*len\s*\(\s*' + var + '\s*\)\s*\)*(.*)', arg )
            if m:
                return m.group(1).replace(' ', '')
                #return m.group(1)

            else:
                res = str(arg)
                if offset != 0:
                    res = res + str(offset)
                return res

    start = makeSlice(x[0], x[1], -1)
    end = makeSlice(x[0], x[2])

    return '%s[%s:%s]' % (x[0], start, end )

def format_tokenize(x,t):
    if len(x) > 2:
        return Token( '%s=%s.split(%s)' % (x[2],x[0],x[1]), 'string', tokenize=x[2] )
    else:
        return Token( '%s=%s.split()' % (x[1],x[0]), 'string', tokenize=x[1] )

def format_tokenize_size( tokenized, sizeVar ):
    """tokenize fix:
    tokenize passes a buffer by reference, and returns a size.
    we must return a list, and compute the size as a second operation::

        int $size = `tokenize "foo bar", $buffer, " "`;

        buffer = "foo bar".split(' ')
        size = len(buffer)

    """
    buf = tokenized.__dict__.pop( 'tokenize' )
    return tokenized + '\n' + sizeVar + " = len(%s)\n" % buf

def format_fread(x, t):
    formatStr = {
         'string': "%s",
        'float'    : "%f",
        'int'    : "%d",
        'vector': "%f %f %f"
    }[x[1].type]
    return "fscanf(%s,'%s')" % (x[0], formatStr)

def format_fopen(x, t):
    try:
        mode = x[1]
    except IndexError:
        mode = "'w'"
    return 'open(%s,%s)' % (x[0], mode)



def format_source(x, t):
    script = eval(x[0])
    name = os.path.splitext( os.path.basename(script) )[0]
    #print "formatting source", name
    moduleName = _melObj_to_pyModule( name )
    if moduleName:
        if moduleName not in t.lexer.imported_modules:
            t.lexer.imported_modules.add(moduleName)
        return ''
    else:
        return '%smel.source(%s)' % (t.lexer.pymel_namespace, x[0] )

# dictionary of functions used to remap procedures to python commands
proc_remap = {

        # strings
        #'capitalizeString'         : ('string', lambda x, t: '%s.capitalize()'     % (x[0]) ), # not equiv
        'capitalizeString'         : ('string', lambda x, t: '%sutil.capitalize(%s)'     % (t.lexer.pymel_namespace,x[0]) ),
        'strip'                 : ('string', lambda x, t: '%s.strip()'         % (x[0]) ),
        'appendStringArray'     : ( None ,   lambda x, t: '%s += %s[:%s]'         % (x[0],x[1],x[2]) ),
        'stringArrayToString'     : ('string', lambda x, t: '%s.join(%s)'         % (x[1],x[0]) ),
        'stringArrayCatenate'    : ('string', lambda x, t: '%s + %s'             % (x[0],x[1]) ),
        'stringArrayContains'    : ('int',    lambda x, t: '%s in %s'             % (x[0],x[1]) ),
        'stringArrayCount'        : ('int',    lambda x, t: '%s.count(%s)'        % (x[1],x[0]) ),
        'stringArrayInsertAtIndex'    : ( None, lambda x, t: '%s.insert(%s,%s)'        % (x[1],x[0],x[2]) ),
        'stringArrayRemove'        : ('string[]', lambda x, t: '[x for x in %s if x not in %s]'    % (x[1],x[0]) ),
        'stringArrayRemoveAtIndex'    : ('string[]', lambda x, t: '%s.pop(%s)'        % (x[1],x[0]) ),
        #'stringArrayRemove'        : lambda x, t: 'filter( lambda x: x not in %s, %s )' % (x[0],x[1]) ),
        'stringToStringArray'    : ('string[]', lambda x, t: '%s.split(%s)'         % (x[0],x[1]) ),
        'startsWith'            : ('int',    lambda x, t: '%s.startswith(%s)'     % (x[0],x[1]) ),
        'endsWith'                : ('int',    lambda x, t: '%s.endswith(%s)'     % (x[0],x[1]) ),
        'tolower'                : ('string', lambda x, t: '%s.lower()'         % (x[0]) ),
        'toupper'                : ('string', lambda x, t: '%s.upper()'         % (x[0]) ),
        'tokenize'                : ('string[]', format_tokenize ),
        'substring'                : ('string', format_substring ),
        'substitute'            : ('string', lambda x, t: '%s.replace(%s,%s)'         % (x[1],x[0],x[2]) ),

        # misc. keywords
        'size'                     : ('int',    lambda x, t: 'len(%s)'             % (', '.join(x)) ),
        'print'                    : ( None ,   lambda x, t: 'print %s'             % (x[0]) ),
        'clear'                    : ( None ,   lambda x, t: '%s=[]'                 % (x[0]) ),
        'eval'                     : ( None ,   lambda x, t: '%smel.eval(%s)'     % (t.lexer.pymel_namespace, x[0]) ),
        'python'                   : ( None ,   lambda x, t: '%spython(%s)'     % (t.lexer.pymel_namespace, x[0]) ),
        'sort'                    : ( None ,   lambda x, t: 'sorted(%s)'            % (x[0]) ),
        'source'                : ( None ,      format_source ),
        # error handling
        'catch'                    : ( 'int' ,   lambda x, t: '%scatch( lambda: %s )' % (t.lexer.pymel_namespace,x[0]) ),
        'catchQuiet'            : ( 'int' ,   lambda x, t: '%scatch( lambda: %s )' % (t.lexer.pymel_namespace,x[0]) ),

        # system

        # TODO: check that new version of system works...
        # 'system'                : ( 'string' ,   lambda x, t: ( 'commands.getoutput( %s )'     % (x[0]), t.lexer.imported_modules.add('commands') )[0] ),  # commands.getoutput doesn't work in windows
        'system'                : ( 'string' ,   lambda x, t: '%sinternal.shellOutput(%s, convertNewlines=False, stripTrailingNewline=False)'     % (t.lexer.pymel_namespace,x[0]) ),
        # TODO: create our own version of exec, as the return value of popen2 is NOT the same as exec
        'exec'                    : ( None ,   lambda x, t: ( 'os.popen2( %s )'     % (x[0]), t.lexer.imported_modules.add('os') )[0] ),
        'getenv'                : ( 'string', lambda x, t: ( 'os.environ[ %s ]'     % (x[0]), t.lexer.imported_modules.add('os') )[0] ),
        # TODO : this differs from mel equiv bc it does not return a value
        'putenv'                : ( None, lambda x, t: ( 'os.environ[ %s ] = %s'     % (x[0], x[1]), t.lexer.imported_modules.add('os') )[0] ),

        # math
        'deg_to_rad'            : ( 'float', lambda x, t: 'radians( %s )'     % (x[0]) ),
        'rad_to_deg'            : ( 'float', lambda x, t: 'degrees( %s )'     % (x[0]) ),

        # file i/o
        'fopen'                    : ('int',    format_fopen ),
        'fprint'                : ( None ,   lambda x, t: '%s.write(%s)' % (x[0], x[1]) ),
        'fclose'                : ( None ,   lambda x, t: '%s.close()' % (x[0]) ),
        'fflush'                : ( None ,   lambda x, t: '%s.flush()' % (x[0]) ),
        'fgetline'                : ( 'string' ,   lambda x, t: '%s.readline()' % (x[0]) ),
        'frewind'                : ( None ,   lambda x, t: '%s.seek(0)' % (x[0]) ),
        'fgetword'                : ( 'string' ,   lambda x, t: "%sfscanf(%s,'%%s')" % (t.lexer.pymel_namespace,x[0]) ),
        'feof'                    : ( 'int'    ,   lambda x, t: '%sfeof(%s)' % (t.lexer.pymel_namespace,x[0]) ),
        'fread'                    : ( 'string' ,   format_fread ),


        #'filetest'                : lambda x, t: (  (  t.lexer.imported_modules.add('os'),  # add os module for access()
        #                                        {     '-r' : "Path(%(path)s).access(os.R_OK)",
        #                                            '-l' : "Path(%(path)s).islink()",
        #                                            '-w' : "Path(%(path)s).access(os.W_OK)",
        #                                            '-x' : "Path(%(path)s).access(os.X_OK)",
        #                                            '-f' : "Path(%(path)s).isfile()",
        #                                            '-d' : "Path(%(path)s).isdir()",
        #                                            '-h' : "Path(%(path)s).islink()",
        #                                            '-f' : "Path(%(path)s).exists() and Path(%(path)s).getsize()",
        #                                            '-L' : "Path(%(path)s).islink()",
        #                                            }[ x[0] ] % { 'path' :x[1] })
        #                                        )[1],

        'filetest'                : ('int',    lambda x, t: (  (  t.lexer.imported_modules.update( ['os', 'os.path'] ),  # add os module for access()
                                                {     '-r' : "os.access( %(path)s, os.R_OK)",
                                                    '-l' : "os.path.islink( %(path)s )",
                                                    '-w' : "os.access( %(path)s, os.W_OK)",
                                                    '-x' : "os.access( %(path)s, os.X_OK)",
                                                    '-f' : "os.path.isfile( %(path)s )",
                                                    '-d' : "os.path.isdir( %(path)s )",
                                                    '-h' : "os.path.islink( %(path)s )",
                                                    '-f' : "os.path.exists( %(path)s ) and os.path.getsize( %(path)s )",
                                                    '-L' : "os.path.islink( %(path)s )",
                                                    }[ x[0] ] % { 'path' :x[1] } )
                                                )[1] ),

        #'sysFile'                : lambda x, t: {     '-delete'    : "Path(%(path)s).remove()",
        #                                            '-del'        : "Path(%(path)s).remove()",
        #                                            '-rename'    : "Path(%(path)s).move(%(param)s)",
        #                                            '-ren'        : "Path(%(path)s).move(%(param)s)",
        #                                            '-move'        : "Path(%(path)s).move(%(param)s)",
        #                                            '-mov'        : "Path(%(path)s).move(%(param)s)",
        #                                            '-copy'        : "Path(%(path)s).copy(%(param)s)",
        #                                            '-cp'        : "Path(%(path)s).copy(%(param)s)",
        #                                            '-makeDir'    : "Path(%(path)s).mkdir()",
        #                                            '-md'         : "Path(%(path)s).mkdir()",
        #                                            '-removeEmptyDir' : "Path(%(path)s).removedirs()",
        #                                            '-red'         : "Path(%(path)s).removedirs()"
        #                                            }[ x[0] ] % { 'path' :x[-1], 'param':x[-2] }



        'sysFile'                : ('int',    lambda x, t: (  ( t.lexer.imported_modules.update( ['os', 'shutil'] ),
                                                {    '-delete'    : "os.remove( %(path)s )",
                                                    '-del'        : "os.remove( %(path)s )",
                                                    '-rename'    : "os.rename( %(path)s, %(param)s )",
                                                    '-ren'        : "os.rename( %(path)s, %(param)s )",
                                                    '-move'        : "os.rename( %(path)s, %(param)s )",
                                                    '-mov'        : "os.rename( %(path)s, %(param)s )",
                                                    '-copy'        : "shutil.copy( %(path)s, %(param)s )",
                                                    '-cp'        : "shutil.copy( %(path)s, %(param)s )",
                                                    '-makeDir'    : "os.mkdir( %(path)s )",
                                                    '-md'         : "os.mkdir( %(path)s ) ",
                                                    '-removeEmptyDir' : "os.rmdir( %(path)s )",
                                                    '-red'         : "os.rmdir( %(path)s )",
                                                    }[ x[0] ] % { 'path' :x[-1], 'param':x[-2] } )
                                                )[1] )
}

#: mel commands which were not ported to python, but which have flags that need to be translated
melCmdFlagList = {
             'error'   : { 'flags': {'showLineNumber': { 'longname': 'showLineNumber', 'numArgs': 1, 'shortname': 'sl'} } },
             'warning' : { 'flags': {'showLineNumber': { 'longname': 'showLineNumber', 'numArgs': 1, 'shortname': 'sl'} } },
             'trace'   : { 'flags': {'showLineNumber': { 'longname': 'showLineNumber', 'numArgs': 1, 'shortname': 'sl'} } }
             }

#: mel commands which were not ported to python; if we find one of these in pymel, we'll assume it's a replacement
melCmdList = ['abs', 'angle', 'ceil', 'chdir', 'clamp', 'clear', 'constrainValue', 'cos', 'cross', 'deg_to_rad', 'delrandstr', 'dot', 'env', 'erf', 'error', 'exec', 'exists', 'exp', 'fclose', 'feof', 'fflush', 'fgetline', 'fgetword', 'filetest', 'floor', 'fmod', 'fopen', 'fprint', 'fread', 'frewind', 'fwrite', 'gamma', 'gauss', 'getenv', 'getpid', 'gmatch', 'hermite', 'hsv_to_rgb', 'hypot', 'linstep', 'log', 'mag', 'match', 'max', 'min', 'noise', 'pclose', 'popen', 'pow', 'print', 'putenv', 'pwd', 'rad_to_deg', 'rand', 'randstate', 'rgb_to_hsv', 'rot', 'seed', 'sign', 'sin', 'size', 'sizeBytes', 'smoothstep', 'sort', 'sphrand', 'sqrt', 'strcmp', 'substitute', 'substring', 'system', 'tan', 'tokenize', 'tolower', 'toupper', 'trace', 'trunc', 'unit', 'warning', 'whatIs'] #
melCmdList = [ x for x in melCmdList if not proc_remap.has_key(x) and ( hasattr(pymel,x) or hasattr(builtin_module,x) ) ]

mel_type_to_python_type = {
    'string'     : 'str',
    'int'         : 'int',
    'float'        : 'float',
    'vector'    : 'Vector'
    }

tag = '# script created by pymel.tools.mel2py'


def pythonizeName(name):
    alphaNumeric = string.ascii_letters + string.digits
    chars = []
    for char in name:
        if char not in alphaNumeric:
            chars.append('_')
        else:
            chars.append(char)
    if chars[0] in string.digits:
        # Since python treats names starting with '_' as
        # somewhat special, use another character...
        chars.insert(0, 'n')
    return ''.join(chars)

def getModuleBasename( script ):
    name = os.path.splitext( os.path.basename(script) )[0]
    return pythonizeName(name)

def findModule( moduleName ):
    for f in sys.path:
        f = os.path.join( f, moduleName  + '.py' )
        if os.path.isfile(f):
            # checks for a tag added by mel2py -- this is unreliable, but so is using simple name comparison
            # TODO : add a keyword for passing directories to look for pre-translated python scripts
            file = open(f, 'r')
            firstline = file.readline()
            file.close()
            if firstline.startswith(tag):
                return f
    return

#def _script_to_module( t, script ):
#    global batchData.currentFiles
#    global script_to_module
#
#    path, name = os.path.split(script)
#    if name.endswith('.mel'):
#        name += '.mel'
#
#    try:
#        return script_to_module[name]
#
#    except KeyError:
#
#        if not path:
#            result = mel.whatIs( name )
#            buf = result.split( ':' )
#            if buf[0] == 'Script found in':
#                fullpath = buf[1]
#            else:
#                return
#        else:
#            fullpath = os.path.join(path, name )
#
#
#        moduleName = getModuleBasename(fullpath)
#
#
#        # the mel file in which this proc is defined is being converted with this batch
#        if fullpath in batchData.currentFiles:
#            script_to_module[name] = moduleName
#            return moduleName
def fileInlist( file, fileList ):
    file = util.path(file)
    for dir in fileList:
        try:
            if file.samefile( dir ):
                return True
        except OSError: pass
    return False

def _melObj_to_pyModule( script ):
    """
    Return the module name this mel script / procedure will be converted to / found in.

    If the mel script is not being translated, returns None.
    """
    result = mel.whatIs( script )
    buf = result.split( ': ' )
    if buf[0] in [ 'Mel procedure found in', 'Script found in' ]:
        melfile = util.path( buf[1].lstrip() )
        melfile = melfile.canonicalpath()
        if batchData.currentModules.has_value(melfile):
            return batchData.currentModules.get_key(melfile)
    return None

def _melProc_to_pyModule( t, procedure ):
    """
    determine if this procedure has been or will be converted into python, and if so, what module it belongs to
    """

    # if root_module is set to None that means we are doing a string conversion, and not a file conversion
    # we don't need to find out the current or future python module.  just use pymel.mel
    if t.lexer.root_module in [ None, '__main__']:
        return None, None

    global batchData

    try:
        return batchData.proc_to_module[procedure]
    except KeyError:
        # if the file currently being parsed is not being translated, then this parsing is just for information gathering.
        # no need to recursively parse any further
        if t.lexer.root_module not in batchData.currentModules:
            #print 'No recursive parsing for procedure %s in module %s' % (procedure, t.lexer.root_module)
            moduleName = None
        else:
            moduleName = _melObj_to_pyModule( procedure )

        if moduleName is not None:
            #print "%s not seen yet: scanning %s" % ( procedure, melfile )
            cbParser = MelScanner()
            cbParser.build()
            melfile = batchData.currentModules[moduleName]
            try:
                proc_list, global_procs, local_procs = cbParser.parse( melfile.bytes() )
            except lex.LexError:
                print "Error parsing mel file:", melfile
                global_procs = {}
            #print "global procs", global_procs
            for proc, procInfo in global_procs.items():
                #print proc, procInfo
                batchData.proc_to_module[proc] = (moduleName, procInfo['returnType'])

        if procedure not in batchData.proc_to_module:
            #print "could not find script for procedure: %s" % procedure
            batchData.proc_to_module[procedure] = (None, None)
        return batchData.proc_to_module[procedure]


def format_command(command, args, t):
    if len(args) == 1 and args[0].startswith('(') and args[0].endswith(')'):
        args[0] = args[0][1:-1]



    if t.lexer.verbose:
        print 'p_command: input_list', command, args



    # commands with custom replacements
    try:
        typ, remap_func = proc_remap[command]
        return Token( remap_func(args, t), typ )
    except KeyError: pass

    #flags = getCommandFlags(command)

    # new-style from cached info
    try:
        cmdInfo = factories.cmdlist[command]
    except KeyError:
        try:
            cmdInfo = melCmdFlagList[command]
        except KeyError:
            # Mel procedures and commands without help documentation
            #if flags is None:
            args = ', '.join(args)

            # function is being called locally, within same file
            if command in t.lexer.global_procs:
                returnType = t.lexer.global_procs[command]['returnType']
                return '%s(%s)' % (command, args)
            if command in t.lexer.local_procs:
                returnType = t.lexer.local_procs[command]['returnType']
                return '_%s(%s)' % (command, args)
            if command in melCmdList:
                return '%s(%s)' % (command, args)

            module, returnType = _melProc_to_pyModule( t, command )

            if module:
                # the procedure is in the currently parsed script, but has not yet been placed in global or local procs.
                #if module == t.lexer.root_module:
                #    return '%s(%s)' % (command, args)
                #else:
                t.lexer.imported_modules.add( module )
                res = '%s.%s(%s)' % (module, command, args)
            else:
                res = '%smel.%s(%s)' % (t.lexer.pymel_namespace, command, args)

            return res

    # commands with help documentation
    try:
        #print 'FLAGS', t[1], flags
        #print 'ARGS', args
        kwargs = {}
        pargs = []
        argTally=[]
        numArgs = 0
        commandFlag = False
        flagReg = re.compile("-\s*([A-Za-z][\w_]*)")
        queryMode = False
        currFlag = None
        for token in args:
            flagmatch = flagReg.match( token )

            #----- Flag -----
            if flagmatch:
                if numArgs > 0:
                    #raise ValueError, 'reached a new flag before receiving all necessary args for last flag'
                    if t.lexer.verbose >= 1: print 'reached a new flag before receiving all necessary args for last flag'
                    kwargs[currFlag]='1'
                    numArgs=0

                #(numArgs, commandFlag) = flags[ token ]

                # remove dash (-) before flag
                token = token[1:]

                # a special dict has been creatd to return the new name of flags removed due to name conflicts
                try:
                    token = Token( cmdInfo['removedFlags'][token], token.type, token.lineno )
                except KeyError: pass

                try:
                    flagInfo = cmdInfo['flags'][token]
                except:
                    longname = cmdInfo['shortFlags'][token]
                    flagInfo = cmdInfo['flags'][longname]
                numArgs = flagInfo['numArgs']
                commandFlag = 'command' in flagInfo['longname'].lower()

                #print 'new flag', token, numArgs

                if numArgs == 0 or queryMode:
                    kwargs[token]='1'
                    numArgs=0
                else:
                    currFlag = token

                # moved this after the queryMode check, bc sometimes the query flag expects a value other than a boolean
                if token in ['q', 'query']:
                    queryMode = True

            elif numArgs == 1:
                # callbacks
                if commandFlag:

                    #if False:
                    #if True :
                    try:
                        cbParser = MelParser()
                        #print "root module for callback parsing", t.lexer.root_module
                        cbParser.build( rootModule = t.lexer.root_module,
                                              pymelNamespace=t.lexer.pymel_namespace,
                                              verbosity=t.lexer.verbose,
                                              expressionsOnly=True )

                        tmpToken = token
                        #print tmpToken
                        # pre-parse cleanup

                        #print tmpToken

                        # remove enclosing parentheses
                        tmpToken = tmpToken.strip(' ')
                        while tmpToken.startswith('(') and tmpToken.endswith(')'):
                            tmpToken = tmpToken[1:-1]
                            tmpToken = tmpToken.strip(' ')

                        tmpToken = unescape(tmpToken)

                        if not tmpToken.endswith( ';' ):
                            tmpToken += ';'
                        cb = re.compile(  '#(\d)' )
                        parts = cb.split( tmpToken  )
                        for i in range(1,len(parts),2):
                            parts[i] = '$args[%d]' % ( int(parts[i] ) -1 )
                        tmpToken = ''.join( parts )

                        #print tmpToken

                        # parse
                        tmpToken = cbParser.parse( tmpToken )

                        #print tmpToken

                        # ensure that the result is not empty
                        assert tmpToken.strip()

                        t.lexer.imported_modules.update( cbParser.lexer.imported_modules )

                        # post-parse cleanup
                        if tmpToken.endswith( '\n' ):
                            tmpToken = tmpToken[:-1]

                        tmpToken = tmpToken.replace( '\n', ' and ')

                        token = 'lambda *args: %s' % (tmpToken)

                    #else:
                    except Exception, msg:
                        #print "callback translation failed", msg
                        token = 'lambda *args: %smel.eval(%s)' % (t.lexer.pymel_namespace, token)

                argTally.append(token)
                #print 'last flag arg', currFlag, argTally
                if len(argTally)==1:
                    argTally = argTally[0]
                else:
                    argTally = '(%s)' % ', '.join(argTally)

                # mutliuse flag, ex.  ls -type 'mesh' -type 'camera'
                if currFlag in kwargs:
                    if isinstance(kwargs[currFlag], list):
                        kwargs[currFlag].append( argTally )
                        #print "appending kwarg", currFlag, kwargs
                    else:
                        kwargs[currFlag] = [ kwargs[currFlag], argTally ]
                        #print "adding kwarg", currFlag, kwargs
                else:
                    #print "new kwarg", currFlag, kwargs
                    kwargs[currFlag] = argTally

                numArgs=0
                argTally=[]
                currFlag = None

            elif numArgs > 0:
                argTally.append(token)
                #print 'adding arg', currFlag, argTally
                numArgs-=1
            else:
                pargs.append(token)
        """
        try:
            if kwargs[-1].endswith('='):
                kwargs[-1] += '1';
        except IndexError:
            pass
        """

        #print 'final kw list', kwargs

        # functions that clash with python keywords and ui functions must use the cmds namespace
        if command in filteredCmds: # + uiCommands:
            command = '%scmds.%s' % (t.lexer.pymel_namespace, command)

        # eval command is the same as using maya.mel.eval.  special commands: error, warning, and trace
        elif command == 'eval' or command in melCmdFlagList:
            command = '%smel.%s' % (t.lexer.pymel_namespace, command)

#        # ironically, the python command is a nightmare to convert to pure
#        # python - we need a return value, which means we can't use 'exec', but
#        # we need to be able to execute arbitrary statements, like imports,
#        # which means we can't use eval.
#        # So, just use the maya.cmds.python command...
#        elif command == 'python':
#            return 'eval(%s)' % args[0]
#            #args = map( lambda x: x.strip('"'), args[0].split(' + ') )
#            #return ''.join(args)

        # cycle through our kwargs and format them
        for flag, value in kwargs.items():
            if value is None:
                value = '1'

            # multi-use flag
            #    mel:     ls -type "transform" -type "camera"
            #    python:    ls( type=["transform","camera"] )
            if isinstance( value, list):
                #sep = ','
                #if len(value) > t.lexer.format_options['kwargs_newline_threshhold']:
                #    sep = ',\n\t'
                #pargs.append( '%s=[%s]' % ( flag, sep.join(value) )  )
                value = assemble(t,'multiuse_flag', ', ', value, matchFormatting=True)
                pargs.append( Token( '%s=[%s]' % (flag, value), None, flag.lineno  ) )
            else:
                pargs.append( Token( '%s=%s'   % (flag, value), None, flag.lineno ) )

        #sep = ','
        #if len(pargs) > t.lexer.format_options['args_newline_threshhold']:
        #    sep = ',\n\t'
        #res =  '%s(%s)' % (command, sep.join( pargs ) )
        res =  '%s(%s)' % (command, assemble( t, 'command_args', ',', pargs, matchFormatting=True ) )
        res = t.lexer.pymel_namespace + res
        return res

    except KeyError, key:

        try:
            print command, args
            # remove string encapsulation
            subCmd = eval(args.pop(0))
            # in rare cases this might end up bing -e or -pi, which evaluate to numbers
            assert isinstance( subCmd, basestring )

            formattedSubCmd = format_command( subCmd, args, t )
            return '%s(%s)' % (command, formattedSubCmd)
        except (NameError, AssertionError):
            print "Error Parsing: Flag %s does not appear in help for command %s. Skipping command formatting" % (key, command)
            return '%s(%s) # <---- Formatting this command failed. You will have to fix this by hand' % (command, ', '.join(args))


class BatchData(object):
    """ """
    __metaclass__ = util.Singleton

    def __init__(self, **kwargs):
        self.currentModules = TwoWayDict()
        self.proc_to_module = {}
        self.scriptPath_to_parser = {}
        self.scriptPath_to_moduleText = {}
        self.basePackage = None
        self.outputDir = None
        for key in kwargs:
            setattr(self, key, kwargs[key])

global batchData
batchData = BatchData()

# Get the list of reserved words -- any variables or procedures that conflict with these keywords will be renamed with a trailing underscore
tokens = mellex.tokens



def store_assignment_spillover( token, t ):

    try:
        var = token.__dict__.pop( 'assignment' )
        t.lexer.spillover_pre.append( token + '\n' )
        #print "adding to spillover:", token, token.lineno
        token = var

    except KeyError:
        pass
    return token

def merge_assignment_spillover( t, curr_lineno, title='' ):
    """ """
    result = ''
    if t.lexer.spillover_pre:
        #curr_lineno = t[token_index].lineno
        i=-1
        tokens = t.lexer.spillover_pre[:]
        t.lexer.spillover_pre = []
        for token in tokens:

            if token.lineno == curr_lineno:
                result += token
                #print "adding", title, token[:-1], "(", token.lineno, curr_lineno, t.lexer.lineno, ")"
                #t.lexer.spillover_pre.pop(0)
            else:
                #print "skipping", title, token[:-1], "(", token.lineno, curr_lineno, t.lexer.lineno, ")"
                t.lexer.spillover_pre.append(token)

    return result

def format_assignment_value( val, typ ):
    """
    when assigning a value in mel, values will be auto-cast to the type of the variable, but in python, the variable
    will simply become the new type.  to ensure that the python operates as in mel, we need to cast when assigning
    a value to a variable of a different type    """

    try:

        if typ != val.type:
            #print "assignment not same type", t[1].type, t[3].type
            val = Token(  '%s(%s)' % ( mel_type_to_python_type[typ], val ), **val.__dict__ )
            val.type = typ
            return val
    except:
        # one of the expressions did not have a type
        try:
            typ = val.type
        except:
            print "NO TYPE", val

    return val

def vprint(t, *args):
    if t.lexer.verbose:
        print args

def toList(t):
    tokens = []
    for i in range(1, len(t)):
        if i is not None:
            tokens.append(t[i])
    return tokens

def assemble(t, funcname, separator='', tokens=None, matchFormatting=False):

    #print "STARTING", lineno
    res = ''

    if len(t) > 1:

        if tokens is None:
            tokens = toList(t)

        tokType = None
        res = Token( '', None )
        for i, tok in enumerate( tokens ) :
            if i == 0:
                res += tok
            else:

                try:
                    if not t.lexer.expression_only and matchFormatting and tokens[i-1].lineno != tok.lineno:
                        res +=  separator + '\n' + entabLines( tok )
                    else:
                        res += separator + tok
                except AttributeError:
                    #print tokens[i-1], type(tokens[i-1]), tok, type(tok)
                    res += separator + tok
            try:
                if tok.type:
                    tokType = tok.type
                    #print 'assembled', funcname, p[i], type
            except: pass

        #res = Token( separator.join(tokens), type, t.lexer.lineno )
        #res = Token( res, tokType, lineno=t.lexer.lineno )
    #res = separator.join(p[1:])
    #

    if t.lexer.verbose >= 1:
        print funcname, res, t.lexer.lineno
    #elif t.lexer.verbose >= 1:
    #    print 'assembled', funcname

    #if p[0].find('def') >= 0:
    #    print funcname
    #    print "'%s'" % p[0]
    return res



def addComments( t, funcname = '' ):

    if t.lexer.verbose:
        print "adding comments:", funcname, t.lexer.comment_queue
    t[0] += ''.join(t.lexer.comment_queue) #+ t[0]
    t.lexer.comment_queue = []

def addHeldComments( t, funcname = '' ):

    try:
        commentList = t.lexer.comment_queue_hold.pop()
    except IndexError:
        return ''
    #commentList = ['# ' + x for x in commentList]

    if t.lexer.verbose:
        print t.lexer.comment_queue_hold
        print "adding held comments:", funcname, commentList

    return ''.join(commentList)
    #t[0] = ''.join(commentList) + t[0]


def addHeldComments2( code, t, funcname = '' ):

    commentList = t.lexer.comment_queue_hold.pop()

    commentList = ['# ' + x for x in commentList]

    if t.lexer.verbose:
        print t.lexer.comment_queue_hold
        print "adding held comments:", funcname, commentList

    return ''.join(commentList) + code

def holdComments():
    t.lexer.comment_queue_hold.append( t.lexer.comment_queue )
    t.lexer.comment_queue = []



def entabLines( line ):

    buf = line.split('\n')
    #for x in buf:
    #    if x.startswith(''):
    #        print 'startswith space!', x

    res = '\n'.join( map( lambda x: '\t'+x, buf) )
    if line.endswith('\n'):
        res += '\n'
    return res


"""
translation_unit
    external_declaration
        function_definition
        declaration
"""

def p_translation_unit(t):
    '''translation_unit : external_declaration
                        | translation_unit external_declaration'''
    t[0] = assemble(t, 'p_translation_unit')
    #print '\n'

# external-declaration:
def p_external_declaration(t):
    '''external_declaration : statement
                            | function_definition'''
    t[0] = assemble(t, 'p_external_declaration')
    #if t.lexer.verbose:
    #    print "external_declaration", t[0]

# function-definition:
def p_function_definition(t):
    '''function_definition :  function_declarator function_specifiers_opt ID seen_func LPAREN function_arg_list_opt RPAREN add_comment compound_statement'''
    #t[0] = assemble(t, 'p_function_definition')


    # add to the ordered list of procs
    t.lexer.proc_list.append( t[3] )

    # global proc
    if t[1][0] == 'global':
        t.lexer.global_procs[ t[3] ] = { 'returnType' : t[2], 'args' : t[6] }
        t[0] = addHeldComments(t, 'func') + "def %s(%s):\n%s\n" % (t[3], ','.join(t[6]) , entabLines( t[9]) )

    # local proc gets prefixed with underscore
    else:
        t.lexer.local_procs[ t[3] ] = { 'returnType' : t[2], 'args' : t[6] }
        t[0] = addHeldComments(t, 'func') + "def _%s(%s):\n%s\n" % (t[3], ','.join(t[6]) , entabLines( t[9]) )

def p_seen_func(t):
    '''seen_func :'''

    global batchData
    #print "seen_func", t[-1].__repr__(), t[-2].__repr__(), t[-3].__repr__()

    if t.lexer.root_module in batchData.currentModules:
        module = t.lexer.root_module
    else:
        module = None

    if t[-3][0] == 'global':

        #print "adding function: (%s) %s.%s, %s" % (  t.lexer.root_module, module, t[-1], t[-2] )
        batchData.proc_to_module[ t[-1] ] = ( module, t[-2] )
    #else:
    #    print "skipping function: (%s) %s.%s, %s" % (  t.lexer.root_module, module, t[-1], t[-2] )

def p_add_comment(t):
    '''add_comment :'''
    if t.lexer.verbose:
        print "holding", t.lexer.comment_queue
    t.lexer.comment_queue_hold.append( t.lexer.comment_queue )
    t.lexer.comment_queue = []

# function-specifiers
def p_function_specifiers_opt(t):
    '''function_specifiers_opt : type_specifier
                                  | type_specifier LBRACKET RBRACKET
                                  | empty'''
    # string
    # string[]
    #
    t[0] = assemble(t, 'p_function_specifiers_opt')

def p_function_declarator(t):
    '''function_declarator : GLOBAL PROC
                           | PROC'''
    # string
    # string[]
    #
    t[0] = t[1:]

def p_function_arg(t):
    '''function_arg : type_specifier variable
                    | type_specifier variable LBRACKET RBRACKET'''
    #t[0] = assemble(t, 'p_function_arg')
    t[0] = t[2]
    t.lexer.type_map[t[2]] = t[1]

def p_function_arg_list(t):
    '''function_arg_list : function_arg
                        | function_arg_list COMMA function_arg'''

    #t[0] = assemble(t, 'p_function_arg_list')
    if len(t)>2:
        t[0] = t[1] + [t[3]]
    # start a new list
    else:
        t[0] = [t[1]]

def p_function_arg_list_opt(t):
    '''function_arg_list_opt : function_arg_list
                        |  empty'''

    #t[0] = assemble(t, 'p_function_arg_list_opt')
    if not t[1]:
        t[0] = []
    else:
        t[0] = t[1]

# declaration:
def p_declaration_statement(t):
    '''declaration_statement : declaration_specifiers init_declarator_list SEMI'''
    # int var=6;
    # int var1=6, var2=9;
    #
    #t[0] = assemble(t, 'p_declaration_statement')



    def includeGlobalVar( var ):
        # handle whether we initialize this variable to the value of the mel global variable.
        # in some cases, the global variable is only for passing within the same script, in which
        # case the python global variable will suffice.  in other cases, we may want to retrieve a
        # global set by maya.

        incl_reg = t.lexer.global_var_include_regex    # if nothing set, match all
        excl_reg = t.lexer.global_var_exclude_regex        # if nothing set, match none
        if re.match(incl_reg, var) and not re.match(excl_reg, var):
            return True
        else:
            return False

    t[0] = ''

    isGlobal = False
    typ = t[1]
    if len(typ) == 2:
        assert typ[0] == 'global'
        typ = typ[1]
        isGlobal = True
    else:
        typ = typ[0]


    # each declaration is a two-element tuple: ( variable, value )
    for var, val in t[2]:


        if '[]' in var:
            iType = typ + '[]'
            array = True
        else:
            iType = typ
            array = False

        # this must occur after the bracket check, bc the globalVar attribute never includes brackets
        try:
            var = var.globalVar
        except AttributeError: pass

        # this must occur after the globalVar attribute check, bc otherwise it will convert the Token into a string
        var = var.strip().strip('[]')

        # default initialization
        if val is None:

            # non -array intitialization
            try:
                val = {
                    'string': "''",
                    'int':    '0',
                    'float': '0.0',
                    'vector': 'Vector()'
                }[  iType  ]

            # array initialization
            except KeyError:
                assert '[]' in iType
                if t.lexer.force_compatibility:
                    val = '%sutil.defaultlist(%s)' % ( t.lexer.pymel_namespace,
                                                     mel_type_to_python_type[typ] )
                else:
                    val = '[]'

            t.lexer.type_map[var] = iType

            # global variable -- overwrite init
            if isGlobal:

                t.lexer.global_vars.add( var )

                # this is the old method, leaving here in case we want to add a switch
                if False:
                    t[0] += 'global %s\n' % var
                    if includeGlobalVar( var):
                        t[0] += "%s = %sgetMelGlobal('%s','%s')\n" % (var, t.lexer.pymel_namespace, iType, var)
                else:
                    t[0] += "%smelGlobals.initVar( '%s', '%s' )\n" % ( t.lexer.pymel_namespace, iType, var )

            else:
                t[0] += var + '=' + val + '\n'

        # initialize to value
        else:

            t[0] += merge_assignment_spillover( t, val.lineno, 'declaration_statement' )
            val = format_assignment_value( val, iType )

            try:
                if val.tokenize:
                    t[0] += format_tokenize_size(val,var)

            except:

                val = val.strip()
                if val.endswith('[]') and val != '[]':
                    val.strip('[]')

                t.lexer.type_map[var] = iType

                if isGlobal:

                    t.lexer.global_vars.add(var)

                    # this is the old method, leaving here in case we want to add a switch
                    if False:
                        t[0] += 'global %s\n' % var
                        t[0] += '%s=%s\n' % (var, val)
                        if includeGlobalVar( var):
                            t[0] += "%ssetMelGlobal( '%s', '%s', %s )\n" % ( t.lexer.pymel_namespace, iType, var, var)
                    else:
                        t[0] += "%smelGlobals.initVar( '%s', '%s' )\n" % ( t.lexer.pymel_namespace, iType, var )
                        t[0] += "%smelGlobals['%s'] = %s\n" % ( t.lexer.pymel_namespace, var, val)

                else:
                    if array and t.lexer.force_compatibility:
                        val = '%sutil.defaultlist(%s, %s)' % ( t.lexer.pymel_namespace,
                                                     mel_type_to_python_type[typ],
                                                     val )

                    t[0] += var + '=' + val + '\n'


    addComments( t, 'declaration_statement' )


# declaration-specifiers
def p_declaration_specifiers(t):
    '''declaration_specifiers : type_specifier
                              | GLOBAL type_specifier'''
    # int
    # global int
    #
    if len(t) > 2:
        t[0] = (t[1], t[2])

    else:
        t[0] = (t[1], )
    #t[0] = assemble(t, 'p_declaration_specifiers', ' ')

# type-specifier:
def p_type_specifier(t):
    '''type_specifier : INT
                      | FLOAT
                      | STRING
                      | VECTOR
                      | MATRIX
                      '''
    t[0] = assemble(t, 'p_type_specifier')



# init-declarator-list:
def p_init_declarator_list(t):
    '''init_declarator_list : init_declarator
                            | init_declarator_list COMMA init_declarator'''
    # var=6;
    # var1=6, var2=9;
    #
    #t[0] = assemble(t, 'p_init_declarator_list')

    # add to list
    if len(t)>2:
        t[0] = t[1] + [t[3]]
    # start a new list
    else:
        t[0] = [t[1]]



# init-declarator
def p_init_declarator(t):
    '''init_declarator : declarator
                        | declarator EQUALS expression'''
    # var=6
    #
    #t[0] = assemble(t, 'p_init_declarator', ' ')

    if len(t) > 2:
        t[0] = (t[1], store_assignment_spillover( t[3], t) )

    else:
        t[0] = (t[1], None )



# declarator:
def p_declarator(t):
    '''declarator : variable
                  | declarator LBRACKET constant_expression_opt RBRACKET'''
#                    | LPAREN declarator RPAREN        removed 11/05 in effort to get cast_expression working
#                    | declarator LPAREN parameter_type_list RPAREN
#                    | declarator LPAREN identifier_list RPAREN
#                    | declarator LPAREN RPAREN '''
    # var
    # var[]
    # var[1]
    if len(t) > 2:
        t[3] = store_assignment_spillover( t[3], t )
    t[0] = assemble(t, 'p_declarator')
    #if len(t) == 5:
    #    if not t[3]:
    #        t[0] = t[1]


# Optional fields in abstract declarators
def p_constant_expression_opt_1(t):
    '''constant_expression_opt : empty'''
    t[0] = assemble(t, 'p_constant_expression_opt_1')

def p_constant_expression_opt_2(t):
    '''constant_expression_opt : constant_expression'''
    t[0] = assemble(t, 'p_constant_expression_opt_2')


# statement:
def p_statement_expr(t):
    '''statement : expression_statement
              | command_statement
              | compound_statement'''

    t[0] = assemble(t, 'p_statement_expr')

def p_statement_complex(t):
    '''statement : selection_statement
              | iteration_statement
              | jump_statement
              | declaration_statement'''
#              | comment'''
    if t.lexer.expression_only:
        raise TypeError, "This mel code is not capable of being translated as a python expression"
    t[0] = assemble(t, 'p_statement_complex')

# labeled-statement:
#def REMOVED_labeled_statement_1(t):
#    '''labeled_statement : ID COLON statement'''
#    # N/A ?
#    t[0] = assemble(t, 'p_labeled_statement_1')



def p_labeled_statement_list(t):
    '''labeled_statement_list : labeled_statement
                  | labeled_statement_list labeled_statement'''

    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

#def REMOVED_labeled_statement_2(t):
#    '''labeled_statement : CASE constant_expression COLON statement_list_opt'''
#    #t[0] = assemble(t, 'p_labeled_statement_2')
#    t[0] = ['case %s == ' + t[2] + ':\n'] + t[4]

#def REMOVED_labeled_statement_3(t):
#    '''labeled_statement : DEFAULT COLON statement_list'''
#    #t[0] = assemble(t, 'p_labeled_statement_3')
#
#    t[0] = ['else:\n'] + t[3]

def p_labeled_statement_2(t):
    '''labeled_statement : CASE constant_expression COLON statement_list_opt'''
    #t[0] = assemble(t, 'p_labeled_statement_2')
    fallthrough = True
    block = []
    for line in t[4]:
        lines = [ x + '\n' for x in line.split('\n')]
        block.extend(lines)

    i=0
    for i,line in enumerate(block):
        #print "--->", line
        if line.startswith('break'):
            #print "---breaking----"
            fallthrough = False
            break

    block = block[:i]

    t[0] = [t[2], block, fallthrough]

def p_labeled_statement_3(t):
    '''labeled_statement : DEFAULT COLON statement_list_opt'''
    #t[0] = assemble(t, 'p_labeled_statement_3')
    block = []
    for line in t[3]:
        if line.startswith('break'):
            fallthrough = False
            break
        block.append(line)
    t[0] = [None, block, False]

# expression-statement:
def p_expression_statement(t):
    '''expression_statement : expression_opt SEMI'''

    t[0] = merge_assignment_spillover( t, t[1].lineno, 'expression_statement'  )
    t[0] += t[1] + '\n'
    addComments(t)

# compound-statement:
def p_compound_statement(t):
    '''compound_statement   : LBRACE statement_list RBRACE
                            | LBRACE RBRACE''' # causes reduce/reduce conflict with postfix_expression

    #print "compound, emptying queue:", t.lexer.comment_queue
    #t[0] = ''.join(t.lexer.comment_queue)
    #t.lexer.comment_queue = []

    #t[0] = assemble(t, 'p_compound_statement')

    if len(t) == 4:
        t[0] = ''.join(t[2])
    else:
        t[0] = 'pass\n'
        addComments(t, 'compound_pass')

def p_statement_list_opt(t):
    '''statement_list_opt : statement_list
                  | empty'''
    #t[0] = assemble(t, 'p_expression_list_opt')
    if isinstance(t[1],list):
        t[0] = t[1]
    else:
        t[0] = []

# statement-list:
def p_statement_list(t):
    '''statement_list   : statement
                        | statement_list statement'''
    #t[0] = assemble(t, 'p_statement_list')
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

# selection-statement
def p_selection_statement_1(t):
    '''selection_statement : IF LPAREN expression RPAREN statement'''
    #t[0] = assemble(t, 'p_selection_statement_1')
    t[0] = merge_assignment_spillover( t, t[3].lineno, 'selection_statement_1' )
    t[0] += 'if %s:\n%s' % (t[3],entabLines(t[5]))


def p_selection_statement_2(t):
    '''selection_statement : IF LPAREN expression RPAREN statement ELSE add_comment statement '''
    #t[0] = assemble(t, 'p_selection_statement_2')
    t[0] = merge_assignment_spillover( t, t[3].lineno, 'selection_statement_2' )
    t[0] += 'if %s:\n%s\n' % (t[3], entabLines(t[5]))

    # elif correction
    match = re.match( r'(?:\s*)(if\b.*:)', t[8] )
    elseStmnt = ''
    if match:
        elseStmnt='el%s\n%s' % ( match.group(1), t[8][match.end()+1:] )
    else:
        elseStmnt='else:\n%s' % ( entabLines(t[8]) )

    t[0] += addHeldComments( t, 'if/else') + elseStmnt
    #t[0] += addHeldComments2( t, elseStmnt, 'if/else')
    #addHeldComments(t, 'if/else')

def p_selection_statement_3(t):
    '''selection_statement : SWITCH LPAREN expression RPAREN add_comment LBRACE labeled_statement_list RBRACE'''
    #t[0] = assemble(t, 'p_selection_statement_3')

    """
    cases = t[7]  # a 2d list: a list of cases, each with a list of lines
    #cases[1:-1]:
    t[0] = ''
    #print cases
    for i,thiscase in enumerate(cases):
        #print 'MAIN', thiscase[0] % t[3]

        # create the first line of the statement block
        caseline = thiscase[0]
        if caseline.startswith('case'):
            if i==0:
                caseline = 'if' + caseline[4:]
            else:
                caseline = 'elif' + caseline[4:]
        try:
            t[0] += caseline % t[3]
        except TypeError:
            t[0] += caseline

        broken = False
        for case in cases[i:]:
            if broken == True:
                break
            for line in case[1:]:
                if line == 'break\n':
                    broken = True
                    break
                    t[0] += '\t' + line
    """
    t[0] = ''
    cases = t[7]  # a 2d list: a list of cases, each with a list of lines
    variable = t[3]
    i = 0
    control = ''

    while i < len(cases):

        if i == 0:
            control = 'if'
        else:
            control = 'elif'

        mainCondition = cases[i][0]
        conditions = set([])
        lines = []

        # cycle through cases until we stop falling through
        for j, (condition, block, fallthrough) in enumerate(cases[i:]):

            if fallthrough:
                if len(block):
                    lines += block
                else:
                    conditions.add(condition)
                    i += 1 # on the next while loop, we will skip this case, because it is now subsumed under the current case

            else:
                if len(block):
                    lines += block
                else:
                    lines.append( 'pass\n' )

                if condition is not None and len(conditions) == j:
                    conditions.add(condition)

                break

        i += 1
        conditions.add( mainCondition )
        conditions = list(conditions)
        block = entabLines( ''.join( lines ) )
        if len(conditions)>1:
            t[0] += '%s %s in [%s]:\n%s' % ( control, variable, ','.join(conditions), block )
        else:
            if conditions[0] is None:
                t[0] +=  'else:\n%s' % ( block )
            else:
                t[0] +=  '%s %s == %s:\n%s' % ( control, variable, conditions[0], block )


    #print t[0]

    t[0] = addHeldComments(t, 'switch') + t[0]


#def REMOVED_selection_statement_3(t):
#    '''selection_statement : SWITCH LPAREN expression RPAREN add_comment LBRACE labeled_statement_list RBRACE'''
#    #t[0] = assemble(t, 'p_selection_statement_3')
#
#    cases = t[7]  # a 2d list: a list of cases, each with a list of lines
#    #cases[1:-1]:
#    t[0] = ''
#    #print cases
#    for i in range(1,len(cases)):
#        # if previous block fell through
#        if cases[i-1][2]:
#            func_name = 'switch_%s_%s()' % (t[3], i+1)
#            if cases[i][0] is None:
#                func_name = 'switch_%s_default()' % (t[3])
#
#            t[0] += 'def %s:\n%s' % (func_name, entabLines(cases[i][1]))
#            cases[i][1] = func_name + '\n'
#
#    for i, (condition, x, x) in enumerate(cases):
#        if condition:
#            if i == 0:
#                t[0] += 'if %s == %s:\n' % (t[3], condition)
#            else:
#                t[0] += 'elif %s == %s:\n' % (t[3], condition)
#        else:
#            t[0] += 'else:\n'
#
#        for (x, block, fallthrough) in cases[i:]:
#            t[0] += entabLines(block)
#            if not fallthrough:
#                break
#
#    print t[0]
#
#    addHeldComments(t, 'switch')


# iteration_statement:
def p_iteration_statement_1(t):
    '''iteration_statement : WHILE LPAREN expression RPAREN add_comment statement'''
    #t[0] = assemble(t, 'p_iteration_statement_1')
    t[0] = addHeldComments(t, 'while') + 'while %s:\n%s\n' % (t[3], entabLines(t[6]) )


def p_iteration_statement_2(t):
    '''iteration_statement : FOR LPAREN expression_list_opt SEMI expression_list_opt SEMI expression_list_opt RPAREN add_comment statement '''
    #t[0] = assemble(t, 'p_iteration_statement_2')

    """
    =============================================
    RANGE : specific case, where only 1 cond.
    =============================================
    init   >=1
    cond   = 1
    update >=1

    other requirements:
    1) the iterator must exist alone on one
    side of the    conditional expression.
    2) the iterator can appear only once in the
    update expression
    ---------------------------------------------
    solution:
        add extra inits before beginning of loop
        add extra updates to end of each loop
    ---------------------------------------------

    int $i;
    for( $i=0, int $j=0; $i<10; $i++, $j++) print $i;



    i = 0
    j = 0
    for i in range(0,10):
        print i
        j+=1

    =============================================
    WHILE : all others
    =============================================
    init   >=0
    cond   >=0
    update >=0
    ---------------------------------------------
    solution:
        use a while statement
        add any inits before beginning of loop
        add any conditions to beginning of each loop
        add any updates to end of each loop
    ---------------------------------------------

    int $i=0;
    for(; ; )
    {
        print $i;
        if ($i > 10)
            break;
        $i++;
    }

    int $i;
    for(; ; $i++) {
        print $i;
        if ($i > 10)
            break;
    }



    i=0
    while 1:
        print i
        if i > 10:
            break
        i++


    """

    #------------------------------------------------------------------
    # for( init_expr; cond_expr; update_expr
    #------------------------------------------------------------------
    # for( iterator=start; iterator(relop)stop; iterator(+/-=)step )
    #------------------------------------------------------------------

    # regular expression for a variable
    var_reg = re.compile(r'[A-Za-z_][\w_]*')

    init_exprs = t[3]
    cond_exprs = t[5]
    update_exprs = t[7]
    statement_body = t[10]

    def default_formatting():
        t[0] = ''
        if init_exprs:
            t[0] += '\n'.join(init_exprs)

        t[0] += '\nwhile 1:\n'

        if cond_exprs:
            t[0] += entabLines( 'if not ( %s ):\n\tbreak\n' % ' or '.join(cond_exprs) )

        t[0] += entabLines( statement_body )

        if update_exprs:
            t[0] += entabLines('\n'.join( update_exprs ) + '\n')

        t[0] = addHeldComments(t, 'for') + t[0]

    if len(cond_exprs) == 1 and len(init_exprs) >= 1 and len(update_exprs) >=1:
        #---------------------------------------------
        # Conditional Expression  --> End
        #---------------------------------------------
        # the conditional expression becomes the end value of a range() function
        # there can be only one variable driven by the range expression, so there can be only one coniditional expression
        end = None
        regex = re.compile('\s*(<=|>=|<|>)\s*')
        cond_buf = regex.split(cond_exprs[0])
        try:
            cond_relop = cond_buf.pop(1)    # cond_buf now contains 2 values, one of which will become our iterator
        except IndexError:
            return default_formatting()

        cond_vars = set( filter( var_reg.match, cond_buf) )

        #---------------------------------------------
        # Update Expression --> Step
        #---------------------------------------------
        # The initialization is optional, so the next most important expression is the update expression.
        iterator = None
        step = None
        update_op = None
        count = 0
        regex = re.compile('\s*(\+\+|--|\+=|-=)\s*')
        for expr in update_exprs:
            # expr: i++
            update_buf = regex.split(expr)

            # update_opt:  ++
            try:
                update_op = update_buf.pop(1) # this might raise an indexError if the update expression followed the form:  $i = $i+1
                # find the variables in the update statement, and find which were also present in conditional statement
                update_vars = filter( var_reg.match, update_buf)
                iterator = list(cond_vars.intersection(update_vars))
                #print cond_vars, tmp, iterator
            except IndexError:
                count += 1
            else:
                if len(iterator) > 1:
                    '''raise ValueError, """Python does not support for loops of format '(init_exp; cond_exp; update_exp)'.
    In order to convert these statements to python, for loop iterator must appear only once in the update expression. I found %d (%s). Please correct this portion of the loop: %s.""" % ( len(iterator), ','.join(iterator), t[7] )
                    '''
                    return default_formatting()
                try:
                    iterator = iterator[0]
                    update_buf.remove(iterator)
                    cond_buf.remove(iterator)
                    step = update_buf[0]
                    end = cond_buf[0]
                    break
                except:
                    iterator = None

        if iterator is None:
            '''raise ValueError, """Python does not support for loops of format '(init_exp; cond_exp; update_exp)'.
    In order to convert these statements to python, for loop iterator must appear alone on one side of the conditional expression. Please correct this portion of the loop: %s.""" % ( t[5] )
            '''
            return default_formatting()

        update_exprs.pop(count)

        #print "iterator:%s, update_op:%s, update_expr:%s, step:%s" % (iterator, update_op, update_exprs, step)

        # determine the step
        if update_op.startswith('-'):
            step = '-'+step
            if cond_relop == '>=':
                end = end + '-1'
        elif cond_relop == '<=':
            end = end + '+1'

        #---------------------------------------------
        # initialization --> start
        #---------------------------------------------
        start = None
        init_reg = re.compile('\s*=\s*')

        for expr in init_exprs:
            init_buf = init_reg.split(expr)
            try:
                init_buf.remove(iterator)
            except ValueError:
                pass
            else:
                if len(init_buf):
                    start = init_buf[0]
                else:
                    start = iterator

        #print "start: %s, end: %s, step: %s" % (start, end, step)

        if step == '1':
            t[0] = 'for %s in range(%s,%s):\n%s' % (iterator, start, end, entabLines(statement_body))
        else:
            t[0] = 'for %s in range(%s,%s,%s):\n%s' % (iterator, start, end, step, entabLines(statement_body) )

        if len( update_exprs ):
            t[0] += '\n' + entabLines('\n'.join(update_exprs) + '\n')

        t[0] = addHeldComments(t, 'for') + t[0]
    else:
        default_formatting()

def p_iteration_statement_3(t):
    '''iteration_statement : FOR LPAREN variable IN expression seen_FOR RPAREN add_comment statement '''
    #t[0] = assemble(t, 'p_iteration_statement_3')
    t[0] = addHeldComments(t, 'for') + 'for %s in %s:\n%s' % (t[3], t[5], entabLines(t[9]))


def p_seen_FOR(t):
    '''seen_FOR :'''

    t.lexer.type_map[t[-3].strip()] = t[-1].type


def p_iteration_statement_4(t):
    '''iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI'''
    t[0] = assemble(t, 'p_iteration_statement_4')

    t[0] = t[2]    + '\n'
    t[0] += 'while %s:\n%s\n' % (t[5], entabLines(t[2]) )
    t[0] = addHeldComments(t, 'do while') + t[0]

# jump_statement:
def p_jump_statement(t):
    '''jump_statement : CONTINUE SEMI
                    | BREAK SEMI
                    | RETURN expression_opt SEMI'''
    t[0] = assemble(t, 'p_jump_statement')
    if len(t)==4:
        t[0] = t[1] + ' ' + t[2] + '\n'
    else:
        t[0] = t[1] + '\n'
    addComments(t)

# optional expression
def p_expression_opt(t):
    '''expression_opt : empty
                      | expression'''
    t[0] = assemble(t, 'p_expression_opt')




# expression:
""""
ID
constant
SCONST
LPAREN expression RPAREN
    primary
        postfix
            unary
                cast
                    multiplicative
                        additive
                            shift
                                relational
                                    equality
                                        AND
                                            exclusive_or
                                                inclusive_or
                                                    logical_and
                                                        logical_or
                                                            conditional
                                                                constant
                                                                assignment
                                                                    expression
"""


def p_expression_list_opt(t):
    '''expression_list_opt : expression_list
                  | empty'''
    #t[0] = assemble(t, 'p_expression_list_opt')

    if isinstance(t[1],list):
        t[0] = t[1]
    else:
        t[0] = []

def p_expression_list(t):
    '''expression_list : expression
                  | expression_list COMMA expression'''
    # descendents: vector, array, for-loop

    #t[0] = assemble(t, 'p_expression')

    # new
    if len(t) == 2:
        t[0] = [t[1]]

    # append
    else:
        t[0] = t[1] + [t[3]]




def p_expression(t):
    '''expression : conditional_expression'''
    t[0] = assemble(t, 'p_expression')


# constant-expression
def p_constant_expression(t):
    '''constant_expression : conditional_expression'''
#                            | CAPTURE command CAPTURE'''
    t[0] = assemble(t, 'p_constant_expression')

# conditional-expression
def p_conditional_expression_1(t):
    '''conditional_expression : logical_or_expression'''
    t[0] = assemble(t, 'p_conditional_expression_1', ' ')


def p_conditional_expression_2(t):
    '''conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression '''

    # ($x>1) ? 1 : 0  --->  (x>1) and 1 or 0
    t[1] = store_assignment_spillover( t[1], t )
    t[2] = 'and'
    t[3] = store_assignment_spillover( t[3], t )
    t[4] = 'or'
    t[5] = store_assignment_spillover( t[5], t )
    t[0] = assemble(t, 'p_conditional_expression_2', ' ')
    #t[0] = '%s and %s or %s' % ( t[1], t[3], t[5] )






# logical-or-expression
def p_logical_or_expression_1(t):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression LOR logical_and_expression'''

    if len(t) == 4:
        t[1] = store_assignment_spillover( t[1], t )
        t[2] = 'or'
        t[3] = store_assignment_spillover( t[3], t )

    t[0] = assemble(t, 'p_logical_or_expression', ' ')

# logical-and-expression
def p_logical_and_expression_1(t):
    '''logical_and_expression : assignment_expression
                              | logical_and_expression LAND assignment_expression'''

    if len(t) == 4:
        t[1] = store_assignment_spillover( t[1], t )
        t[2] = 'and'
        t[3] = store_assignment_spillover( t[3], t )
    t[0] = assemble(t, 'p_logical_and_expression', ' ')




# assigment_expression:
def p_assignment_expression(t):

    '''assignment_expression : equality_expression
                            | postfix_expression assignment_operator assignment_expression''' # changed first item from unary to postfix
#                            | CAPTURE assignment_expression CAPTURE'''
#                            | unary_expression assignment_operator CAPTURE assignment_expression CAPTURE'''

    if len(t) == 4:
        #print t[1], t[2], t[3]

        t[3] = format_assignment_value( t[3], t[1].type )

        if hasattr( t[3], 'tokenize' ):
            t[0] = format_tokenize_size(t[3],t[1])

        else:

            # remove array brackets:  string[]
            if t[2] and t[1].endswith('[]'):
                raise NotImplementedError, "I didn't think we'd make it here. the line below seems very wrong."
                #t[0] = ' '.join( [ t[1][:-2], t[1], t[2] ] )

            elif t[2] in ['=',' = '] and  t.lexer.expression_only:
                raise TypeError, "This mel code is not capable of being translated as a python expression"

            # fill in the append string:
            #    start:        $foo[size($foo)] = $bar
            #    stage1:        foo[len(foo)] = bar
            #    stage2:        foo.append(%s) = bar
            #    stage3:        foo.append(bar)

            elif hasattr( t[1], 'appendingToArray' ):
                var = t[1].appendingToArray
                if hasattr( t[1], 'globalVar' ):
                    t[0] = '%s += [%s]' % ( var, t[3] )
                else:
                    t[0] = '%s.append(%s)' % ( var, t[3] )


            # setting item on a global array
            elif hasattr( t[1], 'globalVar') and hasattr( t[2], 'indexingItem' ):
                var, expr = t[1].indexingItem
                t[0] = var + '.setItem(%s,%s)' % ( expr, t[3])

#                elif t[1].endswith('.append(%s)'):  # replaced below due to a var[len(var)]
#                    t[0] = t[1] % t[3]
#
#
#                elif t[1].endswith(' += [%s]'): # replaced below due to a var[len(var)], special case for global variables
#                    t[0] = t[1] % t[3]

            else:
                t[0] = assemble(t, 'p_assignment_expression')
                t[0].assignment = t[1]

    else:
        t[0] = assemble(t, 'p_assignment_expression')

# assignment_operator:
def p_assignment_operator(t):
    '''
    assignment_operator : EQUALS
                        | TIMESEQUAL
                        | DIVEQUAL
                        | MODEQUAL
                        | PLUSEQUAL
                        | MINUSEQUAL
                        | CROSSEQUAL
                        '''
    t[0] = assemble(t, 'p_assignment_operator')

# equality-expression:
def p_equality_expression_1(t):
    '''equality_expression : relational_expression
                            | equality_expression EQ relational_expression
                            | equality_expression NE relational_expression'''

    if len(t) == 4:
        t[1] = store_assignment_spillover( t[1], t )
        t[3] = store_assignment_spillover( t[3], t )

    t[0] = assemble(t, 'p_equality_expression_3', ' ')

# relational-expression:

def p_relational_expression_1(t):
    '''relational_expression : shift_expression
                             | relational_expression LT shift_expression
                             | relational_expression GT shift_expression
                             | relational_expression LE shift_expression
                             | relational_expression GE shift_expression'''

    if len(t) == 4:
        t[1] = store_assignment_spillover( t[1], t )
        t[3] = store_assignment_spillover( t[3], t )

    t[0] = assemble(t, 'p_relational_expression_5')

# shift-expression
def p_shift_expression(t):
    'shift_expression : additive_expression'
    t[0] = assemble(t, 'p_shift_expression')

# additive-expression
def p_additive_expression(t):
    '''additive_expression : multiplicative_expression
                            | additive_expression PLUS multiplicative_expression
                            | additive_expression MINUS multiplicative_expression'''



    if len(t) == 4:
        t[1] = store_assignment_spillover( t[1], t )
        t[3] = store_assignment_spillover( t[3], t )

        if t[2] == '+':
            #print t[1], t[1].type, t[3], t[3].type
            if t[1].type == 'string' and t[3].type != 'string':
                t[0] = Token( '%s + str(%s)' % (t[1], t[3]) , 'string' )
                return
            elif t[3].type == 'string' and t[1].type != 'string':
                t[0] = Token( 'str(%s) + %s' % (t[1], t[3]), 'string' )
                return

    t[0] = assemble(t, 'p_additive_expression', ' ')


    #    if t[1].endswith('"'):
    #        t[0] = t[1][:-1] + '%s" % ' + t[3]

# multiplicative-expression

def p_multiplicative_expression(t):
    '''multiplicative_expression : cast_expression
                                | multiplicative_expression TIMES cast_expression
                                | multiplicative_expression DIVIDE cast_expression
                                | multiplicative_expression MOD cast_expression
                                | multiplicative_expression CROSS cast_expression'''
    if len(t) > 2:
        t[1] = store_assignment_spillover( t[1], t )
        t[3] = store_assignment_spillover( t[3], t )

    t[0] = assemble(t, 'p_multiplicative_expression', ' ')




# cast-expression:
def p_cast_expression(t):
    '''cast_expression : unary_expression
                        | unary_command_expression
                        | type_specifier LPAREN expression RPAREN
                        | LPAREN type_specifier RPAREN cast_expression'''
    # (int)myvar

    if len(t) == 5 and t[1] == '(':
        t[0] =  Token( '%s(%s)' % (mel_type_to_python_type[ t[2] ], t[4]) , t[2].type  )
        # skip assemble
        return

    # int( x+3 )
    if len(t) == 5 and t[1] == 'string':
        t[1] = mel_type_to_python_type[ t[1] ]

    t[0] = assemble(t, 'p_cast_expression')


# unary-expression
def p_unary_expression(t):
    '''unary_expression : postfix_expression
                        | unary_operator cast_expression'''

    if len(t)>2:
        if t[1] == '!':
            t[1] = 'not '

        t[2] = store_assignment_spillover( t[2], t )
        t[0] = Token( t[1] + t[2], t[2].type, t[2].lineno )

    else:
        t[0] = assemble(t, 'p_unary_expression')

def p_unary_expression_2(t):
    '''unary_expression : PLUSPLUS unary_expression
                        | MINUSMINUS unary_expression'''
    # ++$var --> var+=1
    #t[0] = Operation( t[2], t[1][0] + '=', '1')
    t[0] = assemble(t, 'p_unary_expression', '', [t[2], t[1][0] + '=1'] )
    t[0].assignment = t[2]

# unary-command-expression:
def p_unary_command_expression(t):
    '''unary_command_expression : procedure_expression
                                | unary_operator procedure_expression'''

    if len(t)>2 and t[1] == '!':
            t[1] = 'not '
    t[0] = assemble(t, 'p_unary_expression')

# unary-operator
def p_unary_operator(t):
    '''unary_operator : PLUS
                    | MINUS
                    | NOT'''
    t[0] = assemble(t, 'p_unary_operator')

#def p_catch_expression(t):
#    '''catch_expression : procedure_expression
#                    | CATCH expression'''
#    t[0] = assemble(t, 'p_catch_expression')

# procedure_expression
def p_procedure_expression(t):
    '''procedure_expression : command_expression
                             | procedure'''

    t[0] = assemble(t, 'p_procedure_expression')


#def p_procedure(t):
#    '''procedure : ID LPAREN procedure_expression_list RPAREN
#                 | ID LPAREN RPAREN '''
#    #t[0] = assemble(t, 'p_procedure')
#    #t[0] = 'mel.' + t[0]
#    if len(t) == 5:
#        t[0] = format_command( t[1], t[3], t )
#    else:
#        t[0] = format_command( t[1],[], t )

def p_procedure(t):
    '''procedure : ID LPAREN procedure_expression_list RPAREN
                    | ID LPAREN RPAREN'''

    # myProc( "this", 2 )
    # myProc()

    if len(t) == 5:
        t[0] = format_command( t[1], t[3], t )
    elif len(t) == 3:
        t[0] = format_command( t[1],[t[2]], t )
    else:
        t[0] = format_command( t[1],[], t )

def p_procedure_expression_list(t):
    '''procedure_expression_list : constant_expression
                               | procedure_expression_list COMMA constant_expression'''
                               #| procedure_expression_list COMMA comment command_expression'''

    #t[0] = assemble(t, 'p_procedure_expression_list', matchFormatting=False )

    if len(t)>2:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1]]

    return

#    if len(t) == 4:
#        t[2] = None
#
#    elif len(t) == 5:
#        t[2] = None
#        t[3] += t[4]
#        t[4] = None
#
#    t[0] = assemble(t, 'p_procedure_expression_list', ', ')


# command expression
def p_command_expression(t):
    '''command_expression : CAPTURE command CAPTURE'''
    t[0] = t[2]

# postfix-expression:
def p_postfix_expression(t):
    '''postfix_expression : primary_expression
                            | postfix_expression PLUSPLUS
                            | postfix_expression MINUSMINUS'''
#                            | postfix_expression LBRACE initializer_list RBRACE'''
#                            | postfix_expression command_input_list'''

    # $var++ --> var += 1


    # ++ and -- must be converted to += and -=
    if len(t) == 3:
        t[2] = t[2][0] + '=1'
        t[0] = assemble(t, 'p_postfix_expression')
        t[0].assignment = t[1]
    else:
        t[0] = assemble(t, 'p_postfix_expression')


def p_postfix_expression_2(t):
    '''postfix_expression : LBRACE expression_list_opt RBRACE'''

    # array

    #t[0] = assemble(t, 'p_postfix_expression')
    #t[0] = '[%s]' % ','.join(t[2])
    t[2] = [ store_assignment_spillover( x, t ) for x in t[2] ]
    t[0] = '[%s]' % assemble(t, 'p_postfix_expression_2', ',', t[2], matchFormatting=True)

def p_postfix_expression_3(t):
    '''postfix_expression : LVEC expression_list RVEC'''

    # vector

    #t[0] = assemble(t, 'p_postfix_expression')
    t[2] = [ store_assignment_spillover( x, t ) for x in t[2] ]
    t[0] = Token( 'Vector([%s])' % ','.join(t[2]), 'vector', t.lexer.lineno )

def p_postfix_expression_4(t):
    '''postfix_expression : postfix_expression LBRACKET expression RBRACKET'''

    # array element index:
    # $var[2-4]
    type = t[1].type
    t[3] = store_assignment_spillover( t[3], t )
    if not t[3]:
        t[0] = t[1]
    elif t[3] == 'len(%s)' % t[1]:
        t[0] = t[1] + '[' + t[3] + ']'
        t[0].appendingToArray = str(t[1])

        #if hasattr( t[1], 'globalVar' ):
        #    t[0] = t[1] + ' += [%s]'
        #else:
        #    t[0] = t[1] + '.append(%s)'
    else:
        lenSubtractReg = re.compile( 'len\(%s\)\s*(-)' % t[1] )
        try:
            # assignment relative to the end of the array:   x[-1]
            t[0] = t[1] + '[%s]' % (''.join(lenSubtractReg.split( t[3] )) )
        except:
            t[0] = t[1] + '[%s]' % ( t[3] )

    # type is no longer an array
    try:
        t[0].type = type.strip('[]')
    except AttributeError: pass

    if hasattr( t[1], 'globalVar' ):
        t[0].indexingItem = ( t[1], t[3] )

# primary-expression:
def p_primary_expression_paren(t):
    '''primary_expression :    LPAREN expression RPAREN'''

    t[0] = Token( t[1] + t[2] + t[3], t[2].type )

def p_primary_expression(t):
    '''primary_expression :    boolean'''
    t[0] = assemble(t, 'p_primary_expression')


def p_primary_expression1(t):
    '''primary_expression :     ICONST'''
    # not needed, python understands this notation without the conversion below
    #if t[1].startswith('0x'):
    #    t[1] = "int( '%s', 16 )" % t[1]
    t[0] = Token(t[1], 'int', t.lexer.lineno)
    if t.lexer.verbose >= 2:
        print "p_primary_expression", t[0]

def p_primary_expression2(t):
    '''primary_expression :     SCONST'''
    t[0] = Token(t[1], 'string', t.lexer.lineno)
    if t.lexer.verbose >= 2:
        print "p_primary_expression", t[0]


def p_primary_expression3(t):
    '''primary_expression :     FCONST'''
    t[0] = Token(t[1], 'float', t.lexer.lineno)
    if t.lexer.verbose >= 2:
        print "p_primary_expression", t[0]

def p_primary_expression4(t):
    '''primary_expression :     variable'''
    t[0] = t[1]
    if t.lexer.verbose >= 2:
        print "p_primary_expression", t[0]

    #print "mapping", t[1], t.lexer.type_map.get(t[1], None)
    #print "p_primary_expression", t[0]

# comment
#def p_comment(t):
#    '''comment : COMMENT'''
#    t[0] = '#' + t[1][2:] + '\n'

#def p_comment_block(t):
#    '''comment : COMMENT_BLOCK'''
#    t[0] = '"""%s"""' % t[1][2:-2] + '\n'


# types

def p_boolean_true(t):
    '''boolean : ON
                | TRUE
                | YES '''
    t[0] = 'True'
    if t.lexer.verbose >= 2:
        print "p_boolean_true", t[0]

def p_boolean_false(t):
    '''boolean : OFF
                | FALSE
                | NO '''
    t[0] = 'False'
    if t.lexer.verbose >= 2:
        print "p_boolean_false", t[0]

def p_variable(t):
    '''variable : VAR'''

    # TODO : resolve issue of global variables conflicting with reserved words
    # they will be suffixed with an underscore and won't be able to sync with
    # their mel equivalent

    t[1] = t[1].lstrip('$')
    if t[1] in pythonReservedWords:
        var = t[1] + '_'
    else:
        var = t[1]

    typ = t.lexer.type_map.get(var, None)

    if var in t.lexer.global_vars:
        t[0] = Token("%smelGlobals['%s']" % (t.lexer.pymel_namespace, var),
                     typ, t.lexer.lineno, globalVar=var)

    else:
        t[0] = Token(var, typ, t.lexer.lineno )

    if t.lexer.verbose >= 2:
        print "p_variable", t[0]

def p_variable_vector_component(t):
    '''variable :  VAR COMPONENT'''
    t[1] = t[1].lstrip('$')
    t[0] = Token(t[1]+t[2], 'float', t.lexer.lineno)
    if t.lexer.verbose >= 2:
        print "p_variable_vector_component", t[0]

# command_statement
# -- difference between a comamnd_statement and a command:
#        a command_statement is always followed by a semi-colon
#        a command_statement can receive a command_expression as input
def p_command_statement(t):
    '''command_statement : ID SEMI
            | ID command_statement_input_list SEMI'''

    if len(t) == 3:
        t[0] = format_command(t[1], [], t) + '\n'
    else:
        t[0] = format_command(t[1], t[2], t) + '\n'
    addComments(t)

def p_command_statement_input_list(t):
    '''command_statement_input_list : command_statement_input
                                      | command_statement_input_list command_statement_input'''
    #t[0] = assemble(t, 'p_command_input_list')

    if len(t)>2:
        if isinstance(t[2], list):
            t[0] = t[1] + t[2]
        #print "append"
        else:
            t[0] = t[1] + [t[2]]
    else:
        #print "new"
        if isinstance(t[1], list):
            t[0] = t[1]
        else:
            t[0] = [t[1]]


def p_command_statement_input(t):
    '''command_statement_input : unary_expression
                                | command_flag
                                  | command_expression'''
    t[0] = assemble(t, 'p_command_statement_input')

def p_command_statement_input_2(t):
    '''command_statement_input     : object_list'''
    t[0] =  map( lambda x: "'%s'" % x, t[1])

def p_command_statement_input_3(t):
    '''command_statement_input     : ELLIPSIS'''
    t[0] = Token( "'%s'" % t[1], None, t.lexer.lineno )

# command
# -- difference between a comamnd_statement and a command:
#        a command_statement is always followed by a semi-colon
#        a command_statement can receive a command_expression as input
def p_command(t):
    '''command : ID
                | ID command_input_list'''
    #print "p_command"
    if len(t) == 2:
        t[0] = format_command(t[1],[], t)
    else:
        t[0] = format_command(t[1], t[2], t)


def p_command_input_list(t):
    '''command_input_list : command_input
                          | command_input_list command_input'''
    #t[0] = assemble(t, 'p_command_input_list')

    #t[0] = ' '.join(t[1:])
    if len(t)>2:
        if isinstance(t[2], list):
            t[0] = t[1] + t[2]
        #print "append"
        else:
            t[0] = t[1] + [t[2]]
    else:
        #print "new"
        if isinstance(t[1], list):
            t[0] = t[1]
        else:
            t[0] = [t[1]]

def p_command_input(t):
    '''command_input : unary_expression
                      | command_flag'''
    t[0] = assemble(t, 'p_command_input')

def p_command_input_2(t):
    '''command_input     : object_list'''
    t[0] =  map( lambda x: "'%s'" % x, t[1])

def p_command_input_3(t):
    '''command_input     : ELLIPSIS'''
    t[0] = Token( "'%s'" % t[1], None, t.lexer.lineno )

def p_object_list(t):
    '''object_list : object
                   | object_list object'''
    #t[0] = assemble(t, 'p_command_input_list')

    #t[0] = ' '.join(t[1:])
    if len(t)>2:
        #print "append"
        # `myFunc foo[0].bar` and `myFunc foo[0] .bar` appear the same to the lexer
        # we must check whitespace, and join or split where necessary
        lastObj = t[1][-1]
        #print lastObj #, t[1][-1].lexspan[1]
        #print t[2], t[2].lexspan[0]+1
        if lastObj.lexspan[1]+1 == t[2].lexspan[0]:
            # same object: join together with last element in the list and add to list
            #print t[1][-1].lexspan[1]+1, t[2].lexspan[0]
            joinedToken = Token( lastObj + t[2],
                                    'string',
                                    lastObj.lineno,
                                    lexspan = [ lastObj.lexspan[0], t[2].lexspan[1] ] )
            t[0] = t[1][:-1] + [ joinedToken ]
        else:
            t[0] = t[1] + [ t[2] ]
        #print t[0][-2], t[0][-2].lexspan
        #print t[0][-1], t[0][-1].lexspan
    else:
        #print "new"
        t[0] = [t[1]]
    #print "result", t[0]

def p_object_1(t):
    '''object    : ID'''
    if t.lexer.verbose >= 1:
        print 'p_object_1', t[1]
    #print t[1], t.lexpos(1), len(t[1]), t.lexpos(1)+len(t[1])
    t[0] = Token( t[1], 'string', lexspan=(t.lexpos(1),t.lexpos(1)+len(t[1])-1 ) )
    #t[0] = assemble(t, 'p_object_1')

#def p_object_2(t):
#    '''object    : LOBJECT expression RBRACKET
#                | LOBJECT expression ROBJECT'''
#    t[0] = assemble(t, 'p_object_2')



def p_object_2(t):
    '''object    : ID LBRACKET expression RBRACKET'''
    #print t.lexpos(1), t.lexpos(2),t.lexpos(3),t.lexpos(4)
    if t.lexer.verbose >= 1:
        print 'p_object_2'
    t[0] = Token( t[1]+t[2]+t[3]+t[4], 'string', lexspan=(t.lexpos(1),t.lexpos(4) ) )
    #t[0] = assemble(t, 'p_object_2')

def p_flag(t):
    '''command_flag : MINUS ID
                    | MINUS BREAK
                    | MINUS CASE
                    | MINUS CONTINUE
                    | MINUS DEFAULT
                    | MINUS DO
                    | MINUS ELSE
                    | MINUS FALSE
                    | MINUS FLOAT
                    | MINUS FOR
                    | MINUS GLOBAL
                    | MINUS IF
                    | MINUS IN
                    | MINUS INT
                    | MINUS NO
                    | MINUS ON
                    | MINUS OFF
                    | MINUS PROC
                    | MINUS RETURN
                    | MINUS STRING
                    | MINUS SWITCH
                    | MINUS TRUE
                    | MINUS VECTOR
                    | MINUS WHILE
                    | MINUS YES
                    '''

    # TODO: find complete list
    flag = t[1] +  t[2]

    #t[0] = assemble(t, 'p_flag', '', [flag]  )
    t[0] = Token( flag, 'flag', t.lexer.lineno )


# Other
def p_empty(t):
    '''empty : '''
    t[0] = assemble(t, 'p_empty')

def _error(t):
    if t.lexer.verbose:
        print "Error parsing script, attempting to read forward and restart parser"
    while 1:
        tok = yacc.token()             # Get the next token
        if not tok or tok.type == 'RBRACE': break
    yacc.restart()

def p_error(t):
    if t is None:
        raise ValueError, 'script has no contents'

    if t.type == 'COMMENT':
        #print "Removing Comment", t.value
        # Just discard the token and tell the parser it's okay.
        comment = '#' + t.value[2:] + '\n'
        #if t.lexer.verbose:
        #print "queueing comment", comment
        t.lexer.comment_queue.append( comment )
        yacc.errok()
    elif t.type == 'COMMENT_BLOCK':
        comment = t.value[2:-2]

        if '"' in comment:
            comment = "'''" + comment + "'''\n"
        else:
            comment = '"""' + comment + '"""\n'
        #if t.lexer.verbose:
        #print "queueing comment", comment
        t.lexer.comment_queue.append( comment )
        yacc.errok()

    else:
        t.lexer.errors.append(t)
        #if t.lexer.verbose:
        #    print "Error parsing script at %s, attempting to read forward and restart parser" % t.value
        while 1:
            tok = yacc.token()             # Get the next token
            if not tok or tok.type == 'RBRACE': break
        yacc.restart()



#import profile
# Build the grammar

lexer = lex.lex(module=mellex)

_outputdir = tempfile.gettempdir()
parser = yacc.yacc(method='''LALR''', debug=0, outputdir=_outputdir )

class MelParseError(Exception):
    def __init__(self, *args, **kwargs):
        self.data = kwargs.pop('data', None)
        self.file = kwargs.pop('file', None)
        self.lexer = kwargs.pop('lexer', None)
        super(MelParseError, self).__init__(*args, **kwargs)

    def __str__(self):
        base = super(MelParseError, self).__str__()
        if self.file:
            base += " - Error parsing %s - check for syntax errors" % self.file
        if self.lexer and self.lexer.errors:
            base += "\n\nErrors:\n"
            for errToken in self.lexer.errors:
                base += "line %d (%s): %s\n" % (errToken.lineno, errToken.type, errToken.value)
        return base

class MelParser(object):
    """The MelParser class around which all other mel2py functions are based."""
    def build(self, rootModule = None, pymelNamespace='', verbosity=0,
              addPymelImport=True, expressionsOnly=False, forceCompatibility=True ):

        # data storage
        self.lexer = lexer.clone()
        self.lexer.proc_list = []  # ordered list of procedures
        self.lexer.local_procs = {} # dictionary of local procedures and their related data
        self.lexer.global_procs = {} # dictionary of global procedures and their related data
        self.lexer.imported_modules = set([])  # imported external modules, pymel is assumed
        self.lexer.global_vars = set([])
        self.lexer.spillover_pre = []  # some operations require a single line to be split.
        self.lexer.comment_queue = []
        self.lexer.comment_queue_hold = []
        self.lexer.type_map = {}
        self.lexer.global_var_include_regex = 'gv?[A-Z_].*'     # maya global vars usually begin with 'gv_' or a 'g' followed by a capital letter
        #parser.global_var_include_regex = '.*'
        self.lexer.global_var_exclude_regex = '$'
        #parser.global_var_exclude_regex = 'g_lm.*'        # Luma's global vars begin with 'g_lm' and should not be shared with the mel environment

        # options
        if pymelNamespace and not pymelNamespace.endswith( '.' ):
            pymelNamespace = pymelNamespace + '.'
        self.lexer.pymel_namespace = pymelNamespace
        self.lexer.root_module = rootModule #the name of the module that the hypothetical code is executing in. default is None (i.e. __main__ )
        self.lexer.verbose = verbosity
        self.add_pymel_import = addPymelImport
        self.lexer.force_compatibility = forceCompatibility
        self.lexer.expression_only = expressionsOnly
        self.lexer.errors = []

    def parse(self, data):
        data = data.decode( 'utf-8', 'ignore')
        #data = data.encode( 'utf-8', 'ignore')
        data = data.replace( '\r', '\n' )

        if self.lexer.verbose == 2:
            lex.input(data)
            while 1:
                tok = lex.token()
                if not tok: break      # No more input
                print tok

        prev_modules = self.lexer.imported_modules.copy()

        self.lexer.comment_queue = []
        self.lexer.comment_queue_hold = []

        translatedStr = ''
        try:
            debug = (self.lexer.verbose >= 3)
            translatedStr = parser.parse(data, lexer=self.lexer, debug=debug)
            #translatedStr = simpleParser.parse(data, lexer=self.lexer)

        except ValueError, msg:
            if self.lexer.comment_queue:
                translatedStr = '\n'.join(self.lexer.comment_queue)
            else:
                raise ValueError, msg

        if translatedStr is None:
            raise MelParseError(data=data, lexer=self.lexer)
        #except IndexError, msg:
        #    raise ValueError, '%s: %s' % (melfile, msg)
        #except AttributeError:
        #    raise ValueError, '%s: %s' % (melfile, "script has invalid contents")

        if not self.lexer.expression_only:
            new_modules = self.lexer.imported_modules.difference( prev_modules )

            header = ''

            # adding the pymel import statement should occur only on the
            # first execution of the parser or not at all.

            if self.add_pymel_import:
                if not self.lexer.pymel_namespace:
                    header += 'from pymel.all import *\n'
                elif self.lexer.pymel_namespace == 'pymel.':
                    header += 'import pymel.all as pymel\n'
                else:
                    header += 'import pymel.all as %s\n' % self.lexer.pymel_namespace[:-1]
                self.add_pymel_import = False

            if len( new_modules ):
                header += "import %s" % ','.join(list(new_modules))
                header += '\n'
            translatedStr = header + translatedStr


        return translatedStr

scanner = yacc.yacc(method='''LALR''', debug=0, module=melscan, outputdir=_outputdir)



#simple = SimpleMelGrammar()
#standard = MelGrammar()
#parser = standard.parser
#parser = simple.parser

class MelScanner(object):
    """The MelParser class around which all other mel2py functions are based."""
    def build(self):

        # data storage
        self.lexer = lexer.clone()
        self.lexer.proc_list = []  # ordered list of procedures
        self.lexer.local_procs = {} # dictionary of local procedures and their related data
        self.lexer.global_procs = {} # dictionary of global procedures and their related data
        self.lexer.global_vars = set([])


    def parse(self, data):
        data = data.decode('utf-8', 'ignore')
        #data = data.encode( 'utf-8', 'ignore')
        data = data.replace( '\r', '\n' )

        scanner.parse(data, lexer=self.lexer)
            #translatedStr = simpleParser.parse(data, lexer=self.lexer)


        return self.lexer.proc_list, self.lexer.global_procs, self.lexer.local_procs

#profile.run("yacc.yacc(method='''LALR''')")


