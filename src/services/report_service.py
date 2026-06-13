import pandas as pd


def generate_cluster_report(df):

    report = (
        df.groupby(
            "Cluster"
        )
        .agg(
            {
                "Age": "mean",
                "Annual Income (k$)": "mean",
                "Spending Score (1-100)": "mean"
            }
        )
        .round(2)
    )

    return report