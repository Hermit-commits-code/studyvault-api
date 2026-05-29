from app.services.note_analyzer import clean_transcript, detect_suspicious_words


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


def test_fixes_additional_word_merges():
    text = "alsooperations willhelp Soas isevaluated seethe"

    result = clean_transcript(text)

    assert "also operations" in result
    assert "will help" in result
    assert "So as" in result
    assert "is evaluated" in result
    assert "see the" in result

def test_detects_suspicious_merged_words():
    text = "This lesson explains variableassignment and expressionevaluation."

    result = detect_suspicious_words(text)

    assert "variableassignment" in result
    assert "expressionevaluation" in result
