import streamlit as st

from src.predict import (
    predict_customer
)

st.title(
    "Customer Predictor"
)

age = st.slider(
    "Age",
    18,
    70,
    25
)

income = st.slider(
    "Income",
    15,
    150,
    50
)

spending = st.slider(
    "Spending Score",
    1,
    100,
    50
)

if st.button(
        "Predict Segment"):

    cluster = predict_customer(
        age,
        income,
        spending
    )

    st.success(
        f"Predicted Cluster : {cluster}"
    )