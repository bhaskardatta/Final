# src/lexer/tokenizer.py

import ply.lex as lex
from .symbol_table import SymbolTable
from .tokens import tokens, reserved  # Import both tokens and reserved
from .error_handler import error_handler

# Initialize the symbol table
symbol_table = SymbolTable()

# Regular expression rules for simple tokens
t_ASSIGN    = r'='
t_SEMICOLON = r';'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_LT        = r'<'
t_GT        = r'>'
t_LE        = r'<='
t_GE        = r'>='
t_EQ        = r'=='
t_NE        = r'!='
t_COMMA     = r','

# Reserved words
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
}

# Define token actions
def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    t.column = find_column(t.lexer.lexdata, t)  # Add column attribute
    symbol_table.add_symbol(t.value, t.type, t.lineno, t.column)
    return t

def t_preprocessor(t):
    r'\#.*'
    pass  # Ignore preprocessor directives

def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'  # Matches string literals with escape sequences
    t.value = t.value[1:-1]  # Strip surrounding quotes
    t.column = find_column(t.lexer.lexdata, t)
    return t


def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    t.column = find_column(t.lexer.lexdata, t)
    return t

def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    t.column = find_column(t.lexer.lexdata, t)
    return t

# Track newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters
t_ignore = ' \t'

# Comments
def t_comment_singleline(t):
    r'//.*'
    pass

def t_comment_multiline(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

# Error handling rule
def t_error(t):
    column = find_column(t.lexer.lexdata, t)
    error_handler.add_error('Lexical', f"Illegal character '{t.value[0]}'", t.lineno, column)
    t.lexer.skip(1)

# Compute column numbers
def find_column(input, token):
    """
    Compute the column number of a token.
    """
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return (token.lexpos - last_cr)

# Build the lexer
lexer = lex.lex()

def tokenize(data):
    """
    Tokenize the input data and return a list of tokens with column information.
    """
    lexer.input(data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tok.column = find_column(data, tok)  # Assign column number
        tokens_list.append(tok)
    return tokens_list
