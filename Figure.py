

class Figure:
    name = None
    area = None
    perimeter = None

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name of the {type(self)} must be of type 'str' bur received type '{type(name)}'.")


    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise TypeError(f"Expected to receive the argument of type 'Figure', but received type '{type(figure)}'.")
        return self.area + figure.area
