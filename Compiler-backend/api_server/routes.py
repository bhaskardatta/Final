# api_server/routes.py

from fastapi import APIRouter, HTTPException
from .schemas import CompileRequest, CompileError, CompileResponse
import subprocess
import os
import uuid
import json
import base64

router = APIRouter()

@router.post("/compile", response_model=CompileResponse)
def compile_code(request: CompileRequest):
    """
    Compiles the submitted C code and returns the compilation results.
    """
    # Generate a unique filename for the submission
    unique_id = uuid.uuid4().hex
    code_filename = f"data/sample_c_codes/user_code_{unique_id}.c"

    # Save the submitted code to the unique file
    try:
        with open(code_filename, 'w') as f:
            f.write(request.code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save code: {str(e)}")

    # Define the output file
    output_file = "full_code.txt"

    # Run the compilation script
    try:
        # Ensure the script has execution permissions
        os.chmod("scripts/code.sh", 0o755)

        # Execute the compilation script
        subprocess.run(["./scripts/code.sh"], check=True)
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="Compilation process failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running compilation script: {str(e)}")

    # Read compilation errors
    errors_path = "data/errors.json"
    if os.path.exists(errors_path):
        try:
            with open(errors_path, 'r') as f:
                errors = json.load(f)
        except Exception as e:
            errors = [{"type": "System", "message": f"Failed to read errors.json: {str(e)}", "line": 0, "column": 0}]
    else:
        errors = []

    # Read symbol table
    symbol_table_path = "output/symbol_table.json"
    if os.path.exists(symbol_table_path):
        try:
            with open(symbol_table_path, 'r') as f:
                symbol_table = json.load(f)
        except Exception as e:
            symbol_table = {}
    else:
        symbol_table = {}

    # Read AST image and encode it in Base64
    ast_image_path = "ast_output.png"
    if os.path.exists(ast_image_path):
        try:
            with open(ast_image_path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            ast_image = f"data:image/png;base64,{encoded_string}"
        except Exception as e:
            ast_image = None
    else:
        ast_image = None

    # Determine success based on presence of errors
    success = len(errors) == 0

    # Cleanup: Remove the user-submitted code file
    try:
        os.remove(code_filename)
    except Exception as e:
        pass  # Optionally, log this exception

    return CompileResponse(
        success=success,
        errors=errors,
        symbol_table=symbol_table,
        ast_image=ast_image
    )
