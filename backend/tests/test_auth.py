import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to CrediAI API!"}

def test_login_invalid_credentials():
    response = client.post("/auth/login", json={"username": "fakeuser", "password": "wrongpass"})
    assert response.status_code == 401
    assert "detail" in response.json()

def test_login_missing_fields():
    response = client.post("/auth/login", json={"username": "user"})
    assert response.status_code == 422  # Unprocessable Entity for missing fields