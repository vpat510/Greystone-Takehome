from fastapi import FastAPI
from app.database import engine, Base
from . import models
from .user_endpoints import router as user_router
from .loan_endpoints import router as loan_router


# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the User router
app.include_router(user_router, prefix="/api/v1")
app.include_router(loan_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Amortization API"}

