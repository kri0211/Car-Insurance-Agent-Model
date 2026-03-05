import pandas as pd

data = pd.read_csv("Autonomous_QUOTE_Agents.csv")

cost_map = {
    "<= $ 10 K": 10000,
    "> $ 10 K <= $ 20 K": 20000,
    "> $ 20 K <= $ 30 K": 30000,
    "> $ 30 K <= $ 40 K": 40000,
    "> $ 40 K": 50000
}

data["Vehicl_Cost_Range"] = data["Vehicl_Cost_Range"].map(cost_map).fillna(0)

def premium_advisor(row):

    premium = float(row["Quoted_Premium"])
    vehicle_cost = row["Vehicl_Cost_Range"]

    if premium > vehicle_cost * 0.30:
        return "HIGH"
    elif premium < vehicle_cost * 0.10:
        return "LOW"
    else:
        return "NORMAL"

data["Premium_Flag"] = data.apply(premium_advisor, axis=1)

print(data[["Quoted_Premium","Vehicl_Cost_Range","Premium_Flag"]].head())