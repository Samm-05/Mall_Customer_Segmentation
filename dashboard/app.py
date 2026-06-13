import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(
    page_title="Mall Customer Segmentation",
    layout="wide"
)

st.title(
    "🛍️ Mall Customer Segmentation System"
)

st.write(
    "Predict customer segment using K-Means Clustering"
)

age = st.slider(
    "Age",
    18,
    70,
    25
)

income = st.slider(
    "Annual Income (k$)",
    10,
    150,
    60
)

score = st.slider(
    "Spending Score",
    1,
    100,
    50
)

if st.button(
        "Predict Cluster"):

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    model = joblib.load(
        "models/kmeans.pkl"
    )

    sample = np.array(
        [[
            age,
            income,
            score
        ]]
    )

    sample_scaled = scaler.transform(
        sample
    )

    cluster = model.predict(
        sample_scaled
    )

    st.success(
        f"Customer belongs to Cluster {cluster[0]}"
    )

st.divider()

st.subheader(
    "Customer Segmentation Data"
)

df = pd.read_csv(
    "outputs/customer_segments.csv"
)

st.dataframe(
    df
)