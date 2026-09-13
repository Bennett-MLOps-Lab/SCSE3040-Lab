"Tests for orders.py."

import pytest

from orders import is_valid_order, minutes_per_km


def test_minutes_per_km_simple():
    assert minutes_per_km(30, 10) == 3.0


def test_minutes_per_km_rejects_zero_distance():
    with pytest.raises(ValueError):
        minutes_per_km(30, 0)


def test_good_order_is_accepted():
    good = {"distance_km": 5.0, "prep_time_min": 20,
            "traffic_level": 2, "rain": 0}
    assert is_valid_order(good) is True


def test_bad_traffic_level_is_rejected():
    bad = {"distance_km": 5.0, "prep_time_min": 20,
           "traffic_level": 9, "rain": 0}
    assert is_valid_order(bad) is False
