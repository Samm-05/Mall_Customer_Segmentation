from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "Mall_Customers.csv"

MODELS_DIR = BASE_DIR / "models"

OUTPUTS_DIR = BASE_DIR / "outputs"

ASSETS_DIR = BASE_DIR / "assets"

N_CLUSTERS = 5

RANDOM_STATE = 42

SEGMENT_NAMES = {
    0: "Premium Customers",
    1: "Budget Customers",
    2: "Regular Customers",
    3: "Young Spenders",
    4: "Luxury Customers"
}