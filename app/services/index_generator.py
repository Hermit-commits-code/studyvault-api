from pathlib import Path

NOTES_DIR = Path("notes")
INDEX_FILE = NOTES_DIR / "index.md"


def generate_index() -> None:
    note_files = sorted(
        note_file
        for note_file in NOTES_DIR.glob("*.md")
        if note_file.name != "index.md"
    )

    notes_list = "\n".join(
        f"- [{note_file.stem.replace('-', ' ').title()}]({note_file.name})"
        for note_file in note_files
    )

    index_content = f"""# StudyVault Index

## Notes

{notes_list}

## Total Notes

{len(note_files)}
"""

    with open(INDEX_FILE, "w", encoding="utf-8") as file:
        file.write(index_content)
