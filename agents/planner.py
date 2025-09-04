def plan_acreage(farm_size, soil, weather, market, seeds):
    # Very simplified acreage planner (placeholder)
    recommendations = []
    for crop in market:
        suitability = 1 if soil["ph"] >= 6 else 0.5
        profit_score = suitability * crop["avg_price"]
        recommendations.append({"crop": crop["commodity"], "score": profit_score})
    return sorted(recommendations, key=lambda x: x["score"], reverse=True)
