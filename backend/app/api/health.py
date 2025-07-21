from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Health"])
def health_check():
    """
    Simple health check endpoint to verify that the API is running.
    """
    return {"status": "ok", "message": "CrediAI API is running successfully."}