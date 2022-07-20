import pytest
import math
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Figure import Figure
from Circle import Circle
from fixtures import arbitrary_class


def test_init_positive():
    circle = Circle("some circle", 3)
    assert isinstance(circle, Figure)
    assert circle.name == "some circle"
    assert circle.perimeter == 6 * math.pi
    assert circle.area == 9 * math.pi


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        circle = Circle(arbitrary_class, 4)
    expected = f"Name of the Figure instance must be of type 'str' bur received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        circle = Circle("new circle", -4)
    expected = "The lengths of all circle sides must not be negative."
    result = e.value.args[0]
    assert result == expected


def test_set_perimeter_do_not_matter():
    circle = Circle("awesome circle", 5)
    circle.perimeter = 1
    assert circle.perimeter == 10 * math.pi


def test_set_area_do_not_matter():
    circle = Circle("awesome circle", 6)
    circle.area = 5
    assert circle.area == 36 * math.pi
    

def test_add_area_method_positive():
    circle = Circle("circle", 7)
    figure = Figure("figure name")
    figure.area = 100
    result = circle.add_area(figure)
    assert result == 100 + 49 * math.pi


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        circle = Circle("nice circle", 7)
        dummy = circle.add_area(arbitrary_class)
    expected = f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

