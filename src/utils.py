import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os


def generate_elbow_curve(X_scaled):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    wcss = []

    for i in range(1, 11):

        model = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        wcss.append(
            model.inertia_
        )

    plt.figure(figsize=(8, 5))

    plt.plot(
        range(1, 11),
        wcss,
        marker="o"
    )

    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")

    plt.savefig(
        "outputs/elbow.png"
    )

    plt.close()