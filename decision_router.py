import pandas as pd

class AutonomousDecisionAgent:

    def __init__(self):
        self.decision_count = 0

    def decide(self, risk_tier, bind_score, premium_flag, agent_type, region):

        self.decision_count += 1

        if risk_tier!="High Risk" and bind_score > 0.15 and premium_flag == "NORMAL":
            decision = "AUTO APPROVE"

        elif risk_tier == "High Risk" and bind_score < 0.30:
            decision = "REJECT"

        elif premium_flag == "HIGH":
            decision = "ESCALATE"

        else:
            decision = "AGENT REVIEW"

        return {
            "decision_id": self.decision_count,
            "decision": decision,
            "risk_tier": risk_tier,
            "bind_score": f"{bind_score:.2f}",
            "premium_flag": premium_flag,
            "agent_type": agent_type,
            "region": region,
            "timestamp": pd.Timestamp.now()
        }