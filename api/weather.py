from fastapi import APIRouter
from tools.imd_adapter import get_forecast

router = APIRouter()

@router.get("/weather")
def weather(lat: float, lon: float):
    return get_forecast(lat, lon)
