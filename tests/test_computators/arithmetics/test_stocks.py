
import pytest
import systemflow as sf


def test_addition():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)
    comp = sf.computators.AddComputator(a, b)
    assert 5+5 == comp()

def test_subsraction():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)
    comp = sf.computators.SubComputator(a, b)
    assert 2-8 == comp()

def test_multiplication():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)
    comp = sf.computators.MulComputator(a, b)
    assert 2*8 == comp()

def test_division():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)
    comp = sf.computators.DivComputator(a, b)
    assert 2/8 == comp()

def test_power():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)
    comp = sf.computators.PowComputator(a, b)
    assert 2**8 == comp()
