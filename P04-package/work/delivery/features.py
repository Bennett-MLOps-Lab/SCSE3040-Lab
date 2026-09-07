"""Checks and descriptions for one delivery order."""

TRAFFIC_LEVELS = (1, 2, 3)


def minutes_per_km(delivery_min, distance_km):
    """How many minutes each kilometre took."""
    if distance_km <= 0:
        raise ValueError("distance_km must be positive")
    return delivery_min / distance_km


def describe_order(order):
    """A short sentence a human can read."""
    weather = "in the rain" if order["rain"] else "in dry weather"
    return (f"{order['distance_km']} km, "
            f"{order['prep_time_min']} min prep, "
            f"traffic {order['traffic_level']}, {weather}")


def average_speed_kmph(distance_km, delivery_min):
    "Average speed of a delivery, in kilometres per hour."
    return distance_km / (delivery_min / 60)
