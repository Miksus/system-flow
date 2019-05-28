
import pytest
import systemflow as sf
from systemflow.core.computator import AddComputator, SubComputator, DivComputator, MulComputator

def test_addition():
    a = 2
    b = 8
    comp = AddComputator(a, b)
    assert 2+8 == comp()

def test_subsraction():
    a = 2
    b = 8
    comp = SubComputator(a, b)
    assert 2-8 == comp()

def test_multiplication():
    a = 2
    b = 8
    comp = MulComputator(a, b)
    assert 2*8 == comp()

def test_division():
    a = 2
    b = 8
    comp = DivComputator(a, b)
    assert 2/8 == comp()

def test_power():
    a = 2
    b = 8
    comp = PowComputator(a, b)
    assert 2**8 == comp()
