import pandas as pd


def auto_name_segments(df):

    segment_names = {}

    cluster_summary = (
        df.groupby("Cluster")
        .agg({
            "Annual Income (k$)": "mean",
            "Spending Score (1-100)": "mean",
            "Age": "mean"
        })
    )

    for cluster, row in cluster_summary.iterrows():

        income = row["Annual Income (k$)"]
        spending = row["Spending Score (1-100)"]
        age = row["Age"]

        if income > 70 and spending > 70:
            name = "Luxury Customers"

        elif income > 70 and spending < 40:
            name = "Affluent Savers"

        elif age < 35 and spending > 60:
            name = "Young Spenders"

        elif income < 40 and spending < 40:
            name = "Budget Customers"

        else:
            name = "Regular Customers"

        segment_names[cluster] = name

    return segment_names