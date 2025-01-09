import React from 'react';

interface GameProgressProps {
  currentLevel: number;
  totalLevels: number;
  theme: {
    primaryColor: string;
    secondaryColor: string;
    glowEffect: string;
    borderEffect: string;
    textGradient: string;
  };
}

const GameProgress: React.FC<GameProgressProps> = ({ currentLevel, totalLevels, theme }) => {
  const completedLevels = currentLevel - 1;
  const isAllComplete = completedLevels === totalLevels;
  const progress = isAllComplete ? 100 : (completedLevels / totalLevels) * 100;

  return (
    <div className="w-full max-w-md mx-auto mb-8">
      <div className="p-4 rounded-lg border border-[#463a66] bg-[#1a1630] shadow-[0_0_15px_rgba(226,196,255,0.1)]">
        <div className="flex justify-between mb-3">
          <span className="font-retro text-sm text-[#e2c4ff]">
            {isAllComplete ? "All Levels Complete!" : `Level ${currentLevel}`}
          </span>
          <span className="font-retro text-sm text-[#e2c4ff]">
            {isAllComplete ? "Completed" : `${Math.round(progress)}%`}
          </span>
        </div>
        <div className="relative h-2.5 rounded-full overflow-hidden bg-[#463a66]">
          <div
            className="absolute top-0 left-0 h-full transition-all duration-500 ease-out bg-current"
            style={{ 
              width: `${progress}%`,
              backgroundColor: isAllComplete ? '#7fffd4' : '#ffeb3b'
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default GameProgress;