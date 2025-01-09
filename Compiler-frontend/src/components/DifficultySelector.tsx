import React from 'react';
import { ToggleGroup, ToggleGroupItem } from '@/components/ui/toggle-group';

export type Difficulty = 'easy' | 'medium' | 'hard';

interface DifficultySelectorProps {
  difficulty: Difficulty;
  onDifficultyChange: (difficulty: Difficulty) => void;
}

const DifficultySelector: React.FC<DifficultySelectorProps> = ({
  difficulty,
  onDifficultyChange,
}) => {
  return (
    <div className="mb-6 text-center">
      <h2 className="text-sm sm:text-base font-retro text-[#e2c4ff] mb-3">
        Select Difficulty
      </h2>
      <ToggleGroup
        type="single"
        value={difficulty}
        onValueChange={(value) => value && onDifficultyChange(value as Difficulty)}
        className="border border-[#463a66] p-1 rounded-lg bg-[#1a1630] inline-flex shadow-[0_0_15px_rgba(226,196,255,0.1)]"
      >
        <ToggleGroupItem
          value="easy"
          className="relative px-6 py-2 font-retro text-xs transition-all duration-300
                   data-[state=on]:bg-[#7fffd4] data-[state=on]:text-[#1a1630]
                   data-[state=off]:text-[#e2c4ff] data-[state=off]:hover:bg-[#463a66]
                   rounded-md"
        >
          Easy
        </ToggleGroupItem>
        <ToggleGroupItem
          value="medium"
          className="relative px-6 py-2 font-retro text-xs transition-all duration-300
                   data-[state=on]:bg-[#ffeb3b] data-[state=on]:text-[#1a1630]
                   data-[state=off]:text-[#e2c4ff] data-[state=off]:hover:bg-[#463a66]
                   rounded-md"
        >
          Medium
        </ToggleGroupItem>
        <ToggleGroupItem
          value="hard"
          className="relative px-6 py-2 font-retro text-xs transition-all duration-300
                   data-[state=on]:bg-[#ff6b9d] data-[state=on]:text-white
                   data-[state=off]:text-[#e2c4ff] data-[state=off]:hover:bg-[#463a66]
                   rounded-md"
        >
          Hard
        </ToggleGroupItem>
      </ToggleGroup>
    </div>
  );
};

export default DifficultySelector; 