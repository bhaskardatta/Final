#!/bin/bash

echo "Starting build process..."

# Install system dependencies
echo "Installing system dependencies..."
apt-get update
apt-get install -y graphviz

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Build frontend
echo "Building frontend..."
cd ../Compiler-frontend
npm install
npm run build
cd ../deployment

# Ensure backend files are in place
echo "Setting up backend..."
mkdir -p ../Compiler-backend/api_server
cp -r ../Compiler-backend/api_server/* ../Compiler-backend/api_server/

echo "Build process complete!" 