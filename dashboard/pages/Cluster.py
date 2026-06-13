import streamlit as st
import plotly.express as px

from src.train import train_model

st.title(
    "Cluster Explorer"
)

df, X, labels = train_model()

selected_cluster = st.selectbox(
    "Select Cluster",
    sorted(
        df["Cluster"].unique()
    )
)

filtered_df = df[
    df["Cluster"] ==
    selected_cluster
]

st.subheader(
    f"Cluster {selected_cluster}"
)

st.write(
    f"Customers : {len(filtered_df)}"
)

fig = px.scatter(
    filtered_df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    color="Gender"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    filtered_df,
    use_container_width=True
)