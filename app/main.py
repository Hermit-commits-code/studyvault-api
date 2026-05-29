from fastapi import FastAPI

from app.api.notes import router as notes_router
from app.api.transcripts import router as transcripts_router

app = FastAPI()

app.include_router(notes_router)
app.include_router(transcripts_router)


@app.get("/")
def home():
    return {"message": "StudyVault API is running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
