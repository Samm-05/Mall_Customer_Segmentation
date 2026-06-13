import pandas as pd


def apply_filters(
    df,
    age_range,
    income_range,
    spending_range,
    genders,
    clusters
):

    filtered_df = df.copy()

    filtered_df = filtered_df[
        (
            filtered_df["Age"]
            >= age_range[0]
        )
        &
        (
            filtered_df["Age"]
            <= age_range[1]
        )
    ]

    filtered_df = filtered_df[
        (
            filtered_df[
                "Annual Income (k$)"
            ]
            >= income_range[0]
        )
        &
        (
            filtered_df[
                "Annual Income (k$)"
            ]
            <= income_range[1]
        )
    ]

    filtered_df = filtered_df[
        (
            filtered_df[
                "Spending Score (1-100)"
            ]
            >= spending_range[0]
        )
        &
        (
            filtered_df[
                "Spending Score (1-100)"
            ]
            <= spending_range[1]
        )
    ]

    if genders:

        filtered_df = filtered_df[
            filtered_df["Gender"]
            .isin(genders)
        ]

    if clusters:

        filtered_df = filtered_df[
            filtered_df["Cluster"]
            .isin(clusters)
        ]

    return filtered_df