import pandas as pd


def search_by_customer_id(df, customer_id):

    result = df[
        df["CustomerID"] == customer_id
    ]

    return result


def search_by_cluster(df, cluster):

    result = df[
        df["Cluster"] == cluster
    ]

    return result


def search_by_income(df, min_income, max_income):

    result = df[
        (
            df["Annual Income (k$)"]
            >= min_income
        )
        &
        (
            df["Annual Income (k$)"]
            <= max_income
        )
    ]

    return result


def search_by_spending(df, min_spending, max_spending):

    result = df[
        (
            df["Spending Score (1-100)"]
            >= min_spending
        )
        &
        (
            df["Spending Score (1-100)"]
            <= max_spending
        )
    ]

    return result