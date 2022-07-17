import pytest
import math
from ..Figure import Figure
from ..Circle import Circle


@pytest.fixture
def arbitrary_class():
    class A: pass
    return A


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
        figure = Figure(arbitrary_class())
    assert e.value == "Name of the Figure must be of type 'str' bur received type 'A'."
    


def test_add_area_method_positive():
    figure = Figure("")
    figure.area = 10
    circle = Circle("circle", 1)
    result = figure.add_area(circle)
    assert result == 10 + math.Pi


def test_add_area_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        figure = Figure("")
        some_variable = figure.add_area(arbitrary_class())
    assert e.value == "Expected to receive the argument of type 'Figure', but received type 'A'."
        

