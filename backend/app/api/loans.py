from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app.database.connection import get_db
from backend.app.database.models import LoanApplication
from backend.app.schemas.loan_schemas import LoanApplicationCreate, LoanApplicationOut

router = APIRouter()

@router.post("/", response_model=LoanApplicationOut, status_code=status.HTTP_201_CREATED)
def create_loan_application(application: LoanApplicationCreate, db: Session = Depends(get_db)):
    """
    Create a new loan application.
    """
    new_application = LoanApplication(
        user_id=application.user_id,
        amount=application.amount,
        term_months=application.term_months,
        purpose=application.purpose,
        status="Pending"
    )
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

@router.get("/{user_id}", response_model=List[LoanApplicationOut])
def get_user_loans(user_id: int, db: Session = Depends(get_db)):
    """
    Get all loan applications for a specific user.
    """
    loans = db.query(LoanApplication).filter(LoanApplication.user_id == user_id).all()
    if not loans:
        raise HTTPException(status_code=404, detail="No loans found for this user")
    return loans

@router.patch("/{loan_id}", response_model=LoanApplicationOut)
def update_loan_status(loan_id: int, status: str, db: Session = Depends(get_db)):
    """
    Update the status of a loan application (e.g., Approved, Rejected).
    """
    loan = db.query(LoanApplication).filter(LoanApplication.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=404, detail="Loan application not found")
    
    loan.status = status
    db.commit()
    db.refresh(loan)
    return loan