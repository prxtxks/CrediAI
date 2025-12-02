from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/dashboard", tags=["Admin"])
def admin_dashboard():
    """
    Simple endpoint to view admin dashboard stats.
    For now, it returns placeholder data.
    """
    return {
        "total_users": 120,
        "total_loans": 55,
        "pending_loans": 12,
        "approved_loans": 33
    }