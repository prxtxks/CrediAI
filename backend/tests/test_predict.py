import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_valid_input():
    payload = {
        "user_id": 1,
        "loan_amount": 5000,
        "income": 60000,
        "credit_score": 720,
        "loan_purpose": "personal"
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in ["approved", "denied"]

def test_predict_missing_fields():
    payload = {"user_id": 1, "loan_amount": 5000}
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity for missing fields

def test_predict_invalid_values():
    payload = {
        "user_id": 1,
        "loan_amount": -1000,  # Invalid negative loan
        "income": 0,
        "credit_score": 500,
        "loan_purpose": "personal"
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 400