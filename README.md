# StudyVault API

StudyVault API is a FastAPI backend for converting raw learning transcripts into structured markdown notes and exposing them through searchable API endpoints.

## Features

- Process raw `.txt` transcripts into markdown notes
- Generate structured study-note templates
- List available notes
- Read individual notes
- Search note contents
- Built with FastAPI and Python

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Markdown
- Git/GitHub

## Project Structure

```text
app/
  api/
  services/
  core/
  models/
notes/
scripts/
tests/
transcripts/
```

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## Process Transcripts
```bash
python -m scripts.process_transcript
```
## API ENDPOINTS
GET /
GET /notes
GET /notes/{filename}
GET /search?q=functions

## Status
MVP in progress

