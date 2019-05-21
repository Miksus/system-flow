import pytest

import systemflow as sf

def test_increment():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    stock += 2
    assert stock.value == 7

def test_decrement():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    stock -= 2
    assert stock.value == 3


def test_increment_to_limit():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    stock += 5
    assert stock.value == 10

def test_decrement_to_limit():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    stock -= 5
    assert stock.value == 0


def test_increment_over_limit():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    with pytest.raises(sf.exceptions.OutOfLimitsError) as e_info:
        stock += 6

def test_decrement_under_limit():
    stock = sf.Stock("test", initial_value=5, lower_limit=0, upper_limit=10)
    with pytest.raises(sf.exceptions.OutOfLimitsError) as e_info:
        stock -= 6

