#!/bin/bash

# Define the output file
output_file="full.txt"

# Clear the output file if it already exists
> "$output_file"

# List of files to concatenate
files=(
  "src/main.tsx"
  "src/pages/Index.tsx"
  "src/components/GameLevel.tsx"
  "src/components/GameProgress.tsx"
  "src/components/DifficultySelector.tsx"
  "src/contexts/ThemeContext.tsx"
  "src/data/levels.ts"
  "src/lib/utils.ts"
  "src/hooks/use-toast.ts"
  "src/components/ui/card.tsx"
  "src/components/ui/button.tsx"
  "src/components/ui/textarea.tsx"
  "src/components/ui/toggle.tsx"
  "src/components/ui/toggle-group.tsx"
  "tsconfig.json"
  "package.json"
)

# Loop through the files and append their content to the output file
for file in "${files[@]}"; do
  if [[ -f "$file" ]]; then
    echo -e "\n# Start of $file\n" >> "$output_file"
    cat "$file" >> "$output_file"
    echo -e "\n# End of $file\n" >> "$output_file"
  else
    echo "File not found: $file"
  fi
done

echo "All files have been concatenated into $output_file."
