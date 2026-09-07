"""Training, scoring, saving and loading the model."""

import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


def train_model(X_train, y_train):
    """Fit a linear regression and hand it back."""
    return LinearRegression().fit(X_train, y_train)


def evaluate(model, X_test, y_test):
    """Mean absolute error, in minutes."""
    return mean_absolute_error(y_test, model.predict(X_test))


def save_model(model, path):
    """Write a trained model to disk."""
    joblib.dump(model, path)
    return path


def load_model(path):
    """Read a trained model back from disk."""
    return joblib.load(path)
