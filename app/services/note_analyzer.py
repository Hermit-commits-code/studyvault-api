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
