import pymel.core.animation as animation
import pymel.api as api
import __builtin__ as builtin_module
import maya.cmds as cmds
import pymel.core.context as context
import pymel.core.datatypes as datatypes
import pymel.core.datatypes as dt
import pymel.core.effects as effects
import pymel.internal.factories as factories
import functools
import pymel.core.general as general
import inspect
import itertools
import pymel.core.language as language
import pymel.util.external.ply.lex as lex
import logging
import mellex
import melscan
import pymel.core.modeling as modeling
import pymel.core.nodetypes as nodetypes
import pymel.core.nodetypes as nt
import os
import pymel.core.other as other
import pymel
import re
import pymel.core.rendering as rendering
import pymel.core.runtime as runtime
import string
import sys
import pymel.core.system as system
import tempfile
import traceback
import pymel.core.uitypes as ui
import pymel.core.uitypes as uitypes
import pymel.util as util
import pymel.versions as versions
import warnings
import pymel.core.windows as windows
import pymel.util.external.ply.yacc as yacc

from pymel.core.general import *
from pymel.util.utilitytypes import *
from pymel.util.external.ply.yacc import *
from pymel.util.scanf import *
from pymel.core.other import *
from pymel.core.uitypes import *
from pymel.util.path import *
from pymel.core.context import *
from maya._OpenMaya import *
from pymel.core.modeling import *
from pymel.core.rendering import *
from pymel.internal.pwarnings import *
from pymel.core.animation import *
from pymel.util.external.ply.lex import *
from pymel.core.effects import *
from pymel.core.windows import *
from pymel.core.system import *
from pymel.util.decoration import *
from pymel.core.language import *
from pymel.util.common import *
from pymel.internal.pmcmds import *

class Token(str):
    def __add__(self, other):
        pass
    
    
    def __getslice__(self, start, end):
        pass
    
    
    def __new__(cls, val, type, lineno=None, **kwargs):
        pass
    
    
    __dict__ = None


class MelScanner(object):
    """
    The MelParser class around which all other mel2py functions are based.
    """
    
    
    
    def build(self):
        pass
    
    
    def parse(self, data):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class BatchData(object):
    def __init__(self, **kwargs):
        pass
    
    
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
    
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class MelParser(object):
    """
    The MelParser class around which all other mel2py functions are based.
    """
    
    
    
    def build(self, rootModule=None, pymelNamespace='', verbosity=0, addPymelImport=True, expressionsOnly=False, forceCompatibility=True):
        pass
    
    
    def parse(self, data):
        pass
    
    
    __dict__ = None
    
    __weakref__ = None


class MelParseError(builtin_module.Exception):
    def __init__(self, *args, **kwargs):
        pass
    
    
    def __str__(self):
        pass
    
    
    __weakref__ = None

def addComments(t, funcname=''):
    pass


def addHeldComments(t, funcname=''):
    pass


def addHeldComments2(code, t, funcname=''):
    pass


def assemble(t, funcname, separator='', tokens=None, matchFormatting=False):
    pass


def entabLines(line):
    pass


def fileInlist(file, fileList):
    """
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
    """

    pass


def findModule(moduleName):
    pass


def format_assignment_value(val, typ):
    """
    when assigning a value in mel, values will be auto-cast to the type of the variable, but in python, the variable
    will simply become the new type.  to ensure that the python operates as in mel, we need to cast when assigning
    a value to a variable of a different type
    """

    pass


def format_command(command, args, t):
    pass


def format_fopen(x, t):
    pass


def format_fread(x, t):
    pass


def format_source(x, t):
    pass


def format_substring(x, t):
    """
    convert:
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

    pass


def format_tokenize(x, t):
    pass


def format_tokenize_size(tokenized, sizeVar):
    """
    tokenize fix:
    tokenize passes a buffer by reference, and returns a size.
    we must return a list, and compute the size as a second operation::
    
        int $size = `tokenize "foo bar", $buffer, " "`;
    
        buffer = "foo bar".split(' ')
        size = len(buffer)
    """

    pass


def getModuleBasename(script):
    pass


def holdComments():
    pass


def merge_assignment_spillover(t, curr_lineno, title=''):
    pass


def p_add_comment(t):
    """
    add_comment :
    """

    pass


def p_additive_expression(t):
    """
    additive_expression : multiplicative_expression
    | additive_expression PLUS multiplicative_expression
    | additive_expression MINUS multiplicative_expression
    """

    pass


def p_assignment_expression(t):
    """
    assignment_expression : equality_expression
    | postfix_expression assignment_operator assignment_expression
    """

    pass


def p_assignment_operator(t):
    """
    assignment_operator : EQUALS
                        | TIMESEQUAL
                        | DIVEQUAL
                        | MODEQUAL
                        | PLUSEQUAL
                        | MINUSEQUAL
                        | CROSSEQUAL
    """

    pass


def p_boolean_false(t):
    """
    boolean : OFF
    | FALSE
    | NO
    """

    pass


def p_boolean_true(t):
    """
    boolean : ON
    | TRUE
    | YES
    """

    pass


def p_cast_expression(t):
    """
    cast_expression : unary_expression
    | unary_command_expression
    | type_specifier LPAREN expression RPAREN
    | LPAREN type_specifier RPAREN cast_expression
    """

    pass


def p_command(t):
    """
    command : ID
    | ID command_input_list
    """

    pass


def p_command_expression(t):
    """
    command_expression : CAPTURE command CAPTURE
    """

    pass


def p_command_input(t):
    """
    command_input : unary_expression
    | command_flag
    """

    pass


def p_command_input_2(t):
    """
    command_input     : object_list
    """

    pass


def p_command_input_3(t):
    """
    command_input     : ELLIPSIS
    """

    pass


def p_command_input_list(t):
    """
    command_input_list : command_input
    | command_input_list command_input
    """

    pass


def p_command_statement(t):
    """
    command_statement : ID SEMI
    | ID command_statement_input_list SEMI
    """

    pass


def p_command_statement_input(t):
    """
    command_statement_input : unary_expression
    | command_flag
      | command_expression
    """

    pass


def p_command_statement_input_2(t):
    """
    command_statement_input     : object_list
    """

    pass


def p_command_statement_input_3(t):
    """
    command_statement_input     : ELLIPSIS
    """

    pass


def p_command_statement_input_list(t):
    """
    command_statement_input_list : command_statement_input
    | command_statement_input_list command_statement_input
    """

    pass


def p_compound_statement(t):
    """
    compound_statement   : LBRACE statement_list RBRACE
    | LBRACE RBRACE
    """

    pass


def p_conditional_expression_1(t):
    """
    conditional_expression : logical_or_expression
    """

    pass


def p_conditional_expression_2(t):
    """
    conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression
    """

    pass


def p_constant_expression(t):
    """
    constant_expression : conditional_expression
    """

    pass


def p_constant_expression_opt_1(t):
    """
    constant_expression_opt : empty
    """

    pass


def p_constant_expression_opt_2(t):
    """
    constant_expression_opt : constant_expression
    """

    pass


def p_declaration_specifiers(t):
    """
    declaration_specifiers : type_specifier
    | GLOBAL type_specifier
    """

    pass


def p_declaration_statement(t):
    """
    declaration_statement : declaration_specifiers init_declarator_list SEMI
    """

    pass


def p_declarator(t):
    """
    declarator : variable
    | declarator LBRACKET constant_expression_opt RBRACKET
    """

    pass


def p_empty(t):
    """
    empty :
    """

    pass


def p_equality_expression_1(t):
    """
    equality_expression : relational_expression
    | equality_expression EQ relational_expression
    | equality_expression NE relational_expression
    """

    pass


def p_error(t):
    pass


def p_expression(t):
    """
    expression : conditional_expression
    """

    pass


def p_expression_list(t):
    """
    expression_list : expression
    | expression_list COMMA expression
    """

    pass


def p_expression_list_opt(t):
    """
    expression_list_opt : expression_list
    | empty
    """

    pass


def p_expression_opt(t):
    """
    expression_opt : empty
    | expression
    """

    pass


def p_expression_statement(t):
    """
    expression_statement : expression_opt SEMI
    """

    pass


def p_external_declaration(t):
    """
    external_declaration : statement
    | function_definition
    """

    pass


def p_flag(t):
    """
    command_flag : MINUS ID
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
    """

    pass


def p_function_arg(t):
    """
    function_arg : type_specifier variable
    | type_specifier variable LBRACKET RBRACKET
    """

    pass


def p_function_arg_list(t):
    """
    function_arg_list : function_arg
    | function_arg_list COMMA function_arg
    """

    pass


def p_function_arg_list_opt(t):
    """
    function_arg_list_opt : function_arg_list
    |  empty
    """

    pass


def p_function_declarator(t):
    """
    function_declarator : GLOBAL PROC
    | PROC
    """

    pass


def p_function_definition(t):
    """
    function_definition :  function_declarator function_specifiers_opt ID seen_func LPAREN function_arg_list_opt RPAREN add_comment compound_statement
    """

    pass


def p_function_specifiers_opt(t):
    """
    function_specifiers_opt : type_specifier
    | type_specifier LBRACKET RBRACKET
    | empty
    """

    pass


def p_init_declarator(t):
    """
    init_declarator : declarator
    | declarator EQUALS expression
    """

    pass


def p_init_declarator_list(t):
    """
    init_declarator_list : init_declarator
    | init_declarator_list COMMA init_declarator
    """

    pass


def p_iteration_statement_1(t):
    """
    iteration_statement : WHILE LPAREN expression RPAREN add_comment statement
    """

    pass


def p_iteration_statement_2(t):
    """
    iteration_statement : FOR LPAREN expression_list_opt SEMI expression_list_opt SEMI expression_list_opt RPAREN add_comment statement
    """

    pass


def p_iteration_statement_3(t):
    """
    iteration_statement : FOR LPAREN variable IN expression seen_FOR RPAREN add_comment statement
    """

    pass


def p_iteration_statement_4(t):
    """
    iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMI
    """

    pass


def p_jump_statement(t):
    """
    jump_statement : CONTINUE SEMI
    | BREAK SEMI
    | RETURN expression_opt SEMI
    """

    pass


def p_labeled_statement_2(t):
    """
    labeled_statement : CASE constant_expression COLON statement_list_opt
    """

    pass


def p_labeled_statement_3(t):
    """
    labeled_statement : DEFAULT COLON statement_list_opt
    """

    pass


def p_labeled_statement_list(t):
    """
    labeled_statement_list : labeled_statement
    | labeled_statement_list labeled_statement
    """

    pass


def p_logical_and_expression_1(t):
    """
    logical_and_expression : assignment_expression
    | logical_and_expression LAND assignment_expression
    """

    pass


def p_logical_or_expression_1(t):
    """
    logical_or_expression : logical_and_expression
    | logical_or_expression LOR logical_and_expression
    """

    pass


def p_multiplicative_expression(t):
    """
    multiplicative_expression : cast_expression
    | multiplicative_expression TIMES cast_expression
    | multiplicative_expression DIVIDE cast_expression
    | multiplicative_expression MOD cast_expression
    | multiplicative_expression CROSS cast_expression
    """

    pass


def p_object_1(t):
    """
    object    : ID
    """

    pass


def p_object_2(t):
    """
    object    : ID LBRACKET expression RBRACKET
    """

    pass


def p_object_list(t):
    """
    object_list : object
    | object_list object
    """

    pass


def p_postfix_expression(t):
    """
    postfix_expression : primary_expression
    | postfix_expression PLUSPLUS
    | postfix_expression MINUSMINUS
    """

    pass


def p_postfix_expression_2(t):
    """
    postfix_expression : LBRACE expression_list_opt RBRACE
    """

    pass


def p_postfix_expression_3(t):
    """
    postfix_expression : LVEC expression_list RVEC
    """

    pass


def p_postfix_expression_4(t):
    """
    postfix_expression : postfix_expression LBRACKET expression RBRACKET
    """

    pass


def p_primary_expression(t):
    """
    primary_expression :    boolean
    """

    pass


def p_primary_expression1(t):
    """
    primary_expression :     ICONST
    """

    pass


def p_primary_expression2(t):
    """
    primary_expression :     SCONST
    """

    pass


def p_primary_expression3(t):
    """
    primary_expression :     FCONST
    """

    pass


def p_primary_expression4(t):
    """
    primary_expression :     variable
    """

    pass


def p_primary_expression_paren(t):
    """
    primary_expression :    LPAREN expression RPAREN
    """

    pass


def p_procedure(t):
    """
    procedure : ID LPAREN procedure_expression_list RPAREN
    | ID LPAREN RPAREN
    """

    pass


def p_procedure_expression(t):
    """
    procedure_expression : command_expression
    | procedure
    """

    pass


def p_procedure_expression_list(t):
    """
    procedure_expression_list : constant_expression
    | procedure_expression_list COMMA constant_expression
    """

    pass


def p_relational_expression_1(t):
    """
    relational_expression : shift_expression
    | relational_expression LT shift_expression
    | relational_expression GT shift_expression
    | relational_expression LE shift_expression
    | relational_expression GE shift_expression
    """

    pass


def p_seen_FOR(t):
    """
    seen_FOR :
    """

    pass


def p_seen_func(t):
    """
    seen_func :
    """

    pass


def p_selection_statement_1(t):
    """
    selection_statement : IF LPAREN expression RPAREN statement
    """

    pass


def p_selection_statement_2(t):
    """
    selection_statement : IF LPAREN expression RPAREN statement ELSE add_comment statement
    """

    pass


def p_selection_statement_3(t):
    """
    selection_statement : SWITCH LPAREN expression RPAREN add_comment LBRACE labeled_statement_list RBRACE
    """

    pass


def p_shift_expression(t):
    """
    shift_expression : additive_expression
    """

    pass


def p_statement_complex(t):
    """
    statement : selection_statement
    | iteration_statement
    | jump_statement
    | declaration_statement
    """

    pass


def p_statement_expr(t):
    """
    statement : expression_statement
    | command_statement
    | compound_statement
    """

    pass


def p_statement_list(t):
    """
    statement_list   : statement
    | statement_list statement
    """

    pass


def p_statement_list_opt(t):
    """
    statement_list_opt : statement_list
    | empty
    """

    pass


def p_translation_unit(t):
    """
    translation_unit : external_declaration
    | translation_unit external_declaration
    """

    pass


def p_type_specifier(t):
    """
    type_specifier : INT
    | FLOAT
    | STRING
    | VECTOR
    | MATRIX
    """

    pass


def p_unary_command_expression(t):
    """
    unary_command_expression : procedure_expression
    | unary_operator procedure_expression
    """

    pass


def p_unary_expression(t):
    """
    unary_expression : postfix_expression
    | unary_operator cast_expression
    """

    pass


def p_unary_expression_2(t):
    """
    unary_expression : PLUSPLUS unary_expression
    | MINUSMINUS unary_expression
    """

    pass


def p_unary_operator(t):
    """
    unary_operator : PLUS
    | MINUS
    | NOT
    """

    pass


def p_variable(t):
    """
    variable : VAR
    """

    pass


def p_variable_vector_component(t):
    """
    variable :  VAR COMPONENT
    """

    pass


def pythonizeName(name):
    pass


def store_assignment_spillover(token, t):
    pass


def toList(t):
    pass


def vprint(t, *args):
    pass

MELTYPES = None

SCENE = None

batchData = None

catch = None

contstraintCmdName = 'tangentConstraint'

deprecated_str_methods = None

env = None

fileInfo = None

filteredCmds = None

lexer = None

mel = None

melCmdFlagList = None

melCmdList = None

melGlobals = None

mel_type_to_python_type = None

optionVar = None

parser = None

proc_remap = None

pythonReservedWords = None

reserved = None

scanner = None

scriptTableCmds = None

tag = '# script created by pymel.tools.mel2py'

thisModuleCmd = "import pymel.core.windows; import sys; sys.modules['pymel.core.windows']"

tokens = None

with_statement = None

workspace = None

x = 'whatIs'
