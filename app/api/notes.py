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
    if "/" in filename or "\\" in filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    if not filename.endswith(".md"):
        raise HTTPException(
            status_code=400, detail="Only markdown files are supported."
        )

    note_path = NOTES_DIR / filename

    if not note_path.exists():
        raise HTTPException(status_code=404, detail="Note not found")

    with open(note_path, encoding="utf-8") as file:
        content = file.read()

    return {
        "filename": filename,
        "content": content,
    }


@router.get("/search")
def search_notes(q: str):
    if not q.strip():
        raise HTTPException(status_code=400, detail="Search query cannot be empty")

    results = []

    for note_file in NOTES_DIR.glob("*.md"):
        with open(note_file, encoding="utf-8") as file:
            content = file.read()

        if q.lower() in content.lower():
            results.append(
                {
                    "title": note_file.stem.replace("-", " ").title(),
                    "filename": note_file.name,
                    "path": str(note_file),
                }
            )
    return {
        "query": q,
        "results": results,
        "count": len(results),
    }


@router.get("/index")
def get_index():
    note_files = [
        note_file
        for note_file in NOTES_DIR.glob("*.md")
        if note_file.name != "index.md"
    ]

    notes = [
        {
            "title": note_file.stem.replace("-", " ").title(),
            "filename": note_file.name,
        }
        for note_file in sorted(note_files)
    ]

    return {
        "total_notes": len(notes),
        "notes": notes,
    }
