from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

NOTES_DIR = Path("notes")

@router.get("/notes")
def list_notes():
    notes = []

    for note_file in NOTES_DIR.glob("*.md"):
        notes.append(
            {
                "title": note_file.stem.replace("-", " ").title(),
                "filename": note_file.name,
                "path": str(note_file),
            }
        )
    return {"notes": notes}
