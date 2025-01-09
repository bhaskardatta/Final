# src/utils/ast_visualizer.py

from graphviz import Digraph
from src.parser.ast_nodes import (
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


class ASTVisualizer:
    def __init__(self):
        self.dot = Digraph(comment='Abstract Syntax Tree')
        self.dot.attr('node', shape='box', style='filled', color='lightblue')

    def visualize(self, ast_root, output_filename='ast_output'):
        """
        Traverses the AST and generates a Graphviz graph.

        :param ast_root: The root node of the AST.
        :param output_filename: The base name for the output files (without extension).
        """
        self.visit(ast_root)
        try:
            self.dot.render(filename=output_filename, format='png', cleanup=True)
            print(f"AST visualization saved as {output_filename}.png")
        except Exception as e:
            print(f"Failed to render AST visualization: {e}")

    def visit(self, node, parent=None):
        """
        Recursively visits AST nodes and adds them to the graph.

        :param node: The current AST node.
        :param parent: The parent node in the AST.
        """
        if node is None:
            return

        # Add the current node to the graph
        label = node.get_label()
        self.dot.node(str(node.id), label)

        # If there's a parent, add an edge from parent to current node
        if parent is not None:
            self.dot.edge(str(parent.id), str(node.id))

        # Recursively visit child nodes based on node type
        if isinstance(node, Program):
            for decl in node.declarations:
                self.visit(decl, node)

        elif isinstance(node, FunctionDeclaration):
            for param in node.params:
                self.visit(param, node)
            self.visit(node.body, node)

        elif isinstance(node, VariableDeclaration):
            if node.initializer:
                self.visit(node.initializer, node)

        elif isinstance(node, IfStatement):
            self.visit(node.condition, node)
            self.visit(node.then_branch, node)
            if node.else_branch:
                self.visit(node.else_branch, node)

        elif isinstance(node, ReturnStatement):
            self.visit(node.expression, node)

        elif isinstance(node, BinaryOperation):
            self.visit(node.left, node)
            self.visit(node.right, node)

        elif isinstance(node, UnaryOperation):
            self.visit(node.operand, node)

        elif isinstance(node, FunctionCall):  # Add handling for FunctionCall
            self.visit(node.name, node)
            for arg in node.args:
                self.visit(arg, node)

        elif isinstance(node, Identifier):
            pass  # Leaf node

        elif isinstance(node, Literal):
            pass  # Leaf node

        elif isinstance(node, CompoundStatement):
            for stmt in node.statements:
                self.visit(stmt, node)

        else:
            print(f"Unhandled node type: {type(node).__name__}")
