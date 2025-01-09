#!/bin/bash

# Define the directory where your project is located
PROJECT_DIR="/mnt/c/Users/chait/OneDrive/Documents/Projects/Compiler/trial3/back"

# Define the output file
OUTPUT_FILE="full_code.txt"

# Navigate to the project directory
cd "$PROJECT_DIR" || exit

# Find and concatenate all code files into the output file
find . \( -name "*.py" -o -name "*.c" -o -name "*.sh" \) -exec cat {} + > "$OUTPUT_FILE"

# Perform lexical analysis and syntax analysis
python3 src/main.py "$OUTPUT_FILE"

# Confirm completion
echo "All code has been concatenated and analyzed into $OUTPUT_FILE"
