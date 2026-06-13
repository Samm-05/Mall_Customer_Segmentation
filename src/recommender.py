def get_cluster_name(cluster):

    cluster_names = {

        0: "Premium Customers",

        1: "Budget Customers",

        2: "Regular Customers",

        3: "Young Spenders",

        4: "Luxury Customers"
    }

    return cluster_names.get(
        cluster,
        f"Cluster {cluster}"
    )


def get_recommendation(cluster):

    recommendations = {

        0:
        """
        • VIP Membership Program

        • Premium Product Promotion

        • Exclusive Early Access
        """,

        1:
        """
        • Discount Coupons

        • Bundle Offers

        • Cashback Rewards
        """,

        2:
        """
        • Personalized Offers

        • Loyalty Program

        • Referral Rewards
        """,

        3:
        """
        • Social Media Campaigns

        • Trend Based Products

        • Flash Sales
        """,

        4:
        """
        • Luxury Products

        • Exclusive Events

        • Premium Membership
        """
    }

    return recommendations.get(
        cluster,
        "No Recommendation Available"
    )