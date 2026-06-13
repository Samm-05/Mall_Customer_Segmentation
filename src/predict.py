import numpy as np
import joblib


def predict_customer(
        age,
        income,
        spending_score):

    scaler = joblib.load(
        "models/scaler.pkl"
    )

    model = joblib.load(
        "models/kmeans.pkl"
    )

    sample = np.array(
        [[
            age,
            income,
            spending_score
        ]]
    )

    sample_scaled = scaler.transform(
        sample
    )

    cluster = model.predict(
        sample_scaled
    )

    return cluster[0]


if __name__ == "__main__":

    result = predict_customer(
        25,
        80,
        90
    )

    print(
        f"Cluster : {result}"
    )