import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.ui import load_css

from src.theme import (
    render_kpi,
    page_header
)

from src.services.analytics_service import (
    get_clustered_data
)

st.set_page_config(
    page_title="Mall Customer Analytics",
    page_icon="📊",
    layout="wide"
)

load_css()

df, X, labels = get_clustered_data()

page_header()

st.markdown("---")

# ======================
# KPI SECTION
# ======================

c1, c2, c3, c4 = st.columns(4)

with c1:

    render_kpi(
        "Customers",
        len(df)
    )

with c2:

    render_kpi(
        "Avg Income",
        round(
            df[
                "Annual Income (k$)"
            ].mean(),
            2
        )
    )

with c3:

    render_kpi(
        "Avg Spending",
        round(
            df[
                "Spending Score (1-100)"
            ].mean(),
            2
        )
    )

with c4:

    render_kpi(
        "Segments",
        len(
            df["Cluster"]
            .unique()
        )
    )

st.markdown("---")

# ======================
# CHARTS
# ======================

left, right = st.columns(2)

with left:

    st.markdown(
        """
        <div class="section-title">
            Segment Distribution
        </div>
        """,
        unsafe_allow_html=True
    )

    segment_df = (
        df["Cluster"]
        .value_counts()
        .reset_index()
    )

    segment_df.columns = [
        "Cluster",
        "Customers"
    ]

    fig = px.pie(
        segment_df,
        names="Cluster",
        values="Customers",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.markdown(
        """
        <div class="section-title">
            Income vs Spending
        </div>
        """,
        unsafe_allow_html=True
    )

    scatter = px.scatter(
        df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color=df["Cluster"].astype(str)
    )

    st.plotly_chart(
        scatter,
        use_container_width=True
    )

st.markdown("---")

st.markdown(
    """
    <div class="section-title">
        Customer Age Distribution
    </div>
    """,
    unsafe_allow_html=True
)

hist = px.histogram(
    df,
    x="Age",
    nbins=20
)

st.plotly_chart(
    hist,
    use_container_width=True
)

st.markdown("---")

st.markdown(
    """
    <div class="section-title">
        Dataset Preview
    </div>
    """,
    unsafe_allow_html=True
)

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.sidebar.title(
    "Navigation"
)

st.sidebar.success(
    "Select a page from sidebar."
)