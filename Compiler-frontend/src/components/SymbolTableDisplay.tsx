// src/components/SymbolTableDisplay.tsx

import React from 'react';

interface SymbolTableProps {
  symbolTable: Record<string, any>;
}

const SymbolTableDisplay: React.FC<SymbolTableProps> = ({ symbolTable }) => {
  const symbols = Object.entries(symbolTable);

  if (symbols.length === 0) {
    return null;
  }

  return (
    <div className="mt-4 p-4 rounded-lg border border-gray-500 bg-gray-50">
      <h3 className="font-bold text-gray-700">Symbol Table:</h3>
      <table className="min-w-full mt-2 table-auto text-sm">
        <thead>
          <tr>
            <th className="px-4 py-2 border">Name</th>
            <th className="px-4 py-2 border">Type</th>
            <th className="px-4 py-2 border">Line</th>
            <th className="px-4 py-2 border">Column</th>
          </tr>
        </thead>
        <tbody>
          {symbols.map(([name, details], index) => (
            <tr key={index} className="bg-white">
              <td className="px-4 py-2 border">{name}</td>
              <td className="px-4 py-2 border">{details.type}</td>
              <td className="px-4 py-2 border">{details.line}</td>
              <td className="px-4 py-2 border">{details.column}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SymbolTableDisplay;
