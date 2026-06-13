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

from src.advanced_visualizer import (
    create_pca,
    pca_chart
)

st.title(
    "PCA Analytics"
)

df, X, labels = train_model()

pca_df = create_pca(
    df,
    X,
    labels
)

fig = pca_chart(
    pca_df
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    pca_df.head()
)