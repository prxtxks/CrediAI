from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, predict, users, loans, train, health, admin
from app.database.connection import engine, get_db
from app.database.models import Base

# Initialize FastAPI app
app = FastAPI(
    title="CrediAI - AI-Powered Credit Scoring API",
    description="API backend for loan approval and credit scoring using AI models",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include API routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(loans.router, prefix="/loans", tags=["loans"])
app.include_router(predict.router, prefix="/predict", tags=["predict"])
app.include_router(train.router, prefix="/train", tags=["train"])
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to CrediAI API!"}