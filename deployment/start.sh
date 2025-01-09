#!/bin/bash

# Start the combined server
uvicorn server:app --host 0.0.0.0 --port $PORT 