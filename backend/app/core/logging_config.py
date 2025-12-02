import logging
import os
from logging.handlers import RotatingFileHandler
from .config import settings

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(settings.LOG_FILE), exist_ok=True)

# Define log formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
console_handler.setFormatter(formatter)

# File handler with rotation
file_handler = RotatingFileHandler(
    settings.LOG_FILE, maxBytes=5*1024*1024, backupCount=5
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
logger.info("Logging is configured and ready.")