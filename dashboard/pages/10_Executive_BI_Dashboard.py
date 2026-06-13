import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__).resolve()
    .parent.parent.parent
)

sys.path.append(
    str(ROOT_DIR)
)

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from src.services.analytics_service import (
    get_clustered_data
)

from src.segment_analyzer import (
    auto_name_segments
)

from src.executive_insights import (
    generate_insights
)

from src.auth_guard import (
    protect_page,
    render_user_panel
)

protect_page()

render_user_panel()

st.title(
    "Executive BI Dashboard"
)

df, X, labels = get_clustered_data()

segment_names = auto_name_segments(df)

# ---------------------
# KPI Cards
# ---------------------

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
            df["Annual Income (k$)"]
            .mean(),
            2
        )
    )

with col3:
    st.metric(
        "Avg Spending",
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

# ---------------------
# Correlation Heatmap
# ---------------------

st.subheader(
    "Correlation Analysis"
)

corr = (
    df.select_dtypes(
        include="number"
    )
    .corr()
)

heatmap = px.imshow(
    corr,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(
    heatmap,
    use_container_width=True
)

# ---------------------
# Cluster Ranking
# ---------------------

st.subheader(
    "Cluster Ranking"
)

ranking = (
    df.groupby("Cluster")
    [
        "Spending Score (1-100)"
    ]
    .mean()
    .sort_values(
        ascending=False
    )
)

st.dataframe(
    ranking
)

# ---------------------
# Segment Distribution
# ---------------------

st.subheader(
    "Segment Distribution"
)

distribution = (
    df["Cluster"]
    .value_counts()
    .reset_index()
)

distribution.columns = [
    "Cluster",
    "Customers"
]

fig = px.bar(
    distribution,
    x="Cluster",
    y="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------
# Executive Insights
# ---------------------

st.subheader(
    "Executive Summary"
)

for insight in generate_insights(df):

    st.success(
        insight
    )

# ---------------------
# Segment Names
# ---------------------

st.subheader(
    "Auto Generated Segment Names"
)

segment_df = {
    "Cluster": [],
    "Segment Name": []
}

for cluster, name in segment_names.items():

    segment_df["Cluster"].append(
        cluster
    )

    segment_df["Segment Name"].append(
        name
    )

st.dataframe(
    segment_df
)