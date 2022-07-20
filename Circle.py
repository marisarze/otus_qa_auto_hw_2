import math
from Figure import Figure


class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        if not isinstance(radius, (float, int)):
            raise TypeError(f"Radius of the circle must be 'float' or 'int' type but received {type(radius)}.")
        if radius < 0:
            raise ValueError("Radius of a circle must not be negative.")
        self.radius = radius

    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


    @property
    def area(self):
        return math.pi * self.radius**2

    
    @perimeter.setter
    def perimeter(self, value):
        pass


    @area.setter
    def area(self, value):
        pass
