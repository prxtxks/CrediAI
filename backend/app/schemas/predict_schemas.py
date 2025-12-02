from pydantic import BaseModel
from typing import List, Optional

class PredictInput(BaseModel):
    numeric_features: List[float]
    categorical_features: List[str]

class PredictOutput(BaseModel):
    predicted_class: int
    probability: float

class BatchPredictInput(BaseModel):
    inputs: List[PredictInput]

class BatchPredictOutput(BaseModel):
    results: List[PredictOutput]