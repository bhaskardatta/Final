# # import json
# # import os

# # class Symbol:
# #     """Represents an identifier in the symbol table."""
# #     def __init__(self, name, token_type, lineno):
# #         self.name = name
# #         self.token_type = token_type
# #         self.lineno = lineno

# #     def __repr__(self):
# #         return f"Symbol(name='{self.name}', type='{self.token_type}', line={self.lineno})"

# #     def to_dict(self):
# #         """Converts the Symbol instance to a dictionary for JSON serialization."""
# #         return {
# #             "name": self.name,
# #             "type": self.token_type,
# #             "line": self.lineno
# #         }

# # class SymbolTable:
# #     """Stores symbols collected during lexical analysis."""
# #     def __init__(self):
# #         self.symbols = {}

# #     def add_symbol(self, name, token_type, lineno):
# #         if name not in self.symbols:
# #             self.symbols[name] = Symbol(name, token_type, lineno)
# #             print(f"Added to Symbol Table: {self.symbols[name]}")
# #         else:
# #             print(f"Symbol '{name}' already exists in the Symbol Table.")

# #     def display(self):
# #         print("\n--- Symbol Table ---")
# #         if not self.symbols:
# #             print("No symbols collected.")
# #         else:
# #             for symbol in self.symbols.values():
# #                 print(f"{symbol}")
# #         print("---------------------\n")

# #     def export_to_json(self, file_path):
# #         """Exports the symbol table to a JSON file."""
# #         # Create the directory if it does not exist
# #         directory = os.path.dirname(file_path)
# #         if not os.path.exists(directory):
# #             os.makedirs(directory)
        
# #         with open(file_path, 'w') as json_file:
# #             json.dump(
# #                 {name: symbol.to_dict() for name, symbol in self.symbols.items()},
# #                 json_file,
# #                 indent=4
# #             )
# #         print(f"Symbol table exported to {file_path}")



# # src/lexer/symbol_table.py

# import json
# import os

# class Symbol:
#     """Represents an identifier in the symbol table."""
#     def __init__(self, name, token_type, lineno, column):
#         self.name = name
#         self.token_type = token_type
#         self.lineno = lineno
#         self.column = column

#     def __repr__(self):
#         return f"Symbol(name='{self.name}', type='{self.token_type}', line={self.lineno}, column={self.column})"

#     def to_dict(self):
#         """Converts the Symbol instance to a dictionary for JSON serialization."""
#         return {
#             "name": self.name,
#             "type": self.token_type,
#             "line": self.lineno,
#             "column": self.column
#         }

# class SymbolTable:
#     """Stores symbols collected during lexical analysis."""
#     def __init__(self):
#         self.symbols = {}

#     def add_symbol(self, name, token_type, lineno, column):
#         if name not in self.symbols:
#             self.symbols[name] = Symbol(name, token_type, lineno, column)
#             print(f"Added to Symbol Table: {self.symbols[name]}")
#         else:
#             print(f"Symbol '{name}' already exists in the Symbol Table.")

#     def display(self):
#         print("\n--- Symbol Table ---")
#         if not self.symbols:
#             print("No symbols collected.")
#         else:
#             for symbol in self.symbols.values():
#                 print(f"{symbol}")
#         print("---------------------\n")

#     def export_to_json(self, file_path):
#         """Exports the symbol table to a JSON file."""
#         # Create the directory if it does not exist
#         directory = os.path.dirname(file_path)
#         if not os.path.exists(directory):
#             os.makedirs(directory)
        
#         with open(file_path, 'w') as json_file:
#             json.dump(
#                 {name: symbol.to_dict() for name, symbol in self.symbols.items()},
#                 json_file,
#                 indent=4
#             )
#         print(f"Symbol table exported to {file_path}")




# src/lexer/symbol_table.py

import json
import os

class Symbol:
    """Represents an identifier in the symbol table."""
    def __init__(self, name, token_type, lineno, column):
        self.name = name
        self.token_type = token_type
        self.lineno = lineno
        self.column = column

    def __repr__(self):
        return f"Symbol(name='{self.name}', type='{self.token_type}', line={self.lineno}, column={self.column})"

    def to_dict(self):
        """Converts the Symbol instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "type": self.token_type,
            "line": self.lineno,
            "column": self.column
        }

class SymbolTable:
    """Stores symbols collected during lexical analysis."""
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, token_type, lineno, column):
        if name not in self.symbols:
            self.symbols[name] = Symbol(name, token_type, lineno, column)
            print(f"Added to Symbol Table: {self.symbols[name]}")
        else:
            print(f"Symbol '{name}' already exists in the Symbol Table.")

    def display(self):
        print("\n--- Symbol Table ---")
        if not self.symbols:
            print("No symbols collected.")
        else:
            for symbol in self.symbols.values():
                print(f"{symbol}")
        print("---------------------\n")

    def export_to_json(self, file_path):
        """Exports the symbol table to a JSON file."""
        # Create the directory if it does not exist
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(file_path, 'w') as json_file:
            json.dump(
                {name: symbol.to_dict() for name, symbol in self.symbols.items()},
                json_file,
                indent=4
            )
        print(f"Symbol table exported to {file_path}")

    def reset(self):
        """Clear all symbols from the table."""
        self.symbols = {}
