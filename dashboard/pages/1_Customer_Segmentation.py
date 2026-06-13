import streamlit as st

from src.train import train_model
from src.visualizer import (
    create_pca_dataframe,
    pca_plot
)

st.title("Customer Segmentation Dashboard")

df, X, labels = train_model()

st.success(
    f"Successfully Segmented {len(df)} Customers"
)

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

st.subheader(
    "Segmented Customers"
)

st.dataframe(
    df,
    use_container_width=True
)