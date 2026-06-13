import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

from config.settings import (
    DATA_PATH,
    MODELS_DIR
)


def load_data():

    df = pd.read_csv(DATA_PATH)

    return df


def preprocess_data():

    df = load_data()

    df["Gender"] = df["Gender"].map(
        {
            "Male": 1,
            "Female": 0
        }
    )

    features = [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]

    X = df[features]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    MODELS_DIR.mkdir(exist_ok=True)

    joblib.dump(
        scaler,
        MODELS_DIR / "scaler.pkl"
    )

    return df, X_scaled