from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index_endpoint_exists():
    response = client.get("/index")

    assert response.status_code == 200
