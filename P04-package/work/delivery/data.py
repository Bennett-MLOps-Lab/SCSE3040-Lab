"""Loading and splitting the delivery dataset."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

FEATURES = ["distance_km", "prep_time_min", "traffic_level", "rain"]
TARGET = "delivery_min"
SEED = 42


def load_orders(path):
    """Read the delivery CSV into a table."""
    return pd.read_csv(Path(path))


def split_orders(orders, test_size=0.2):
    """Return X_train, X_test, y_train, y_test."""
    X = orders[FEATURES]
    y = orders[TARGET]
    return train_test_split(X, y, test_size=test_size,
                            random_state=SEED)
