
import pytest
import systemflow as sf


def test_addition():
    a = 2
    b = 8
    comp = sf.computators.AddComputator(a, b)
    assert 2+8 == comp()

def test_subsraction():
    a = 2
    b = 8
    comp = sf.computators.SubComputator(a, b)
    assert 2-8 == comp()

def test_multiplication():
    a = 2
    b = 8
    comp = sf.computators.MulComputator(a, b)
    assert 2*8 == comp()

def test_division():
    a = 2
    b = 8
    comp = sf.computators.DivComputator(a, b)
    assert 2/8 == comp()

def test_power():
    a = 2
    b = 8
    comp = sf.computators.PowComputator(a, b)
    assert 2**8 == comp()
