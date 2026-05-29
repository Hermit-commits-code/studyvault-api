#!/usr/bin/env bash

set -e

echo "Pulling latest changes..."
git pull

echo "Processing transcripts..."
python -m scripts.process_transcript

echo "Rebuilding and restarting containers..."
docker compose up -d --build

echo "Deployment complete."
