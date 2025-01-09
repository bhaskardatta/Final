import React from 'react';
import { createRoot } from 'react-dom/client';
import Index from './pages/Index';
import './index.css';
import './styles/prism-custom.css';

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Index />
  </React.StrictMode>
);
