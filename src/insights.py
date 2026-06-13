import pandas as pd


def cluster_summary(df):

    summary = df.groupby(
        "Cluster"
    ).agg(
        {
            "Age": "mean",
            "Annual Income (k$)": "mean",
            "Spending Score (1-100)": "mean"
        }
    )

    return summary.round(2)