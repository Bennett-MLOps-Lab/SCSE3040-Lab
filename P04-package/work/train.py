"""Train the delivery-time model and report its error."""

import sys
from pathlib import Path

from delivery import (evaluate, load_orders, save_model,
                      split_orders, train_model)


HERE = Path(__file__).resolve().parent
DEFAULT_DATA = HERE.parent.parent / "data" / "delivery_times.csv"


def main():
    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DATA

    orders = load_orders(data_path)
    X_train, X_test, y_train, y_test = split_orders(orders)
    model = train_model(X_train, y_train)
    mae = evaluate(model, X_test, y_test)

    save_model(model, Path(__file__).parent / "model.joblib")

    print(f"rows: {len(orders)}")
    print(f"MAE: {mae:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
