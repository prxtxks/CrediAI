from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
import joblib

from backend.app.database.connection import get_db
from backend.app.ml.train_model import train_credit_model

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def train_model(db: Session = Depends(get_db)):
    """
    Train the credit scoring model and save it to disk.
    """
    try:
        model, metrics = train_credit_model(db)
        # Save trained model
        joblib.dump(model, "backend/app/ml/saved_models/credit_model.pkl")
        return {
            "message": "Model trained successfully",
            "metrics": metrics
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Training failed: {str(e)}"
        )