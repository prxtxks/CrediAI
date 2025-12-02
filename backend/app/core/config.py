import os
from pydantic import BaseSettings, PostgresDsn, validator

class Settings(BaseSettings):
    """
    Application configuration using environment variables.
    """
    # App settings
    APP_NAME: str = "CrediAI"
    DEBUG: bool = True
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # Database settings
    DATABASE_URL: PostgresDsn = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/credi_ai"
    )

    # ML model paths
    MODEL_PATH: str = "backend/app/ml/saved_models/credit_model.pkl"

    # Logging settings
    LOG_FILE: str = "logs/app.log"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()