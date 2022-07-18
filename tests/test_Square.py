import pytest
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Figure import Figure
from Square import Square
from fixtures import arbitrary_class


def test_attributes_positive():
    assert Square.name == None
    assert Square.perimeter == None
    assert Square.area == None


def test_init_positive():
    square = Square("some square", 5)
    assert isinstance(square, Figure)
    assert square.name == "some square"
    assert square.perimeter == 20
    assert square.area == 25


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        square = Square(arbitrary_class, 4)
    expected = f"Name of the Figure instance must be of type 'str' bur received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        square = Square("new square", -4)
    expected = "The lengths of all square sides must not be negative."
    result = e.value.args[0]
    assert result == expected
    

def test_add_area_method_positive():
    square = Square("square", 10)
    figure = Figure("figure name")
    figure.area = 15
    result = square.add_area(figure)
    assert result == 115


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        square = Square("nice square", 7)
        dummy = square.add_area(arbitrary_class)
    expected = f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

