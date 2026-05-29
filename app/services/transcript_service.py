from pathlib import Path

from app.services.index_generator import generate_index
from app.services.note_analyzer import (
    CONCEPT_DEFINITIONS,
    clean_transcript,
    detect_tags,
    generate_summary,
)

TRANSCRIPTS_DIR = Path("transcripts")
NOTES_DIR = Path("notes")


def read_transcript(file_path: Path) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def create_notes(title: str, content: str) -> str:
    cleaned_content = clean_transcript(content)
    tags = detect_tags(cleaned_content)
    tags_markdown = "\n".join(f"- {tag}" for tag in tags)
    key_concepts_list = []
    for tag in tags[:5]:
        if tag in CONCEPT_DEFINITIONS:
            key_concepts_list.append(
                f"- **{tag.replace('-', ' ').title()}**: {CONCEPT_DEFINITIONS[tag]}"
            )
        else:
            key_concepts_list.append(f"- {tag.replace('-', ' ').title()}")

    key_concepts = "\n".join(key_concepts_list)
    summary = generate_summary(cleaned_content)
    frontmatter_tags = "\n".join(f"  - {tag}" for tag in tags)

    notes = f'''
---
title: "{title}"
source_type: "transcript"
tags:
{frontmatter_tags}
---

# {title}

## Summary

{summary}

---

## Key Concepts
{key_concepts}
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
    generate_index()
