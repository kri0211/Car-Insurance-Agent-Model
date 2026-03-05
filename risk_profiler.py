def risk_profiler(row):

    risk_score = 0
    reasons = []

    if row["Prev_Accidents"] >= 2:
        risk_score += 3
        reasons.append("Multiple previous accidents")

    elif row["Prev_Accidents"] == 1:
        risk_score += 1
        reasons.append("One previous accident")

    if row["Prev_Citations"] >= 2:
        risk_score += 2
        reasons.append("Multiple traffic citations")

    elif row["Prev_Citations"] == 1:
        risk_score += 1
        reasons.append("One traffic citation")

    if row["Driver_Age"] < 25:
        risk_score += 2
        reasons.append("Young driver)")

    if row["Driving_Exp"] < 3:
        risk_score += 2
        reasons.append("Low driving experience")

    if row["HH_Drivers"] > 2:
        risk_score += 1
        reasons.append("Many household drivers")

    if risk_score >= 5:
        risk = "High Risk"
    elif risk_score >= 3:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return risk, reasons