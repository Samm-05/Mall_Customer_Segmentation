def get_cluster_name(cluster):

    mapping = {

        0: "Premium Customers",

        1: "Budget Customers",

        2: "Regular Customers",

        3: "Young Spenders",

        4: "Luxury Customers"

    }

    return mapping.get(
        cluster,
        "Unknown"
    )