from app.services.note_analyzer import detect_tags, extract_vocabulary, generate_summary


def test_detects_boolean_tags():
    content = "Booleans use True and False values."

    tags = detect_tags(content)

    assert "booleans" in tags


def test_detects_conditionals_tags():
    content = "Use if and else statements to control logic."

    tags = detect_tags(content)

    assert "conditionals" in tags


def test_detects_comparison_operator_tags():
    content = "Use == and != to compare values."

    tags = detect_tags(content)

    assert "comparison-operators" in tags


def test_generate_summary_returns_text():
    transcript = (
        "Python uses numbers for arithmetic operations. "
        "Expressions are evaluated and printed. "
        "Variables will be introduced later."
    )

    summary = generate_summary(transcript)

    assert isinstance(summary, str)
    assert len(summary) > 0


def test_summary_is_shorter_than_original_text():
    transcript = (
        "Python uses numbers for arithmetic operations. "
        "Expressions are evaluated and printed. "
        "Variables will be introduced later. "
        "This lesson focuses on numerical computation."
    )

    summary = generate_summary(transcript)

    assert len(summary) <= len(transcript)


def test_extracts_vocabulary_terms():
    transcript = "Booleans use True and False values in conditional statements."

    vocabulary = extract_vocabulary(transcript)

    assert "Boolean" in vocabulary
    assert "Conditional Statement" in vocabulary
