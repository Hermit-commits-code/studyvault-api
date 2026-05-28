from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "StudyVault API is running!"}

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_notes_endpoint():
    response = client.get("/notes")

    assert response.status_code == 200
    assert "notes" in response.json()

def test_search_endpoint():
    response = client.get("/search?q=functions")
    assert response.status_code == 200
    assert "results" in response.json()
