import React, { createContext, useContext } from 'react';
import { Difficulty } from '@/components/DifficultySelector';

interface ThemeContextType {
  bgColor: string;
  primaryColor: string;
  secondaryColor: string;
  glowEffect: string;
  borderEffect: string;
  textGradient: string;
  cardBg: string;
  animation: string;
}

const themesByDifficulty: Record<Difficulty, ThemeContextType> = {
  easy: {
    bgColor: 'bg-[#0f0720]',
    primaryColor: 'text-[#7fffd4]',
    secondaryColor: 'text-[#e2c4ff]',
    glowEffect: 'shadow-[0_0_15px_rgba(127,255,212,0.15)]',
    borderEffect: 'border-[#463a66] border-opacity-80',
    textGradient: 'bg-gradient-to-r from-[#7fffd4] to-[#e2c4ff] text-transparent bg-clip-text',
    cardBg: 'bg-[#1a1630]',
    animation: 'animate-none',
  },
  medium: {
    bgColor: 'bg-[#0f0720]',
    primaryColor: 'text-[#ffeb3b]',
    secondaryColor: 'text-[#e2c4ff]',
    glowEffect: 'shadow-[0_0_15px_rgba(255,235,59,0.15)]',
    borderEffect: 'border-[#463a66] border-opacity-80',
    textGradient: 'bg-gradient-to-r from-[#ffeb3b] to-[#e2c4ff] text-transparent bg-clip-text',
    cardBg: 'bg-[#1a1630]',
    animation: 'animate-none',
  },
  hard: {
    bgColor: 'bg-[#0f0720]',
    primaryColor: 'text-[#ff6b9d]',
    secondaryColor: 'text-[#e2c4ff]',
    glowEffect: 'shadow-[0_0_15px_rgba(255,107,157,0.15)]',
    borderEffect: 'border-[#463a66] border-opacity-80',
    textGradient: 'bg-gradient-to-r from-[#ff6b9d] to-[#e2c4ff] text-transparent bg-clip-text',
    cardBg: 'bg-[#1a1630]',
    animation: 'animate-none',
  },
};

const ThemeContext = createContext<ThemeContextType>(themesByDifficulty.easy);

export const useTheme = () => useContext(ThemeContext);

export const ThemeProvider: React.FC<{
  difficulty: Difficulty;
  children: React.ReactNode;
}> = ({ difficulty, children }) => {
  const theme = themesByDifficulty[difficulty];

  return (
    <ThemeContext.Provider value={theme}>
      {children}
    </ThemeContext.Provider>
  );
}; 