
import pytest
import systemflow as sf


def test_with_in_limit_lower():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=0, upper_limit=None)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=None, upper_limit=None)

    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="to limits")
    a_to_b()
    assert 0 == stock_a.value
    assert 10 == stock_b.value

def test_with_in_limit_upper():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=None, upper_limit=None)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=None, upper_limit=10)

    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="to limits")
    a_to_b()
    assert 0 == stock_a.value
    assert 10 == stock_b.value

def test_with_in_limit_both():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=0, upper_limit=10)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=0, upper_limit=10)

    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="to limits")
    a_to_b()
    assert 0 == stock_a.value
    assert 10 == stock_b.value

def test_with_shut():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=0, upper_limit=10)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=0, upper_limit=10)
    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="shut")
    a_to_b()
    assert 5 == stock_a.value
    assert 5 == stock_b.value

def test_ignore():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=0, upper_limit=10)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=0, upper_limit=10)
    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="ignore")
    a_to_b()
    assert -5 == stock_a.value
    assert 15 == stock_b.value

def test_with_raise():
    stock_a = sf.Stock("A", initial_value=5, lower_limit=0, upper_limit=10)
    stock_b = sf.Stock("B", initial_value=5, lower_limit=0, upper_limit=10)
    a_to_b = sf.Flow(stock_a, stock_b, valve=10, at_limit="raise")

    with pytest.raises(sf.exceptions.FlowOver) as e_info:
        a_to_b()