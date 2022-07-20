import pytest
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Figure import Figure
from Triangle import Triangle
from fixtures import arbitrary_class


def test_init_positive():
    triangle = Triangle("some triangle", 3, 4, 5)
    assert isinstance(triangle, Figure)
    assert triangle.name == "some triangle"
    assert triangle.perimeter == 12
    assert triangle.area == 6


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        triangle = Triangle(arbitrary_class, 3, 4, 5)
    expected = f"Name of the Figure instance must be of type 'str' bur received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(TypeError) as e:
        triangle = Triangle("bad triangle", arbitrary_class, 4, 5)
    expected = f"side1 of the triangle must be 'float' or 'int' type but received {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        triangle = Triangle("new triangle", -3, 4, 5)
    expected = "The lengths of all triangle sides must not be negative."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        triangle = Triangle("new triangle", 3, 4, 8)
    expected = "A triangle with such side lengths does not exist."
    result = e.value.args[0]
    assert result == expected


def test_add_area_method_positive():
    triangle = Triangle("triangle", 6, 8, 10)
    figure = Figure("figure name")
    figure.area = 15
    result = triangle.add_area(figure)
    assert result == 39


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        triangle = Triangle("nice triangle", 4, 5, 7)
        dummy = triangle.add_area(arbitrary_class)
    expected = f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected


def test_set_name_negative():
    with pytest.raises(AttributeError) as e:
        triangle = Triangle("triangle", 1, 2, 3)
        triangle.name = "free name"
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected


def test_set_perimeter_negative():
    with pytest.raises(AttributeError) as e:
        triangle = Triangle("triangle", 1, 2, 3)
        triangle.perimeter = 67
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected


def test_set_area_negative():
    with pytest.raises(AttributeError) as e:
        triangle = Triangle("triangle", 2, 3, 4)
        triangle.area = 56
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected