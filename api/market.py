from fastapi import APIRouter
from tools.market_adapter import fetch_market_prices
from tools.packcommittee_adapter import fetch_packcommittee_prices

router = APIRouter()

@router.get("/market/{commodity}")
def market(commodity: str):
    agmarknet = fetch_market_prices(commodity)
    local = fetch_packcommittee_prices(commodity)
    return {"commodity": commodity, "agmarknet": agmarknet, "local": local}
