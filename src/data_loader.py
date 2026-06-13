import pandas as pd
import joblib

from config.settings import (
    DATA_PATH,
    MODELS_DIR
)


def load_dataset():

    return pd.read_csv(
        DATA_PATH
    )


def load_model():

    return joblib.load(
        MODELS_DIR /
        "kmeans.pkl"
    )


def load_scaler():

    return joblib.load(
        MODELS_DIR /
        "scaler.pkl"
    )