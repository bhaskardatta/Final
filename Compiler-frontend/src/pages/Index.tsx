import React from 'react';
import GameLevel from '@/components/GameLevel';
import GameProgress from '@/components/GameProgress';
import DifficultySelector, { Difficulty } from '@/components/DifficultySelector';
import { LEVELS } from '@/data/levels';
import { ThemeProvider, useTheme } from '@/contexts/ThemeContext';

const GameContent = () => {
  const theme = useTheme();
  const [currentLevel, setCurrentLevel] = React.useState(1);
  const [difficulty, setDifficulty] = React.useState<Difficulty>('easy');
  
  const currentLevels = LEVELS[difficulty];
  
  const handleLevelComplete = () => {
    if (currentLevel < currentLevels.length) {
      setCurrentLevel(prev => prev + 1);
    }
  };

  const handleDifficultyChange = (newDifficulty: Difficulty) => {
    setDifficulty(newDifficulty);
    setCurrentLevel(1);
  };

  return (
    <div className={`min-h-screen px-4 py-6 sm:p-8 transition-colors duration-500 ${theme.bgColor}`}>
      <div className="max-w-2xl mx-auto">
        <h1 className={`text-xl sm:text-3xl font-retro mb-8 text-center ${theme.textGradient}`}>
          C-Syntax Adventure
        </h1>
        
        <DifficultySelector 
          difficulty={difficulty}
          onDifficultyChange={handleDifficultyChange}
        />
        
        <GameProgress 
          currentLevel={currentLevel} 
          totalLevels={currentLevels.length}
          theme={theme}
        />
        
        <GameLevel
          level={currentLevel}
          code={currentLevels[currentLevel - 1].code}
          solution={currentLevels[currentLevel - 1].solution}
          hint={currentLevels[currentLevel - 1].hint}
          onComplete={handleLevelComplete}
          theme={theme}
        />
        
        <div className="mt-6 text-center">
          <p className={`text-xs sm:text-sm font-retro ${theme.secondaryColor}`}>
            {currentLevel === currentLevels.length ? (
              "🎮 You've completed all levels in this difficulty! Try a harder mode! 🏆"
            ) : (
              "Fix the syntax errors to advance to the next level!"
            )}
          </p>
        </div>
      </div>
    </div>
  );
};

const Index = () => {
  const [difficulty, setDifficulty] = React.useState<Difficulty>('easy');

  return (
    <ThemeProvider difficulty={difficulty}>
      <GameContent />
    </ThemeProvider>
  );
};

export default Index;