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
    figure = Figure("some figure")
    assert figure.name == "some figure"
    assert figure.perimeter == None
    assert figure.area == None


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        figure = Figure(arbitrary_class)
    expected = f"Name of the Figure instance must be of type 'str' bur received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected


def test_set_perimeter_positive():
    figure = Figure("awesome figure")
    figure.perimeter = 10


def test_set_perimeter_negative():
    figure = Figure("awesome figure")
    with pytest.raises(TypeError) as e:
        figure.perimeter = arbitrary_class
    expected = f"Perimeter value type must be 'float' or 'int' but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        figure.perimeter = -345
    expected = f"Perimeter value must be non-negative."
    result = e.value.args[0]
    assert result == expected
    

def test_get_perimeter():
    figure = Figure("another figure")
    assert figure.perimeter == None
    figure.perimeter = 45
    assert figure.perimeter == 45


def test_set_area_positive():
    figure = Figure("awesome figure")
    figure.area = 23


def test_set_area_negative():
    figure = Figure("awesome figure")
    with pytest.raises(TypeError) as e:
        figure.area = arbitrary_class
    expected = f"Area value type must be 'float' or 'int' but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected

    with pytest.raises(ValueError) as e:
        figure.area = -78
    expected = f"Area value must be non-negative."
    result = e.value.args[0]
    assert result == expected
    

def test_get_area():
    figure = Figure("another figure")
    assert figure.perimeter == None
    figure.perimeter = 3
    assert figure.perimeter == 3


def test_add_area_method_positive():
    figure = Figure("")
    figure.area = 10
    circle = Circle("circle", 1)
    result = figure.add_area(circle)
    assert result == 10 + math.pi


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        figure = Figure("")
        dummy = figure.add_area(arbitrary_class)
    expected = f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(arbitrary_class)}."
    result = e.value.args[0]
    assert result == expected
