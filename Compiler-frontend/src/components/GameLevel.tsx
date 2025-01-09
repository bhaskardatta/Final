// src/components/GameLevel.tsx

import React from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { useToast } from '@/hooks/use-toast';
import { Textarea } from '@/components/ui/textarea';
import Confetti from 'react-confetti';
import { compileCode } from '@/services/api'; // Import the API service
import ErrorDisplay from '@/components/ErrorDisplay';
import SymbolTableDisplay from '@/components/SymbolTableDisplay';
import ASTDisplay from '@/components/ASTDisplay';

interface GameLevelProps {
  level: number;
  code: string;
  solution: string;
  hint: string;
  onComplete: () => void;
  theme: {
    primaryColor: string;
    secondaryColor: string;
    glowEffect: string;
    borderEffect: string;
    textGradient: string;
    cardBg: string;
    animation: string;
  };
}

interface CompilationError {
  type: string;
  message: string;
  line: number;
  column: number;
}

interface CompileResponse {
  success: boolean;
  errors: CompilationError[];
  symbol_table: SymbolTable;
  ast_image: string | null;
}

interface SymbolTable {
  [key: string]: {
    type: string;
    line: number;
    column: number;
  };
}

const GameLevel: React.FC<GameLevelProps> = ({ 
  level, 
  code, 
  solution, 
  hint, 
  onComplete,
  theme 
}) => {
  const [userCode, setUserCode] = React.useState(code);
  const [showHint, setShowHint] = React.useState(false);
  const [showConfetti, setShowConfetti] = React.useState(false);
  const [errors, setErrors] = React.useState<CompilationError[]>([]);
  const [symbolTable, setSymbolTable] = React.useState<SymbolTable>({});
  const [astImage, setAstImage] = React.useState<string | null>(null);
  const [isLoading, setIsLoading] = React.useState(false);
  const { toast } = useToast();
  const editorRef = React.useRef<HTMLTextAreaElement>(null);

  React.useEffect(() => {
    setUserCode(code);
    setShowHint(false);
    setShowConfetti(false);
    setErrors([]);
  }, [code, level]);

  const handleCodeChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const value = e.target.value;
    setUserCode(value);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      const start = e.currentTarget.selectionStart;
      const end = e.currentTarget.selectionEnd;
      const newValue = userCode.substring(0, start) + '  ' + userCode.substring(end);
      setUserCode(newValue);
      
      // Set cursor position after tab
      setTimeout(() => {
        if (editorRef.current) {
          editorRef.current.selectionStart = editorRef.current.selectionEnd = start + 2;
        }
      }, 0);
    }
  };
  
  const handleSubmit = async () => {
    setIsLoading(true);
    try {
      const response: CompileResponse = await compileCode(userCode);
      
      if (response.success) {
        if (level === 3) { // Assuming level 3 is the final level
          setShowConfetti(true);
          setTimeout(() => setShowConfetti(false), 5000);
        }
        toast({
          title: "Level Complete! 🎮",
          description: "Great job! You've fixed the syntax error!",
          className: `font-retro ${theme.textGradient}`,
        });
        onComplete();
      } else {
        setErrors(response.errors);
        toast({
          title: "Compilation Errors! ❌",
          description: "Please fix the highlighted errors and try again.",
          variant: "destructive",
          className: "font-retro",
        });
      }

      // Set symbol table and AST image regardless of success
      setSymbolTable(response.symbol_table);
      if (response.ast_image) {
        setAstImage(response.ast_image);
      }
    } catch (error: any) {
      toast({
        title: "Error!",
        description: error.message || "An unexpected error occurred.",
        variant: "destructive",
        className: "font-retro",
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {showConfetti && (
        <Confetti
          width={window.innerWidth}
          height={window.innerHeight}
          recycle={false}
          numberOfPieces={500}
          gravity={0.3}
        />
      )}
      
      <Card className={`p-4 sm:p-6 border-2 transition-all duration-300 
                     ${theme.cardBg} ${theme.borderEffect} ${theme.glowEffect}`}>
        <h2 className={`text-lg sm:text-xl font-retro mb-4 ${theme.textGradient}`}>
          Level {level}
        </h2>
        <div className="mb-4 relative">
          <div className="relative font-mono rounded-lg overflow-hidden">
            <Textarea
              ref={editorRef}
              value={userCode}
              onChange={handleCodeChange}
              onKeyDown={handleKeyDown}
              className={`w-full min-h-[200px] p-4 
                       font-mono text-base rounded-lg border-2 
                       focus:outline-none focus:ring-1 resize-none scrollbar-thin 
                       transition-all duration-300 bg-[#1a1a1a]
                       ${theme.primaryColor} ${theme.borderEffect}`}
              spellCheck="false"
              style={{
                fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
                lineHeight: '1.5',
                tabSize: '2',
              }}
              aria-label={`Code editor for Level ${level}`}
            />
            {/* Display error count badge */}
            {errors.length > 0 && (
              <div className="absolute top-0 right-0 bg-red-500 text-white p-1 rounded-bl-md text-xs font-bold">
                {errors.length} Error{errors.length > 1 ? 's' : ''}
              </div>
            )}
          </div>
        </div>
        <div className="flex flex-col sm:flex-row justify-between items-center gap-3 sm:gap-4">
          <Button
            onClick={() => setShowHint(!showHint)}
            variant="outline"
            className={`w-full sm:w-auto font-retro text-xs sm:text-sm px-6 py-2
                     hover:bg-opacity-10 transition-all duration-200 
                     ${theme.borderEffect} ${theme.secondaryColor}`}
            aria-pressed={showHint}
            aria-label={showHint ? "Hide Hint" : "Show Hint"}
          >
            {showHint ? "Hide Hint" : "Show Hint"}
          </Button>
          <Button
            onClick={handleSubmit}
            className={`w-full sm:w-auto font-retro text-xs sm:text-sm px-6 py-2
                     text-white transition-all duration-200 
                     hover:bg-opacity-90 ${theme.glowEffect}`}
            disabled={isLoading}
          >
            {isLoading ? "Submitting..." : "Submit"}
          </Button>
        </div>
        {showHint && (
          <div className={`mt-4 p-4 rounded-lg border animate-in slide-in-from-bottom duration-300 
                        transition-all ${theme.borderEffect} ${theme.secondaryColor} bg-opacity-10`}>
            <p className="font-retro text-sm">{hint}</p>
          </div>
        )}

        {/* Display Compilation Errors */}
        {errors.length > 0 && (
          <ErrorDisplay errors={errors} />
        )}
        
        {/* Show Symbol Table and AST for all levels */}
        {Object.keys(symbolTable).length > 0 && (
          <SymbolTableDisplay symbolTable={symbolTable} />
        )}
        
        {astImage && (
          <ASTDisplay astImage={astImage} />
        )}
      </Card>
    </>
  );
};

export default GameLevel;
