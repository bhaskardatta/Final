from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add the backend directory and api_server to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
logger.info(f"Current directory: {current_dir}")

backend_path = os.path.join(current_dir, '..', 'Compiler-backend')
api_server_path = os.path.join(backend_path, 'api_server')

logger.info(f"Backend path: {backend_path}")
logger.info(f"API server path: {api_server_path}")

sys.path.append(backend_path)
sys.path.append(api_server_path)

try:
    # Import the backend app
    from main import app as backend_app
    logger.info("Successfully imported backend app")
except Exception as e:
    logger.error(f"Error importing backend app: {str(e)}")
    raise

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
logger.info(f"Frontend path: {frontend_path}")

if not os.path.exists(frontend_path):
    logger.error(f"Frontend build directory not found at {frontend_path}")
else:
    logger.info("Frontend directory found")
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

# Add health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "paths": {
            "current_dir": current_dir,
            "backend_path": backend_path,
            "api_server_path": api_server_path,
            "frontend_path": frontend_path
        }
    }

# Serve index.html for all routes (SPA support)
@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    if full_path.startswith("api/"):
        raise HTTPException(status_code=404, detail="Not found")
    index_path = os.path.join(frontend_path, "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="Frontend not built")
    return FileResponse(index_path) 