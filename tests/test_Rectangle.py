import pytest
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Figure import Figure
from Rectangle import Rectangle
from fixtures import arbitrary_class


def test_init_positive():
    rectangle = Rectangle("some rectangle", 4, 5)
    assert isinstance(rectangle, Figure)
    assert rectangle.name == "some rectangle"
    assert rectangle.perimeter == 18
    assert rectangle.area == 20


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        rectangle = Rectangle(arbitrary_class, 4, 5)
    expected = f"Name of the Figure instance must be of type 'str' bur received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(TypeError) as e:
        rectangle = Rectangle("bad rectangle", arbitrary_class, 4)
    expected = f"side1 of the rectangle must be 'float' or 'int' type but received {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        rectangle = Rectangle("new rectangle", -4, 5)
    expected = "The lengths of all rectangle sides must not be negative."
    result = e.value.args[0]
    assert result == expected
    

def test_add_area_method_positive():
    rectangle = Rectangle("rectangle", 8, 10)
    figure = Figure("figure name")
    figure.area = 15
    result = rectangle.add_area(figure)
    assert result == 95


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        rectangle = Rectangle("nice rectangle", 5, 7)
        dummy = rectangle.add_area(arbitrary_class)
    expected = f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected


def test_set_name_negative():
    with pytest.raises(AttributeError) as e:
        rectangle = Rectangle("rectangle", 1, 2)
        rectangle.name = "free name"
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected


def test_set_perimeter_negative():
    with pytest.raises(AttributeError) as e:
        rectangle = Rectangle("rectangle", 1, 2)
        rectangle.perimeter = 67
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected


def test_set_area_negative():
    with pytest.raises(AttributeError) as e:
        rectangle = Rectangle("rectangle", 2, 3)
        rectangle.area = 56
    expected = "can't set attribute"
    result = e.value.args[0]
    assert result == expected
