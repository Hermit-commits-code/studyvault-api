from pathlib import Path
from app.services.note_analyzer import detect_tags, generate_summary, clean_transcript


TRANSCRIPTS_DIR = Path("transcripts")
NOTES_DIR = Path("notes")

def read_transcript(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def create_notes(title: str, content: str) -> str:
    cleaned_content = clean_transcript(content)
    summary = generate_summary(cleaned_content)
    tags = detect_tags(cleaned_content)
    tags_markdown="\n".join(f"- {tag}" for tag in tags)
    notes = f'''# {title}

## Summary

{summary}

---

## Key Concepts

- Main concept from transcript
- Supporting concept
- Important programming idea

---

## Code Example

```python
# Replace with transcript-related example

is_logged_in = True

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")
```

---

## Important Terms

### Boolean
A value that is either True or False.

### Conditional Statement
Logic that controls code execution using conditions.

---

## Common Mistakes

- Incorrect indentation
- Confusing `=` with `==`
- Forgetting colons after conditions

---

## Practice Tasks

- Write 3 if/else statements
- Create a boolean variable
- Practice comparison operators

---

## Tags

{tags_markdown}
'''
    return notes

def save_notes(file_path: Path, content: str) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def process_transcripts() -> None:
    transcript_files = list(TRANSCRIPTS_DIR.glob("*.txt"))
    for transcript_file in transcript_files:
        title = transcript_file.stem.replace("-", " ").title()

        output_file = NOTES_DIR / f"{transcript_file.stem}.md"

        transcript_content = read_transcript(transcript_file)

        notes_content = create_notes(title, transcript_content)

        save_notes(output_file, notes_content)

        print(f"Created notes: {output_file}")

