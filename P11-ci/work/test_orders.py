"Tests for orders.py."

import pytest

from orders import is_valid_order, minutes_per_km


def test_minutes_per_km():
    assert minutes_per_km(30, 10) == 3.0


def test_zero_distance_raises():
    with pytest.raises(ValueError):
        minutes_per_km(30, 0)


def test_good_order():
    assert is_valid_order({"distance_km": 5.0, "prep_time_min": 20,
                           "traffic_level": 2, "rain": 0})


def test_bad_traffic():
    assert not is_valid_order({"distance_km": 5.0,
                               "prep_time_min": 20,
                               "traffic_level": 9, "rain": 0})
