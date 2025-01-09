// src/services/api.ts

import axios from 'axios';

// Define the base URL from environment variables
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// Create an Axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Define the response structure based on your backend
interface CompileResponse {
  success: boolean;
  errors: Array<{
    type: string;
    message: string;
    line: number;
    column: number;
  }>;
  symbol_table: Record<string, any>;
  ast_image: string | null;
}

// Function to compile code
export const compileCode = async (code: string): Promise<CompileResponse> => {
  try {
    const response = await api.post<CompileResponse>('/compile', { code });
    return response.data;
  } catch (error: any) {
    // Handle errors appropriately
    if (error.response) {
      // Server responded with a status other than 2xx
      throw new Error(error.response.data.detail || 'Server Error');
    } else if (error.request) {
      // Request was made but no response received
      throw new Error('No response from server. Please try again later.');
    } else {
      // Something else happened
      throw new Error(error.message);
    }
  }
};
