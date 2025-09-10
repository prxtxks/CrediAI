from pydantic import BaseModel
from typing import Optional
from datetime import date

class LoanBase(BaseModel):
    amount: float
    term_months: int
    interest_rate: float
    borrower_id: int

class LoanCreate(LoanBase):
    pass

class LoanUpdate(BaseModel):
    amount: Optional[float] = None
    term_months: Optional[int] = None
    interest_rate: Optional[float] = None
    status: Optional[str] = None

class LoanOut(LoanBase):
    id: int
    status: str
    start_date: date

    class Config:
        orm_mode = True