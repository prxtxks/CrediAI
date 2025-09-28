import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_loans_unauthorized():
    response = client.get("/loans/")
    assert response.status_code == 401  # Should fail without authentication

def test_create_loan_missing_fields():
    payload = {
        "user_id": 1,
        "loan_amount": 5000
        # Missing other required fields like income, purpose
    }
    response = client.post("/loans/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity

def test_create_loan_valid(monkeypatch):
    payload = {
        "user_id": 1,
        "loan_amount": 5000,
        "income": 60000,
        "credit_score": 700,
        "loan_purpose": "education"
    }

    # Mock authentication to bypass login (if needed)
    monkeypatch.setattr("app.api.loans.get_current_user", lambda: {"id": 1, "username": "testuser"})

    response = client.post("/loans/", json=payload)
    assert response.status_code in [200, 201]
    assert "loan_id" in response.json()