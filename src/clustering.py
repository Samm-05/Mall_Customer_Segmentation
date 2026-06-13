from sklearn.cluster import (
    KMeans,
    DBSCAN,
    AgglomerativeClustering
)

from config.settings import (
    RANDOM_STATE,
    N_CLUSTERS
)


def train_kmeans(X):

    model = KMeans(
        n_clusters=N_CLUSTERS,
        random_state=RANDOM_STATE,
        n_init=10
    )

    labels = model.fit_predict(X)

    return model, labels


def train_dbscan(X):

    model = DBSCAN(
        eps=0.8,
        min_samples=5
    )

    labels = model.fit_predict(X)

    return model, labels


def train_hierarchical(X):

    model = AgglomerativeClustering(
        n_clusters=N_CLUSTERS
    )

    labels = model.fit_predict(X)

    return model, labels