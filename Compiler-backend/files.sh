#!/bin/bash

# Create top-level files
touch README.md LICENSE requirements.txt setup.py .gitignore

# Create directories and subdirectories
mkdir -p docs src/config src/lexer src/parser src/analyzer src/utils src/api tests/test_lexer tests/test_parser tests/test_analyzer tests/test_utils scripts data/sample_c_codes

# Create files in docs
touch docs/architecture.md docs/user_guide.md docs/api_reference.md

# Create files in src
touch src/__init__.py src/main.py
touch src/config/__init__.py src/config/settings.py
touch src/lexer/__init__.py src/lexer/tokenizer.py src/lexer/tokens.py
touch src/parser/__init__.py src/parser/ast_nodes.py src/parser/parser.py src/parser/grammar.py
touch src/analyzer/__init__.py src/analyzer/semantic_analyzer.py src/analyzer/symbol_table.py
touch src/utils/__init__.py src/utils/logger.py src/utils/helpers.py
touch src/api/__init__.py src/api/endpoints.py src/api/schemas.py

# Create files in tests
touch tests/__init__.py
touch tests/test_lexer/__init__.py tests/test_lexer/test_tokenizer.py
touch tests/test_parser/__init__.py tests/test_parser/test_parser.py
touch tests/test_analyzer/__init__.py tests/test_analyzer/test_semantic_analyzer.py
touch tests/test_utils/__init__.py tests/test_utils/test_helpers.py

# Create files in scripts
touch scripts/build.sh scripts/run_tests.sh

# Create sample C code files in data/sample_c_codes
touch data/sample_c_codes/example1.c data/sample_c_codes/example2.c

echo "File structure created successfully."
