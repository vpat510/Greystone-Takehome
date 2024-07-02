import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models import User, Loan


# Configure an SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Override the get_db dependency to use the testing database.
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Tests the user creation endpoint
def test_create_user(setup_db):
    response = client.post("/api/v1/users/", json={"email": "test@example.com", "name": "Test User"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["name"] == "Test User"

# Tests the loan creation endpoint
def test_create_loan(setup_db):
    user_response = client.post("/api/v1/users/", json={"email": "loanuser@example.com", "name": "Loan User"})
    user_id = user_response.json()["id"]
    loan_data = {
        "amount": 10000,
        "annual_interest_rate": 5,
        "loan_term_months": 12,
        "owner_id": user_id
    }
    response = client.post("/api/v1/loans/", json=loan_data)
    assert response.status_code == 200
    assert response.json()["amount"] == 10000
    assert response.json()["annual_interest_rate"] == 5
    assert response.json()["loan_term_months"] == 12
    assert response.json()["owner_id"] == user_id

# Tests the amortization schedule endpoint
def test_get_amortization_schedule(setup_db):
    user_response = client.post("/api/v1/users/", json={"email": "amortuser@example.com", "name": "Amort User"})
    user_id = user_response.json()["id"]
    loan_data = {
        "amount": 10000,
        "annual_interest_rate": 5,
        "loan_term_months": 12,
        "owner_id": user_id
    }
    loan_response = client.post("/api/v1/loans/", json=loan_data)
    loan_id = loan_response.json()["id"]

    response = client.get(f"/api/v1/loans/{loan_id}/amortization")
    assert response.status_code == 200
    assert len(response.json()) == 12
    assert response.json()[0]["month"] == 1
    assert response.json()[0]["monthly_payment"] > 0
    assert response.json()[-1]["month"] == 12
    assert response.json()[-1]["remaining_balance"] == 0