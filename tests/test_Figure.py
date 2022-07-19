import pytest
import math
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Figure import Figure
from Circle import Circle
from fixtures import arbitrary_class


def test_attributes_positive():
    assert Figure.name == None
    assert Figure.perimeter == None
    assert Figure.area == None


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
