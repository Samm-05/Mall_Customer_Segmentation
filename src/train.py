import joblib

from config.settings import (
    MODELS_DIR
)

from src.preprocess import preprocess_data

from src.clustering import (
    train_kmeans
)


def train_model():

    df, X = preprocess_data()

    model, labels = train_kmeans(X)

    df["Cluster"] = labels

    MODELS_DIR.mkdir(
        exist_ok=True
    )

    joblib.dump(
        model,
        MODELS_DIR / "kmeans.pkl"
    )

    return df, X, labels