import streamlit as st

from src.services.customer_service import (
    get_customer_data,
    get_model,
    get_scaler
)


@st.cache_data
def get_clustered_data():

    df = get_customer_data()

    scaler = get_scaler()

    model = get_model()

    X = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    X_scaled = scaler.transform(
        X
    )

    labels = model.predict(
        X_scaled
    )

    df["Cluster"] = labels

    return (
        df,
        X_scaled,
        labels
    )