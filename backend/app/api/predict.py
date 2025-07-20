from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
import joblib
import numpy as np

from backend.app.database.connection import get_db
from backend.app.schemas.predict_schemas import PredictInput, PredictOutput
from backend.app.ml.feature_engineering import preprocess_input

router = APIRouter()

# Load trained model (XGBoost / Random Forest)
try:
    model = joblib.load("backend/app/ml/saved_models/credit_model.pkl")
except FileNotFoundError:
    model = None
    print("Model not found. Train the model first using /train endpoint.")

@router.post("/", response_model=PredictOutput)
def predict_credit(input_data: PredictInput, db: Session = Depends(get_db)):
    """
    Predict loan approval probability for a user.
    """
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Prediction model not available. Train model first."
        )
    
    # Preprocess input
    processed_input = preprocess_input(input_data.dict())
    
    # Predict probability
    try:
        probability = model.predict_proba(processed_input)[:, 1][0]  # probability of approval
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )
    
    # Convert probability to approval decision
    decision = "Approved" if probability >= 0.5 else "Rejected"
    
    return PredictOutput(
        probability=round(float(probability), 4),
        decision=decision
    )