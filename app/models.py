from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Define User model 
# represent user with fields for ID, Email, Name & Relationship to Loan
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    loans = relationship("Loan", back_populates="owner")

# Define Loan model
# represent a loan associated with a user. Field for ID, Amount, Interest Rate, Term, Owner
class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    annual_interest_rate = Column(Float)
    loan_term_months = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="loans")