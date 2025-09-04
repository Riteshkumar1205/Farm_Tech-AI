import pandas as pd

def fetch_packcommittee_prices(commodity: str):
    df = pd.read_csv("data/samples/packcommittee_prices.csv")
    df = df[df["commodity"].str.lower() == commodity.lower()]
    return df.to_dict(orient="records")
