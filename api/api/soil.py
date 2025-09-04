from fastapi import APIRouter
from tools.soil_adapter import get_soil_report

router = APIRouter()

@router.get("/soil/{farm_id}")
def soil(farm_id: str):
    return get_soil_report(farm_id)
