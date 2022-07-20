from Figure import Figure


class Rectangle(Figure):

    def __init__(self, name, side1, side2):
        super().__init__(name)
        if side1 < 0 or side2 < 0:
            raise ValueError("The lengths of all rectangle sides must not be negative.")
        self.side1 = side1
        self.side2 = side2

    
    @property
    def perimeter(self):
        return 2*(self.side1+self.side2)


    @property
    def area(self):
        return self.side1*self.side2


    @perimeter.setter
    def perimeter(self, value):
        pass


    @area.setter
    def area(self, value):
        pass