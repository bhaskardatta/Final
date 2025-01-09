from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import base64
from src.lexer import tokenize, symbol_table
from src.parser import parse_tokens
from src.utils.ast_visualizer import ASTVisualizer
from src.lexer.error_handler import error_handler

app = FastAPI()

# Allowed origins for CORS
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
    # Add any other origins you expect
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_ast_image(ast_root, output_path="data/ast_output.png"):
    """
    Generates a PNG image for the given AST and encodes it in Base64.
    """
    visualizer = ASTVisualizer()
    visualizer.visualize(ast_root, output_filename=output_path.split(".png")[0])

    with open(output_path, "rb") as img_file:
        return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

@app.post("/compile")
async def compile_code(request: dict):
    """
    Compile and process the submitted C code using Lexer and Parser.

    """
    error_handler.reset()  # Reset the error handler for fresh processing
    symbol_table.reset()  # Reset the symbol table

    try:
        # Retrieve the submitted code
        code = request.get("code", "")
        if not code:
            raise ValueError("No code provided.")

        # Save the code to a file for reference
        os.makedirs("data", exist_ok=True)
        code_path = "data/user_code.c"
        with open(code_path, "w") as file:
            file.write(code)

        # Step 1: Lexical Analysis
        tokens_list = tokenize(code)

        # Step 2: Syntax Analysis (Parsing)
        ast = parse_tokens(tokens_list)

        # Step 3: Collect Errors
        lexical_and_syntax_errors = error_handler.errors  # Get all errors so far
        success = not error_handler.has_errors()

        # Step 4: Generate AST Visualization (if no errors)
        ast_image = None
        if success and ast:
            ast_image = generate_ast_image(ast)

        # Step 5: Prepare Symbol Table (collected during tokenization)
        symbol_table_json = {
            name: symbol.to_dict() for name, symbol in symbol_table.symbols.items()
        }

        # Step 6: Return the response
        return {
            "success": success,
            "errors": [err.to_dict() for err in lexical_and_syntax_errors],
            "symbol_table": symbol_table_json,
            "ast_image": ast_image,
        }

    except Exception as e:
        print(f"Error during compilation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
