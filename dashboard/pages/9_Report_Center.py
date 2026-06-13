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

from src.train import train_model

st.title(
    "Report Center"
)

from src.services.analytics_service import (
    get_clustered_data
)

df, X, labels = get_clustered_data()

csv = df.to_csv(
    index=False
)

st.download_button(
    label="Download Customer Segments CSV",
    data=csv,
    file_name="customer_segments.csv",
    mime="text/csv"
)

st.dataframe(
    df.head(20)
)