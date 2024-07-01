from pydantic import BaseModel

#User Schemas

# UserBase -> base schema for user data containing email field
class UserBase(BaseModel):
    email: str

# Schema for creating a user. extend userBase to include name
class UserCreate(UserBase):
    name: str

# Schema for returning user data. extend UserBase to unlcude ID & name. Config to work with ORM Models
class User(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True



#Loan Schemas

# Base class for loan data containing amount, interest rate, term, owner ID
class LoanBase(BaseModel):
    amount: float
    annual_interest_rate: float
    loan_term_months: int
    owner_id: int

# Schema for creating a loan
class LoanCreate(LoanBase):
    pass

# Schema for returning loan data ie extends LoanBase to include ID for returning loan data. 
class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True


#Additonal Schemas

# Schema for loan schedule entry. loan schedule entries for months, remaining balance, and montyly payemnts
class LoanSchedule(BaseModel):
    month: int
    remaining_balance: float
    monthly_payment: float

# Schema for loan summary ie current principal, total principal and total paid interest
class LoanSummary(BaseModel):
    current_principal_balance: float
    total_principal_paid: float
    total_interest_paid: float

# Schema for messages with a message field
class Message(BaseModel):
    message: str





    