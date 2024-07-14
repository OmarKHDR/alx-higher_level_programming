add_integer = __import__('0-add_integer').add_integer
import pytest
import unittest

def test_negative():
    assert add_integer(-4,-1) == -5
    assert add_integer(-10,-10) == -20


def test_positive():
    assert add_integer(1,12) == 13
    assert add_integer(10,10) == 20

def test_zero():
    assert add_integer(0,4) == 4
    assert add_integer(4,0) == 4
    assert add_integer(0,0) == 0

def test_pos_nig():
    assert add_integer(-10,10) == 0
    assert add_integer(-1,11) == 10
    assert add_integer(-11,1) == -10

def test_input():
    with pytest.raises(TypeError):
        add_integer("a","b")
        add_integer(3,"b")
        add_integer("a",3)
    
