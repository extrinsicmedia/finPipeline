"""
# ----------------------------------------------------------------------
# ctokens.py
#
# Token specifications for symbols in ANSI C and C++.  This file is
# meant to be used as a library in other tokenizers.
# ----------------------------------------------------------------------
"""

def t_COMMENT(t):
    """
    /\*(.|\n)*?\*/
    """

    pass


def t_CPPCOMMENT(t):
    """
    //.*\n
    """

    pass

t_AND = '&'

t_ANDEQUAL = '&='

t_ARROW = '->'

t_CHARACTER = r"(L)?\'([^\\\n]|(\\.))*?\'"

t_COLON = ':'

t_COMMA = ','

t_DECREMENT = '--'

t_DIVEQUAL = '/='

t_DIVIDE = '/'

t_ELLIPSIS = r'\.\.\.'

t_EQ = '=='

t_EQUALS = '='

t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_GE = '>='

t_GT = '>'

t_ID = '[A-Za-z_][A-Za-z0-9_]*'

t_INCREMENT = r'\+\+'

t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

t_LAND = '&&'

t_LBRACE = r'\{'

t_LBRACKET = r'\['

t_LE = '<='

t_LNOT = '!'

t_LOR = r'\|\|'

t_LPAREN = r'\('

t_LSHIFT = '<<'

t_LSHIFTEQUAL = '<<='

t_LT = '<'

t_MINUS = '-'

t_MINUSEQUAL = '-='

t_MODEQUAL = '%='

t_MODULO = '%'

t_NE = '!='

t_NOT = '~'

t_OR = r'\|'

t_OREQUAL = r'\|='

t_PERIOD = r'\.'

t_PLUS = r'\+'

t_PLUSEQUAL = r'\+='

t_RBRACE = r'\}'

t_RBRACKET = r'\]'

t_RPAREN = r'\)'

t_RSHIFT = '>>'

t_RSHIFTEQUAL = '>>='

t_SEMI = ';'

t_STRING = r'\"([^\\\n]|(\\.))*?\"'

t_TERNARY = r'\?'

t_TIMES = r'\*'

t_TIMESEQUAL = r'\*='

t_XOR = r'\^'

t_XOREQUAL = '^='

tokens = None
