"Shared setup for every test in this folder."

from pathlib import Path

import pandas as pd
import pytest
import yaml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

HERE = Path(__file__).resolve().parent


@pytest.fixture(scope="session")
def config():
    with open(HERE / "config.yaml", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


@pytest.fixture(scope="session")
def split(config):
    data_path = HERE.parent.parent / "data" / "delivery_times.csv"
    orders = pd.read_csv(data_path)
    X = orders[config["data"]["features"]]
    y = orders[config["data"]["target"]]
    return train_test_split(
        X, y,
        test_size=config["split"]["test_size"],
        random_state=config["split"]["seed"],
    )


@pytest.fixture(scope="session")
def trained_model(split):
    X_tr, _, y_tr, _ = split
    return LinearRegression().fit(X_tr, y_tr)


@pytest.fixture(scope="session")
def model_mae(trained_model, split):
    _, X_te, _, y_te = split
    return mean_absolute_error(y_te, trained_model.predict(X_te))


@pytest.fixture(scope="session")
def baseline_mae(split):
    _, X_te, y_tr, y_te = split
    guess = [y_tr.mean()] * len(y_te)
    return mean_absolute_error(y_te, guess)
