import re

def detect_tags(content: str)-> list[str]:
    text = content.lower()

    tags=["python", "beginner"]
    if "boolean" in text or "true" in text or "false" in text:
        tags.append("booleans")

    if "if" in text or "else" in text or "elif" in text:
        tags.append("conditionals")

    if "==" in text or "!=" in text or "greater than" in text or "less than" in text:
        tags.append("comparison-operators")

    return sorted(set(tags))

def clean_transcript(content: str)-> str:
    cleaned = content
    cleaned = re.sub(r"\s+"," ", cleaned)
    cleaned = re.sub(r"([a-z])([A-Z])", r"\1 \2", cleaned)

    cleaned = re.sub(r"([a-zA-Z])(\d)", r"\1 \2", cleaned)

    cleaned = re.sub(r"(\d)([a-zA-Z])", r"\1 \2", cleaned)

    return cleaned.strip()

def generate_summary(content: str, max_sentences: int = 3) -> str:
    sentences = content.split(".")

    cleaned_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        if sentence.count(" ") < 5:
            continue

        cleaned_sentences.append(sentence)

    summary_sentences = cleaned_sentences[:max_sentences]

    summary = ". ".join(summary_sentences)

    if summary and not summary.endswith("."):
        summary += "."

    return summary
