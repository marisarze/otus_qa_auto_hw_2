import math
from Figure import Figure


class Circle(Figure):

    def __init__(self, name, radius):
        super().__init__(name)
        if radius < 0:
            raise ValueError("The lengths of all circle sides must not be negative.")
        self.radius = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2
