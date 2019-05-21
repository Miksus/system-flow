import pytest

import systemflow as sf


@pytest.fixture(scope="function")
def stock_a():
    return sf.Stock("A", initial_value=10, lower_limit=None, upper_limit=None)

@pytest.fixture(scope="function")
def stock_b():
    return sf.Stock("B", initial_value=10, lower_limit=None, upper_limit=None)
    

def test_zero_flow(stock_a, stock_b):
    a_to_b = sf.Flow(stock_a, stock_b, valve=0)
    a_to_b()
    assert 10 == stock_a.value
    assert 10 == stock_b.value

def test_fixed_flow(stock_a, stock_b):
    a_to_b = sf.Flow(stock_a, stock_b, valve=5)
    a_to_b()
    assert 5 == stock_a.value
    assert 15 == stock_b.value

def test_fixed_flow_negative(stock_a, stock_b):
    a_to_b = sf.Flow(stock_a, stock_b, valve=-5)
    a_to_b()
    assert 15 == stock_a.value
    assert 5 == stock_b.value
