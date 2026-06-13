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
    create_tsne,
    tsne_chart
)

st.title(
    "t-SNE Analytics"
)

df, X, labels = train_model()

tsne_df = create_tsne(
    df,
    X,
    labels
)

fig = tsne_chart(
    tsne_df
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    tsne_df.head()
)