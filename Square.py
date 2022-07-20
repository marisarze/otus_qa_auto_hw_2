from Figure import Figure


class Square(Figure):

    def __init__(self, name, side):
        super().__init__(name)
        if not isinstance(side, (float, int)):
            raise TypeError(f"A side of the square must be 'float' or 'int' type but received {type(side)}.")
        if side < 0:
            raise ValueError("The lengths of all square sides must not be negative.")
        self.side = side

    
    @property
    def perimeter(self):
        return 4*self.side


    @property
    def area(self):
        return self.side**2


    @perimeter.setter
    def perimeter(self, value):
        pass


    @area.setter
    def area(self, value):
        pass
