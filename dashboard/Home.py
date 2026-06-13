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

from src.filter_service import (
    apply_filters
)

from src.services.analytics_service import (
    get_clustered_data
)

st.set_page_config(
    page_title="Mall Customer Analytics",
    page_icon="📊",
    layout="wide"
)

from src.auth_guard import (
    protect_page
)

protect_page()

load_css()

df, X, labels = get_clustered_data()

page_header()

# ==================================
# SIDEBAR FILTERS
# ==================================

st.sidebar.header(
    "Dashboard Filters"
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (
        int(df["Age"].min()),
        int(df["Age"].max())
    )
)

income_range = st.sidebar.slider(
    "Income Range",
    int(
        df["Annual Income (k$)"]
        .min()
    ),
    int(
        df["Annual Income (k$)"]
        .max()
    ),
    (
        int(
            df["Annual Income (k$)"]
            .min()
        ),
        int(
            df["Annual Income (k$)"]
            .max()
        )
    )
)

spending_range = st.sidebar.slider(
    "Spending Score",
    int(
        df[
            "Spending Score (1-100)"
        ].min()
    ),
    int(
        df[
            "Spending Score (1-100)"
        ].max()
    ),
    (
        int(
            df[
                "Spending Score (1-100)"
            ].min()
        ),
        int(
            df[
                "Spending Score (1-100)"
            ].max()
        )
    )
)

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"]
    .unique()
    .tolist(),
    default=df["Gender"]
    .unique()
    .tolist()
)

cluster_filter = st.sidebar.multiselect(
    "Cluster",
    options=sorted(
        df["Cluster"]
        .unique()
        .tolist()
    ),
    default=sorted(
        df["Cluster"]
        .unique()
        .tolist()
    )
)

filtered_df = apply_filters(
    df,
    age_range,
    income_range,
    spending_range,
    gender_filter,
    cluster_filter
)

# ==================================
# KPI SECTION
# ==================================

c1, c2, c3, c4 = st.columns(4)

with c1:

    render_kpi(
        "Customers",
        len(filtered_df)
    )

with c2:

    render_kpi(
        "Avg Income",
        round(
            filtered_df[
                "Annual Income (k$)"
            ].mean(),
            2
        )
    )

with c3:

    render_kpi(
        "Avg Spending",
        round(
            filtered_df[
                "Spending Score (1-100)"
            ].mean(),
            2
        )
    )

with c4:

    render_kpi(
        "Segments",
        len(
            filtered_df[
                "Cluster"
            ].unique()
        )
    )

st.markdown("---")

left, right = st.columns(2)

with left:

    segment_df = (
        filtered_df[
            "Cluster"
        ]
        .value_counts()
        .reset_index()
    )

    segment_df.columns = [
        "Cluster",
        "Customers"
    ]

    pie_fig = px.pie(
        segment_df,
        names="Cluster",
        values="Customers",
        hole=0.5
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

with right:

    scatter_fig = px.scatter(
        filtered_df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        color=filtered_df[
            "Cluster"
        ].astype(str),
        hover_data=["Age"]
    )

    st.plotly_chart(
        scatter_fig,
        use_container_width=True
    )

st.markdown("---")

hist = px.histogram(
    filtered_df,
    x="Age",
    nbins=20
)

st.plotly_chart(
    hist,
    use_container_width=True
)

st.markdown("---")

st.dataframe(
    filtered_df,
    use_container_width=True
)