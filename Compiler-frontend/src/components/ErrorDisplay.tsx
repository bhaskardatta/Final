// src/components/ErrorDisplay.tsx

import React from 'react';

interface CompilationError {
  type: string;
  message: string;
  line: number;
  column: number;
}

interface ErrorDisplayProps {
  errors: CompilationError[];
}

const ErrorDisplay: React.FC<ErrorDisplayProps> = ({ errors }) => {
  return (
    <div className="mt-4 p-4 rounded-lg border border-red-500 bg-red-50">
      <h3 className="font-bold text-red-700">Compilation Errors:</h3>
      <ul className="list-disc list-inside mt-2 text-red-600">
        {errors.map((error, index) => (
          <li key={index}>
            <strong>{error.type} Error</strong> at line {error.line}, column {error.column}: {error.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ErrorDisplay;
