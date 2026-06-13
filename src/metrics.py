from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)


def evaluate_model(X, labels):

    scores = {}

    scores["silhouette"] = round(
        silhouette_score(X, labels),
        3
    )

    scores["davies_bouldin"] = round(
        davies_bouldin_score(X, labels),
        3
    )

    scores["calinski"] = round(
        calinski_harabasz_score(X, labels),
        3
    )

    return scores