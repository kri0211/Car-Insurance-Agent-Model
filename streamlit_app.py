import streamlit as st

from risk_profiler import risk_profiler
from conversion_predictor import conversion_predictor
from premium_advisor import premium_advisor
from decision_router import AutonomousDecisionAgent

st.title("Autonomous Insurance Decision System")

accidents = st.slider("Previous Accidents",0,5)
citations = st.slider("Previous Citations",0,5)
age = st.slider("Driver Age",18,70)
premium = st.slider("Quoted Premium",500,5000)

if st.button("Run Decision System"):

    customer = {
        "Prev_Accidents":accidents,
        "Prev_Citations":citations,
        "Driver_Age":age,
        "Driving_Exp":5,
        "HH_Drivers":2,
        "HH_Vehicles":2,
        "Quoted_Premium":premium,
        "Vehicl_Cost_Range":20000
    }

    risk = risk_profiler(customer)

    bind_score = conversion_predictor(customer)

    premium_flag = premium_advisor(customer)

    agent = AutonomousDecisionAgent()

    decision = agent.decide(
        risk,
        bind_score,
        premium_flag,
        "EA",
        "C"
    )

    st.write("Risk Tier:",risk)
    st.write("Bind Score:",bind_score)
    st.write("Premium Flag:",premium_flag)
    st.write("Final Decision:",decision["decision"])