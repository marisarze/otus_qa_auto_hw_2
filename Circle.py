import math
from Figure import Figure


class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        if radius < 0:
            raise ValueError("The lengths of all circle sides must not be negative.")
        self.radius = radius

    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


    @property
    def area(self):
        return math.pi * self.radius**2
