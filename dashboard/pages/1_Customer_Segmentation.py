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

from src.services.analytics_service import (
    get_clustered_data
)

from src.visualizer import (
    create_pca_dataframe,
    pca_plot
)

from src.auth_guard import (
    protect_page
)

protect_page()

st.title(
    "Customer Segmentation"
)

df, X, labels = get_clustered_data()

pca_df = create_pca_dataframe(
    X,
    labels
)

fig = pca_plot(
    pca_df
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    df,
    use_container_width=True
)