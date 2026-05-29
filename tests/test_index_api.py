from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_endpoint_exists():
    response = client.get("/index")

    assert response.status_code == 200


def test_index_returns_note_list():
    response = client.get("/index")

    data = response.json()

    assert "total_notes" in data
    assert "notes" in data
    assert isinstance(data["notes"], list)


def test_index_note_has_required_fields():
    response = client.get("/index")

    data = response.json()

    first_note = data["notes"][0]

    assert "title" in first_note
    assert "filename" in first_note
