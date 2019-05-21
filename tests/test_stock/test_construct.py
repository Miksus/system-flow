import pytest

import systemflow as sf

def test_add():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a + b
    assert isinstance(new, sf.computators.AddComputator)
    assert new() == 2 + 8
    assert a.value == 2
    assert b.value == 8

def test_sub():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a - b
    assert isinstance(new, sf.computators.SubComputator)
    assert new() == 2 - 8
    assert a.value == 2
    assert b.value == 8

def test_multiply():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a * b
    assert isinstance(new, sf.computators.MulComputator)
    assert new() == 2 * 8
    assert a.value == 2
    assert b.value == 8

def test_divide():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a / b
    assert isinstance(new, sf.computators.DivComputator)
    assert new() == 2 / 8
    assert a.value == 2
    assert b.value == 8

def test_to_flow():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a >> b
    assert isinstance(new, sf.Flow)
    # Test the flow has input & output correctly
    assert new.input is a
    assert new.output is b
    # Test the flow did not change values just in case
    assert a.value == 2
    assert b.value == 8