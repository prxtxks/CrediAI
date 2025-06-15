from fastapi import APIRouter

from .auth import router as auth_router
from .predict import router as predict_router
from .train import router as train_router
from .users import router as users_router
from .health import router as health_router
from .loans import router as loans_router

# Main API router
api_router = APIRouter()

# Register routes
api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(loans_router, prefix="/loans", tags=["Loans"])
api_router.include_router(predict_router, prefix="/predict", tags=["Predictions"])
api_router.include_router(train_router, prefix="/train", tags=["Model Training"])