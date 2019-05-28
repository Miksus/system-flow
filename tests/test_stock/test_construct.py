import pytest

import systemflow as sf
from systemflow.core.computator import AddComputator, SubComputator, DivComputator, MulComputator
def test_add():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a + b
    assert isinstance(new, AddComputator)
    assert new() == 2 + 8
    assert a.value == 2
    assert b.value == 8

def test_sub():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a - b
    assert isinstance(new, SubComputator)
    assert new() == 2 - 8
    assert a.value == 2
    assert b.value == 8

def test_multiply():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a * b
    assert isinstance(new, MulComputator)
    assert new() == 2 * 8
    assert a.value == 2
    assert b.value == 8

def test_divide():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = a / b
    assert isinstance(new, DivComputator)
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

def test_to_flow_rev():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    b = sf.Stock("B", initial_value=8, lower_limit=0, upper_limit=10)

    new = b << a
    assert isinstance(new, sf.Flow)
    # Test the flow has input & output correctly
    assert new.input is a
    assert new.output is b
    # Test the flow did not change values just in case
    assert a.value == 2
    assert b.value == 8


def test_to_inflow():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    new = a << None
    assert isinstance(new, sf.flow.InFlow)
    assert 2 == a.value

def test_to_outflow():
    b = sf.Stock("B", initial_value=2, lower_limit=0, upper_limit=10)
    new = b >> None
    assert isinstance(new, sf.flow.OutFlow)
    assert 2 == b.value


def test_to_inflow_rev():
    a = sf.Stock("A", initial_value=2, lower_limit=0, upper_limit=10)
    new = None >> a
    assert isinstance(new, sf.flow.InFlow)
    assert 2 == a.value

def test_to_outflow_rev():
    b = sf.Stock("B", initial_value=2, lower_limit=0, upper_limit=10)
    new = None << b
    assert isinstance(new, sf.flow.OutFlow)
    assert 2 == b.value