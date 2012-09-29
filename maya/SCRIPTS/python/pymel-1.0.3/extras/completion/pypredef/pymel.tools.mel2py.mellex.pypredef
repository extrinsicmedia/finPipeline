"""
# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------
"""

import pymel.util.external.ply.lex as lex
import sys

def t_CAPTURE(t):
    """
    `
    """

    pass


def t_COMMENT(t):
    """
    //.*
    """

    pass


def t_COMMENT_BLOCK(t):
    """
    /\*(.|\n)*?\*/|/\*(.|\n)*?$
    """

    pass


def t_COMPONENT(t):
    """
    \.[xyz]
    """

    pass


def t_ELLIPSIS(t):
    """
    \.\.
    """

    pass


def t_ID(t):
    """
    ([|]?([:]?([.]?[A-Za-z_][\w]*)+)+)+?
    """

    pass


def t_LBRACKET(t):
    """
    \[
    """

    pass


def t_LPAREN(t):
    """
    \(
    """

    pass


def t_NEWLINE(t):
    """
    \n+|\r+
    """

    pass


def t_RBRACKET(t):
    """
    \]
    """

    pass


def t_RPAREN(t):
    """
    \)
    """

    pass


def t_SEMI(t):
    """
    ;
    """

    pass


def t_VAR(t):
    """
    \$[A-Za-z_][\w_]*
    """

    pass

id_state = None

r = 'YES'

reserved = None

reserved_map = None

suspend_depth = 0

t_COLON = ':'

t_COMMA = ','

t_CONDOP = r'\?'

t_CROSS = r'\^'

t_CROSSEQUAL = '^='

t_DIVEQUAL = '/='

t_DIVIDE = '/'

t_EQ = '=='

t_EQUALS = '='

t_FCONST = r'(((\d+\.)(\d+)?|(\d+)?(\.\d+))(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_GE = '>='

t_GT = '>'

t_ICONST = r'(0x[a-fA-F0-9]*)|\d+'

t_LAND = '&&'

t_LBRACE = r'\{'

t_LE = '<='

t_LOR = r'\|\|'

t_LT = '<'

t_LVEC = '<<'

t_MINUS = '-'

t_MINUSEQUAL = '-='

t_MINUSMINUS = '--'

t_MOD = '%'

t_MODEQUAL = '%='

t_NE = '!='

t_NOT = '!'

t_PLUS = r'\+'

t_PLUSEQUAL = r'\+='

t_PLUSPLUS = r'\+\+'

t_RBRACE = r'\}'

t_RVEC = '>>'

t_SCONST = r'"([^\\\n]|(\\.)|\\\n)*?"'

t_TIMES = r'\*'

t_TIMESEQUAL = r'\*='

t_ignore = ' \t\x0c'

tokens = None
