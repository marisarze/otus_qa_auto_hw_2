
import math
from .Figure import Figure


class Triangle(Figure):

    def __init__(self, name, side1, side2, side3):
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("The lengths of all triangle sides must not be negative.")
        if side1 + side2 < side3 \
        or side1 + side3 < side2 \
        or side2 + side3 < side1:
            raise ValueError("A triangle with such side lengths does not exist.")
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3

    def calculate_area(self):
        perimeter = self.calculate_perimeter()
        return math.sqrt(perimeter*(perimeter-self.side1)*(perimeter-self.side2)*(perimeter-self.side3))