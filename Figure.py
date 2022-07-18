

class Figure:
    name = None
    area = None
    perimeter = None

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name of the Figure instance must be of type 'str' bur received type {type(name)}.")
        self.name = name


    def add_area(self, other):
        if not isinstance(other, Figure):
            raise TypeError(f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(other)}.")
        return self.area + other.area
