import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(ROOT_DIR)
)

import streamlit as st
import plotly.express as px

from src.ui import load_css

from src.services.analytics_service import (
    get_clustered_data
)

load_css()

st.set_page_config(
    page_title="Mall Customer Analytics",
    layout="wide"
)

df, X, labels = get_clustered_data()

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
        "Average Income",
        round(
            df[
                "Annual Income (k$)"
            ].mean(),
            2
        )
    )

with col3:

    st.metric(
        "Average Spending",
        round(
            df[
                "Spending Score (1-100)"
            ].mean(),
            2
        )
    )

with col4:

    st.metric(
        "Segments",
        len(
            df["Cluster"]
            .unique()
        )
    )

st.markdown("---")

left, right = st.columns(2)

with left:

    cluster_df = (
        df["Cluster"]
        .value_counts()
        .reset_index()
    )

    cluster_df.columns = [
        "Cluster",
        "Customers"
    ]

    pie_fig = px.pie(
        cluster_df,
        names="Cluster",
        values="Customers",
        hole=0.5,
        title="Customer Segments"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

with right:

    scatter_fig = px.scatter(
        df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color=df["Cluster"].astype(str),
        title="Income vs Spending"
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

st.markdown("---")

hist_fig = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

st.plotly_chart(
    hist_fig,
    use_container_width=True
)