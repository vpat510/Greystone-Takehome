from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from .amortization import calculate_amortization_schedule

# Create router for loan endpoints
router = APIRouter()

# Dependency -> get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# fetch a loan by it's ID and return it. Raise 404 if not found
def get_loan_by_id(loan_id: int, db: Session):
    loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


# POST / Create new loan, add to database, commit transaction & return created loan
@router.post("/loans/", response_model=schemas.Loan)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    #mode_dump -> convert loan into pydantic model to a dictionary & then create a new `Loan` ORM instance using that dict
    new_loan = models.Loan(**loan.model_dump())
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan


# GET / Read Loan details by loan ID
@router.get("/loans/{loan_id}", response_model=schemas.Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    return get_loan_by_id(loan_id, db)


# PUT / Update Loan details by Loan & return updated loan
@router.put("/loans/{loan_id}", response_model=schemas.Loan)
def update_loan(loan_id: int, loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    db_loan = get_loan_by_id(loan_id, db)
    for key, value in loan.model_dump().items():
        setattr(db_loan, key, value)
    db.commit()
    db.refresh(db_loan)
    return db_loan

# DELETE / Delete Loan by loan ID, commit transaction & return deleted loan
@router.delete("/loans/{loan_id}", response_model=schemas.Loan)
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = get_loan_by_id(loan_id, db)
    db.delete(db_loan)
    db.commit()
    return db_loan

# calculates the amortization schedule for a loan based on the principal, annual interest rate, and loan term in months.
# calls the endpoint & returns the schedule
@router.get("/loans/{loan_id}/amortization", response_model=list[schemas.LoanSchedule])
def get_amortization_schedule(loan_id: int, db: Session = Depends(get_db)):
    loan = get_loan_by_id(loan_id, db)
    schedule = calculate_amortization_schedule(loan.amount, loan.annual_interest_rate, loan.loan_term_months)
    return schedule