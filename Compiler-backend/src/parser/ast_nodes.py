# src/parser/ast_nodes.py

import itertools

class ASTNode:
    _id_iter = itertools.count()

    def __init__(self):
        self.id = next(ASTNode._id_iter)

    def get_label(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"{self.__class__.__name__}()"

class Program(ASTNode):
    def __init__(self, declarations):
        super().__init__()
        self.declarations = declarations

    def get_label(self):
        return "Program"

    def __repr__(self):
        return f"Program(declarations={self.declarations})"

class FunctionDeclaration(ASTNode):
    def __init__(self, return_type, name, params, body):
        super().__init__()
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body

    def get_label(self):
        return f"FunctionDeclaration\n{self.return_type} {self.name}"

    def __repr__(self):
        return f"FunctionDeclaration(return_type='{self.return_type}', name='{self.name}', params={self.params}, body={self.body})"

class VariableDeclaration(ASTNode):
    def __init__(self, var_type, name, initializer=None):
        super().__init__()
        self.var_type = var_type
        self.name = name
        self.initializer = initializer

    def get_label(self):
        if self.initializer:
            return f"VariableDeclaration\n{self.var_type} {self.name} = ..."
        return f"VariableDeclaration\n{self.var_type} {self.name}"

    def __repr__(self):
        return f"VariableDeclaration(var_type='{self.var_type}', name='{self.name}', initializer={self.initializer})"

class IfStatement(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        super().__init__()
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def get_label(self):
        return "IfStatement"

    def __repr__(self):
        return f"IfStatement(condition={self.condition}, then_branch={self.then_branch}, else_branch={self.else_branch})"

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def get_label(self):
        return "ReturnStatement"

    def __repr__(self):
        return f"ReturnStatement(expression={self.expression})"

class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right

    def get_label(self):
        return f"BinaryOperation\n'{self.operator}'"

    def __repr__(self):
        return f"BinaryOperation(left={self.left}, operator='{self.operator}', right={self.right})"

class UnaryOperation(ASTNode):
    def __init__(self, operator, operand):
        super().__init__()
        self.operator = operator
        self.operand = operand

    def get_label(self):
        return f"UnaryOperation\n'{self.operator}'"

    def __repr__(self):
        return f"UnaryOperation(operator='{self.operator}', operand={self.operand})"

class Identifier(ASTNode):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_label(self):
        return f"Identifier\n{self.name}"

    def __repr__(self):
        return f"Identifier(name='{self.name}')"

class Literal(ASTNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def get_label(self):
        return f"Literal\n{self.value}"

    def __repr__(self):
        return f"Literal(value={self.value})"

class CompoundStatement(ASTNode):
    def __init__(self, statements):
        super().__init__()
        self.statements = statements

    def get_label(self):
        return "CompoundStatement"

    def __repr__(self):
        return f"CompoundStatement(statements={self.statements})"

# class FunctionCall(ASTNode):
#     def __init__(self, name, args):
#         super().__init__()
#         self.name = name  # Should be an Identifier instance
#         self.args = args  # List of expressions

#     def get_label(self):
#         return f"FunctionCall\n{self.name.name}"

#     def __repr__(self):
#         return f"FunctionCall(name={self.name}, args={self.args})"

class FunctionCall(ASTNode):
    def __init__(self, name, args):
        super().__init__()
        self.name = name  # Should be an Identifier instance
        self.args = args  # List of expressions

    def get_label(self):
        return f"FunctionCall\n{self.name.name}"

    def __repr__(self):
        return f"FunctionCall(name={self.name}, args={self.args})"