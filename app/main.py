from fastapi import FastAPI
from app.database import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Amortization API"}