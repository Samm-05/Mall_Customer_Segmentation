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
    "Executive Insights"
)

df, X, labels = train_model()

cluster_counts = (
    df["Cluster"]
    .value_counts()
)

top_cluster = (
    cluster_counts.idxmax()
)

st.metric(
    "Largest Segment",
    f"Cluster {top_cluster}"
)

st.metric(
    "Customers",
    cluster_counts.max()
)

st.markdown("---")

for cluster in sorted(
        df["Cluster"].unique()):

    cluster_df = df[
        df["Cluster"]
        == cluster
    ]

    st.subheader(
        f"Cluster {cluster}"
    )

    st.write(
        f"Customers: {len(cluster_df)}"
    )

    st.write(
        f"Average Income: {cluster_df['Annual Income (k$)'].mean():.2f}"
    )

    st.write(
        f"Average Spending: {cluster_df['Spending Score (1-100)'].mean():.2f}"
    )