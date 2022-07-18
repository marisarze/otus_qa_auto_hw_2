from Figure import Figure


class Square(Figure):

    def __init__(self, name, side):
        super().__init__(name)
        if side < 0:
            raise ValueError("The lengths of all square sides must not be negative.")
        self.side = side
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    
    def calculate_perimeter(self):
        return 4*self.side

    def calculate_area(self):
        return self.side**2

