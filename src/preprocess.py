import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os


def preprocess_data(csv_path):

    df = pd.read_csv(csv_path)

    df["Gender"] = df["Gender"].map({
        "Male": 1,
        "Female": 0
    })

    X = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    os.makedirs("models", exist_ok=True)

    joblib.dump(
        scaler,
        "models/scaler.pkl"
    )

    return df, X_scaled