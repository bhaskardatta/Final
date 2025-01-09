from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import sys

# Add the backend directory and api_server to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(current_dir, '..', 'Compiler-backend')
api_server_path = os.path.join(backend_path, 'api_server')
sys.path.append(backend_path)
sys.path.append(api_server_path)

# Import the backend app
from main import app as backend_app

# Create the main app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the backend API
app.mount("/api", backend_app)

# Mount the frontend static files
frontend_path = os.path.join(current_dir, '..', 'Compiler-frontend', 'dist')
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

# Add health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Serve index.html for all routes (SPA support)
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(os.path.join(frontend_path, "index.html")) 