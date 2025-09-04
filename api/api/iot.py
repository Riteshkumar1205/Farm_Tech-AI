from fastapi import APIRouter
from tools.iot_adapter import latest_sensor_data

router = APIRouter()

@router.get("/iot/{farm_id}")
def iot(farm_id: str):
    return latest_sensor_data(farm_id)
