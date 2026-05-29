from app.services.note_analyzer import clean_transcript


def test_removes_extra_whitespace():
    text = "hello     world"

    result = clean_transcript(text)

    assert result == "hello world"


def test_fixes_common_transcript_artifacts():
    text = "Andthis Boolean canmake decisions usingconditions."

    result = clean_transcript(text)

    assert "And this" in result
    assert "can make" in result
    assert "using conditions" in result
