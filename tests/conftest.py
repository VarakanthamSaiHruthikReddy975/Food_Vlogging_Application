import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """
    Docstring for client
    example code:
    def test_client(client):
        response = client.get("/")
        assert response.status_code == 200
    """
    return TestClient(app)