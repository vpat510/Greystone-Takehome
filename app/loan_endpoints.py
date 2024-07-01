from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Loan

# Read Loan

# Update Loan

# Delete Loan


