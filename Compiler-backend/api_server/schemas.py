# api_server/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class CompileRequest(BaseModel):
    code: str

class CompileError(BaseModel):
    type: str
    message: str
    line: int
    column: int

class CompileResponse(BaseModel):
    success: bool
    errors: List[CompileError]
    symbol_table: dict
    ast_image: Optional[str]  # Base64-encoded image string
