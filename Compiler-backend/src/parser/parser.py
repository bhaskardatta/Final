# src/parser/parser.py

import ply.yacc as yacc
from src.lexer.tokens import tokens  # Correct import for tokens
from src.lexer.error_handler import error_handler  # Correct import for error_handler
from src.parser.ast_nodes import (  # Import AST nodes
    Program,
    FunctionDeclaration,
    VariableDeclaration,
    IfStatement,
    ReturnStatement,
    BinaryOperation,
    UnaryOperation,
    FunctionCall,
    Identifier,
    Literal,
    CompoundStatement,
)


# Define precedence rules to resolve ambiguities
precedence = (
    ('left', 'EQ', 'NE'),              # Equality operators
    ('left', 'LT', 'LE', 'GT', 'GE'),   # Relational operators
    ('left', 'PLUS', 'MINUS'),         # Addition and subtraction
    ('left', 'MULTIPLY', 'DIVIDE'),    # Multiplication and division
    ('right', 'UMINUS'),               # Unary minus
)

# Dictionary to hold all AST nodes (optional, can be used for tracking)
ast_nodes = []

def p_program(p):
    """program : declarations"""
    p[0] = Program(p[1])
    ast_nodes.append(p[0])

def p_declarations(p):
    """declarations : declarations declaration
                    | declaration"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaration(p):
    """declaration : var_declaration
                   | func_declaration"""
    p[0] = p[1]

def p_var_declaration(p):
    """var_declaration : type_specifier IDENTIFIER SEMICOLON
                       | type_specifier IDENTIFIER ASSIGN expression SEMICOLON"""
    var_type = p[1]
    var_name = p[2]
    if len(p) == 4:
        initializer = None
    else:
        initializer = p[4]
    p[0] = VariableDeclaration(var_type=var_type, name=var_name, initializer=initializer)

def p_type_specifier(p):
    """type_specifier : INT
                      | FLOAT"""
    p[0] = p[1]

def p_func_declaration(p):
    """func_declaration : type_specifier IDENTIFIER LPAREN params RPAREN compound_stmt"""
    return_type = p[1]
    func_name = p[2]
    params = p[4]
    body = p[6]
    p[0] = FunctionDeclaration(return_type=return_type, name=func_name, params=params, body=body)

def p_params(p):
    """params : param_list
              | empty"""
    p[0] = p[1] if p[1] is not None else []

def p_param_list(p):
    """param_list : param_list COMMA param
                  | param"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_param(p):
    """param : type_specifier IDENTIFIER"""
    var_type = p[1]
    var_name = p[2]
    return VariableDeclaration(var_type=var_type, name=var_name)

def p_compound_stmt(p):
    """compound_stmt : LBRACE stmt_list RBRACE"""
    p[0] = CompoundStatement(statements=p[2])

def p_stmt_list(p):
    """stmt_list : stmt_list statement
                 | empty"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_statement(p):
    """statement : expr_stmt
                 | var_declaration
                 | compound_stmt
                 | if_stmt
                 | return_stmt"""
    p[0] = p[1]

def p_if_stmt(p):
    """if_stmt : IF LPAREN expression RPAREN statement
               | IF LPAREN expression RPAREN statement ELSE statement"""
    condition = p[3]
    then_branch = p[5]
    else_branch = p[7] if len(p) > 6 else None
    p[0] = IfStatement(condition=condition, then_branch=then_branch, else_branch=else_branch)

def p_return_stmt(p):
    """return_stmt : RETURN expression SEMICOLON"""
    expr = p[2]
    p[0] = ReturnStatement(expression=expr)

def p_expr_stmt(p):
    """expr_stmt : expression SEMICOLON"""
    p[0] = p[1]

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression"""
    left = p[1]
    operator = p[2]
    right = p[3]
    p[0] = BinaryOperation(left=left, operator=operator, right=right)

def p_expression_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    operand = p[2]
    p[0] = UnaryOperation(operator='-', operand=operand)

def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    """expression : INT_LITERAL
                  | FLOAT_LITERAL"""
    p[0] = Literal(value=p[1])

def p_expression_identifier(p):
    """expression : IDENTIFIER"""
    p[0] = Identifier(name=p[1])

def p_expression_call(p):
    """expression : IDENTIFIER LPAREN arg_list RPAREN"""
    p[0] = FunctionCall(name=Identifier(p[1]), args=p[3])

def p_arg_list(p):
    """arg_list : arg_list COMMA expression
                | expression
                | empty"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[0] = []

def p_empty(p):
    """empty :"""
    p[0] = None  # Explicitly set to None for clarity

# def p_error(p):
#     if p:
#         column = getattr(p, 'column', 'Unknown')  # Safely get 'column' attribute
#         print(f"Syntax error at token '{p.value}', line {p.lineno}, column {column}")
#     else:
#         print("Syntax error at EOF")

def p_error(p):
    if p:
        column = getattr(p, 'column', 'Unknown')  # Safely get 'column' attribute
        error_handler.add_error('Syntax', f"Syntax error at token '{p.value}'", p.lineno, column)
    else:
        error_handler.add_error('Syntax', "Syntax error at EOF", '?', '?')

def p_expression_string(p):
    """expression : STRING_LITERAL"""
    p[0] = Literal(value=p[1])

def p_preprocessor_directive(p):
    """preprocessor : """
    pass

# Build the parser
parser = yacc.yacc()

def parse_tokens(tokens_list):
    """
    Parse the list of tokens and return the AST.
    """
    from collections import deque

    token_queue = deque(tokens_list)

    class TokenLexer:
        def __init__(self, tokens):
            self.tokens = tokens

        def token(self):
            if self.tokens:
                return self.tokens.popleft()
            else:
                return None

    lexer = TokenLexer(token_queue)
    ast = parser.parse(lexer=lexer)
    return ast
