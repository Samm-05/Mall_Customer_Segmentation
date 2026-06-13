import pandas as pd
import joblib

from config.settings import (
    DATA_PATH,
    MODELS_DIR
)


def get_customer_data():

    df = pd.read_csv(
        DATA_PATH
    )

    return df


def get_model():

    model = joblib.load(
        MODELS_DIR /
        "kmeans.pkl"
    )

    return model


def get_scaler():

    scaler = joblib.load(
        MODELS_DIR /
        "scaler.pkl"
    )

    return scaler