"Helpers for delivery orders."

TRAFFIC_LEVELS = (1, 2, 3)


def minutes_per_km(delivery_min, distance_km):
    "How many minutes each kilometre took."
    if distance_km <= 0:
        raise ValueError("distance_km must be positive")
    return delivery_min / distance_km


def is_valid_order(order):
    "True if this order is usable for training."
    return (order.get("distance_km", 0) > 0
            and order.get("prep_time_min", 0) >= 0
            and order.get("traffic_level") in TRAFFIC_LEVELS
            and order.get("rain") in (0, 1))
