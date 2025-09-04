import pandas as pd

official_df = pd.read_csv("data/samples/seeds_official.csv")

def fetch_official_prices(crop: str):
    return official_df[official_df['crop'].str.lower() == crop.lower()].to_dict(orient="records")

def compare_with_dealer(crop: str, dealer_price: float, dealer_name: str, threshold: float = 1.2):
    official = fetch_official_prices(crop)
    if not official:
        return {"status": "No official data", "dealer_price": dealer_price}
    base_price = official[0]['official_price']
    if dealer_price > base_price * threshold:
        return {
            "status": "Overpriced",
            "official_price": base_price,
            "dealer_price": dealer_price,
            "dealer": dealer_name
        }
    else:
        return {
            "status": "Fair",
            "official_price": base_price,
            "dealer_price": dealer_price,
            "dealer": dealer_name
        }
