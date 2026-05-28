from app.services.note_analyzer import detect_tags


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
