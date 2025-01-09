// src/components/ASTDisplay.tsx

import React from 'react';

interface ASTDisplayProps {
  astImage: string;
}

const ASTDisplay: React.FC<ASTDisplayProps> = ({ astImage }) => {
  return (
    <div className="mt-4 p-4 rounded-lg border border-blue-500 bg-blue-50">
      <h3 className="font-bold text-blue-700">Abstract Syntax Tree (AST):</h3>
      <img src={astImage} alt="AST Visualization" className="mt-2 w-full h-auto rounded-md" />
    </div>
  );
};

export default ASTDisplay;
