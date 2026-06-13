def generate_insights(df):

    insights = []

    highest_income_cluster = (
        df.groupby("Cluster")
        ["Annual Income (k$)"]
        .mean()
        .idxmax()
    )

    highest_spending_cluster = (
        df.groupby("Cluster")
        ["Spending Score (1-100)"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"Cluster {highest_income_cluster} has the highest average income."
    )

    insights.append(
        f"Cluster {highest_spending_cluster} has the highest spending score."
    )

    insights.append(
        f"Total Customers Analyzed: {len(df)}"
    )

    return insights