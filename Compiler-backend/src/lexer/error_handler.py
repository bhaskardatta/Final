# src/lexer/error_handler.py

import json
import os

class CompilerError:
    """Represents a single error in the compiler."""
    def __init__(self, error_type, message, lineno, column):
        self.error_type = error_type  # 'Lexical', 'Syntax', 'Semantic', etc.
        self.message = message
        self.lineno = lineno
        self.column = column

    def to_dict(self):
        return {
            "type": self.error_type,
            "message": self.message,
            "line": self.lineno,
            "column": self.column
        }

class ErrorHandler:
    """Centralized error handling for the compiler."""
    def __init__(self):
        self.errors = []

    def add_error(self, error_type, message, lineno, column):
        """Record a new compiler error."""
        err = CompilerError(error_type, message, lineno, column)
        self.errors.append(err)
        # Print a concise message for immediate feedback
        print(f"{error_type} Error at line {lineno}, column {column}: {message}")

    def has_errors(self):
        return len(self.errors) > 0

    def display_errors(self):
        """Display all errors on the console."""
        if not self.errors:
            print("No errors found.")
            return

        print("\n--- Compilation Errors ---")
        for e in self.errors:
            print(f"{e.error_type} Error at line {e.lineno}, column {e.column}: {e.message}")
        print("--------------------------\n")

    def export_to_json(self, file_path='data/errors.json'):
        """Export errors to a JSON file for easier reference."""
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, 'w') as jf:
            json.dump([err.to_dict() for err in self.errors], jf, indent=4)
        print(f"Errors exported to {file_path}")

    def reset(self):
        """Reset all errors in the error handler."""
        self.errors = []


# Initialize the error handler
error_handler = ErrorHandler()
