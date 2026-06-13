import streamlit as st

from src.preprocess import (
    preprocess_data
)

from src.clustering import (
    train_kmeans,
    train_dbscan,
    train_hierarchical
)

from src.metrics import (
    evaluate_model
)

st.title(
    "Model Comparison"
)

df, X = preprocess_data()

models = {}

kmeans, labels = train_kmeans(X)

models["KMeans"] = evaluate_model(
    X,
    labels
)

hierarchical, labels = train_hierarchical(X)

models["Hierarchical"] = evaluate_model(
    X,
    labels
)

dbscan, labels = train_dbscan(X)

if len(set(labels)) > 1:

    models["DBSCAN"] = evaluate_model(
        X,
        labels
    )

st.dataframe(
    models,
    use_container_width=True
)