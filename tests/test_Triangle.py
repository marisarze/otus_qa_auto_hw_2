import pytest
import math
from ..Triangle import Triangle

@pytest.fixture
def arbitrary_class():
    class A: pass
    return A


def test_attributes_positive():
    assert Triangle.name == None
    assert Triangle.perimeter == None
    assert Triangle.area == None


def test_init_positive():
    triangle = Triangle("some triangle", 3, 4, 5)
    assert triangle.name == "some triangle"
    assert triangle.perimeter == 12
    assert triangle.area == 6


def test_init_negative(arbitrary_class):
    with pytest.raises(TypeError) as e:
        figure = Triangle(arbitrary_class(), 3, 4, 5)
    assert e.value == "Name of the Triangle must be of type 'str' bur received type 'A'."
    


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