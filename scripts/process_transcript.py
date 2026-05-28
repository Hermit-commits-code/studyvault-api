from pathlib import Path


TRANSCRIPTS_DIR = Path("transcripts")
NOTES_DIR = Path("notes")


def read_transcript(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def create_notes(title: str, content: str) -> str:
    notes = f"""# {title}

## Summary

{content}

## Key Concepts

- Add key concept here
- Add key concept here
- Add key concept here

## Important Terms

- Add important term here
- Add important term here

## Action Items

- Review this transcript
- Refine these notes
"""

    return notes


def save_notes(file_path: Path, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    transcript_files = list(TRANSCRIPTS_DIR.glob("*.txt"))

    for transcript_file in transcript_files:
        title = transcript_file.stem.replace("-", " ").title()
        output_file = NOTES_DIR / f"{transcript_file.stem}.md"

        transcript_content = read_transcript(transcript_file)
        notes_content = create_notes(title, transcript_content)

        save_notes(output_file, notes_content)

        print(f"Created notes: {output_file}")


if __name__ == "__main__":
    main()
