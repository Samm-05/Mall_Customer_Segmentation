import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.train import train_model
from src.ui import load_css

load_css()

st.set_page_config(
    page_title="Customer Analytics",
    layout="wide"
)

df, X, labels = train_model()

st.markdown(
    """
    <div class="main-header">
    Mall Customer Analytics Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        len(df)
    )

with col2:
    st.metric(
        "Avg Income",
        round(
            df["Annual Income (k$)"].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Avg Spending",
        round(
            df["Spending Score (1-100)"].mean(),
            2
        )
    )

with col4:
    st.metric(
        "Clusters",
        len(
            df["Cluster"].unique()
        )
    )

st.markdown("---")

st.markdown(
    """
    <div class="section-title">
    Customer Distribution
    </div>
    """,
    unsafe_allow_html=True
)

cluster_count = (
    df["Cluster"]
    .value_counts()
    .reset_index()
)

cluster_count.columns = [
    "Cluster",
    "Customers"
]

fig = px.pie(
    cluster_count,
    names="Cluster",
    values="Customers",
    hole=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)