import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("Autonomous_QUOTE_AGENTS.csv")

data["Policy_Bind"] = data["Policy_Bind"].map({"Yes":1,"No":0})

features = [
"HH_Vehicles",
"HH_Drivers",
"Driver_Age",
"Driving_Exp",
"Prev_Accidents",
"Prev_Citations",
"Quoted_Premium"
]

X = data[features]
y = data["Policy_Bind"]

model = LogisticRegression(max_iter=1000)
model.fit(X,y)


def conversion_predictor(customer):

    customer_data = [[
        customer["HH_Vehicles"],
        customer["HH_Drivers"],
        customer["Driver_Age"],
        customer["Driving_Exp"],
        customer["Prev_Accidents"],
        customer["Prev_Citations"],
        customer["Quoted_Premium"]/2
    ]]

    probability = model.predict_proba(customer_data)

    return probability[0][1]