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

from src.services.report_service import (
    generate_cluster_report
)

from src.auth_guard import (
    protect_page
)

protect_page()

st.title(
    "Business Insights"
)

df, X, labels = get_clustered_data()

report = generate_cluster_report(
    df
)

st.dataframe(
    report,
    use_container_width=True
)

st.markdown("---")

best_cluster = report[
    "Spending Score (1-100)"
].idxmax()

st.success(
    f"Highest Spending Segment: Cluster {best_cluster}"
)