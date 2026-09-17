from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/")
def home():
    return {
        "message": "California house price prediction API",
        "status": "active",
    }


@router.get("/health")
def get_health():
    return {
        "status": "running",
        "model": "RandomForestRegressor",
        "avg_error": "$37,000",
    }