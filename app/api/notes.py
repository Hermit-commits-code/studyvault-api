from pathlib import Path

from fastapi import APIRouter, HTTPException

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

@router.get("/notes/{filename}")
def get_notes(filename: str):
    note_path = NOTES_DIR / filename

    if not note_path.exists():
        raise HTTPException(status_code=404, detail="Note not found")

    with open(note_path, "r", encoding="utf-8") as file:
        content = file.read()

    return{
        "filename": filename,
        "content": content,
    }

@router.get('/search')
def search_notes(q: str):
    results=[]

    for note_file in NOTES_DIR.glob("*.md"):
        with open(note_file, "r", encoding='utf-8')as file:
            content = file.read()

        if q.lower() in content.lower():
            results.append({
                "title": note_file.stem.replace("-", " ").title(),
                "filename": note_file.name,
                "path": str(note_file)
            }
        )
    return{
        "query": q,
        "results": results,
        "count": len(results),
    }
