import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

sys.path.append(
    str(ROOT_DIR)
)

import streamlit as st

from src.predict import (
    predict_customer
)

from src.recommender import (
    get_cluster_name,
    get_recommendation
)

st.title(
    "Customer Segment Predictor"
)

st.markdown(
    "Predict customer segment and generate business recommendations."
)

age = st.slider(
    "Age",
    18,
    70,
    25
)

income = st.slider(
    "Annual Income (k$)",
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
    "Predict Segment"
):

    cluster = predict_customer(
        age,
        income,
        spending
    )

    segment = get_cluster_name(
        cluster
    )

    recommendation = (
        get_recommendation(
            cluster
        )
    )

    st.success(
        f"Predicted Segment: {segment}"
    )

    st.info(
        recommendation
    )