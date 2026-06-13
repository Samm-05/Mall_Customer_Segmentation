import joblib
import os

from sklearn.cluster import KMeans

from src.preprocess import preprocess_data
from src.utils import generate_elbow_curve


def train_model():

    df, X_scaled = preprocess_data(
        "data/Mall_Customers.csv"
    )

    generate_elbow_curve(
        X_scaled
    )

    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(
        X_scaled
    )

    df["Cluster"] = clusters

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        "models/kmeans.pkl"
    )

    df.to_csv(
        "outputs/customer_segments.csv",
        index=False
    )

    print(
        "Training Complete"
    )


if __name__ == "__main__":
    train_model()