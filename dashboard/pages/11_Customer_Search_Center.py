import sys
from pathlib import Path

ROOT_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

sys.path.append(str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from src.services.analytics_service import (
    get_clustered_data
)

from src.auth_guard import (
    protect_page,
    render_user_panel
)

protect_page()

render_user_panel()

from src.customer_search import (
    search_by_customer_id,
    search_by_cluster,
    search_by_income,
    search_by_spending
)

from src.recommender import (
    get_cluster_name,
    get_recommendation
)

st.set_page_config(
    page_title="Customer Search Center",
    layout="wide"
)

st.title(
    "🔍 Customer Search Center"
)

df, X, labels = get_clustered_data()

search_option = st.selectbox(
    "Search Method",
    [
        "Customer ID",
        "Cluster",
        "Income Range",
        "Spending Range"
    ]
)

results = None

# ===================================
# CUSTOMER ID SEARCH
# ===================================

if search_option == "Customer ID":

    customer_id = st.number_input(
        "Customer ID",
        min_value=1,
        max_value=int(
            df["CustomerID"].max()
        ),
        value=1
    )

    if st.button(
        "Search Customer"
    ):

        results = search_by_customer_id(
            df,
            customer_id
        )

# ===================================
# CLUSTER SEARCH
# ===================================

elif search_option == "Cluster":

    cluster = st.selectbox(
        "Cluster",
        sorted(
            df["Cluster"]
            .unique()
            .tolist()
        )
    )

    if st.button(
        "Search Cluster"
    ):

        results = search_by_cluster(
            df,
            cluster
        )

# ===================================
# INCOME SEARCH
# ===================================

elif search_option == "Income Range":

    min_income, max_income = st.slider(
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
            40,
            80
        )
    )

    if st.button(
        "Search Income"
    ):

        results = search_by_income(
            df,
            min_income,
            max_income
        )

# ===================================
# SPENDING SEARCH
# ===================================

else:

    min_spending, max_spending = st.slider(
        "Spending Range",
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
            40,
            80
        )
    )

    if st.button(
        "Search Spending"
    ):

        results = search_by_spending(
            df,
            min_spending,
            max_spending
        )

# ===================================
# RESULTS
# ===================================

if results is not None and not results.empty:

    st.success(
        f"Found {len(results)} customer(s)"
    )

    st.dataframe(
        results,
        use_container_width=True
    )

    # Single Customer Profile

    if len(results) == 1:

        row = results.iloc[0]

        st.markdown("---")

        st.subheader(
            "Customer Profile"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Age",
                row["Age"]
            )

        with col2:
            st.metric(
                "Income",
                row[
                    "Annual Income (k$)"
                ]
            )

        with col3:
            st.metric(
                "Spending",
                row[
                    "Spending Score (1-100)"
                ]
            )

        cluster = int(
            row["Cluster"]
        )

        st.info(
            f"Segment: {get_cluster_name(cluster)}"
        )

        st.success(
            get_recommendation(cluster)
        )

    # Multi Customer Analytics

    else:

        st.markdown("---")

        st.subheader(
            "Search Result Analytics"
        )

        fig = px.scatter(
            results,
            x="Annual Income (k$)",
            y="Spending Score (1-100)",
            color=results[
                "Cluster"
            ].astype(str),
            hover_data=[
                "Age"
            ]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

else:

    st.info(
        "Run a search to view customers."
    )