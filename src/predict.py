import numpy as np
import joblib

from config.settings import (
    MODELS_DIR
)


def predict_customer(
        age,
        income,
        spending):

    scaler = joblib.load(
        MODELS_DIR /
        "scaler.pkl"
    )

    model = joblib.load(
        MODELS_DIR /
        "kmeans.pkl"
    )

    sample = np.array(
        [
            [
                age,
                income,
                spending
            ]
        ]
    )

    sample = scaler.transform(
        sample
    )

    prediction = model.predict(
        sample
    )

    return prediction[0]