from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter()

TRANSCRIPTS_DIR = Path("transcripts")


@router.post("/transcripts/upload")
async def upload_transcript(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required.")
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")

    if "/" in file.filename or "\\" in file.filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    file_path = TRANSCRIPTS_DIR / file.filename

    content = await file.read()

    with open(file_path, "wb") as transcript_file:
        transcript_file.write(content)

    return {
        "message": "Transcript uploaded successfully",
        "filename": file.filename,
        "path": str(file_path),
    }
