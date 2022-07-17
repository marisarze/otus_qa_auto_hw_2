import math
from .Figure import Figure


class Circle(Figure):

    def __init__(self, name, radius):
        if radius < 0:
            raise ValueError("The lengths of all circle sides must not be negative.")
        self.radius1 = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    
    def calculate_perimeter(self):
        return 2*math.Pi*self.radius

    def calculate_area(self):
        return math.Pi * self.radius**2
