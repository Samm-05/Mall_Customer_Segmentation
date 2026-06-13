import streamlit as st

from src.train import train_model
from src.insights import cluster_summary

st.title(
    "Business Insights"
)

df, X, labels = train_model()

summary = cluster_summary(df)

st.subheader(
    "Cluster Statistics"
)

st.dataframe(
    summary,
    use_container_width=True
)

st.markdown("---")

for cluster in summary.index:

    st.subheader(
        f"Cluster {cluster}"
    )

    age = summary.loc[
        cluster,
        "Age"
    ]

    income = summary.loc[
        cluster,
        "Annual Income (k$)"
    ]

    spending = summary.loc[
        cluster,
        "Spending Score (1-100)"
    ]

    st.write(
        f"""
        Average Age : {age}

        Average Income : {income}

        Spending Score : {spending}
        """
    )