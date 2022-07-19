
import math
from Figure import Figure


class Triangle(Figure):

    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        if side1 < 0 or side2 < 0 or side3 < 0:
            raise ValueError("The lengths of all triangle sides must not be negative.")
        if side1 + side2 < side3 \
        or side1 + side3 < side2 \
        or side2 + side3 < side1:
            raise ValueError("A triangle with such side lengths does not exist.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


    @property
    def perimeter(self):
        if hasattr(self, "side1") and hasattr(self, "side2") and hasattr(self, "side3"):
            return self.side1+self.side2+self.side3
        return None


    @property
    def area(self):
        if hasattr(self, "side1") and hasattr(self, "side2") and hasattr(self, "side3"):
            half_perimeter = self.perimeter/2
            return math.sqrt(half_perimeter*(half_perimeter-self.side1)*(half_perimeter-self.side2)*(half_perimeter-self.side3))
        return None

