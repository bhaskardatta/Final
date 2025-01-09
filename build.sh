#!/bin/bash

# Install frontend dependencies and build
echo "Building frontend..."
cd ../Compiler-frontend
npm install
npm run build

# Install backend dependencies
echo "Setting up backend..."
cd ../Compiler-backend
pip install -r requirements.txt

# Install deployment dependencies
echo "Setting up deployment..."
cd ../deployment
pip install -r requirements.txt

echo "Build complete!" 