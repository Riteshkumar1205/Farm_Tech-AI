from fastapi import APIRouter
from tools.seeds_adapter import fetch_official_prices, compare_with_dealer

router = APIRouter()

@router.get("/seeds/advisory")
def seed_advisory(crop: str, dealer_name: str, dealer_price: float):
    official = fetch_official_prices(crop)
    comparison = compare_with_dealer(crop, dealer_price, dealer_name)
    return {"crop": crop, "official": official, "dealer_comparison": comparison}
