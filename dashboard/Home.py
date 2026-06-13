import streamlit as st

from src.train import train_model

st.set_page_config(
    page_title="Mall Customer Analytics",
    layout="wide"
)

st.title(
    "Mall Customer Analytics Platform"
)

df, X, labels = train_model()

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
            df[
                "Annual Income (k$)"
            ].mean(),
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
            set(labels)
        )
    )

st.markdown("---")

st.markdown(
    """
    ## Navigation

    - Customer Segmentation
    - Business Insights
    - Cluster Explorer
    - Customer Predictor
    - Model Comparison
    """
)