

class Figure:
    __name = None
    __perimeter = None
    __area = None

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name of the Figure instance must be of type 'str' bur received type {type(name)}.")
        self.__name = name


    def add_area(self, other):
        if not isinstance(other, Figure):
            raise TypeError(f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(other)}.")
        return self.area + other.area

    
    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError(f"Name of the Figure instance must be of type 'str' bur received type {type(new_name)}.")
        self.__name = new_name


    @property
    def perimeter(self):
        return self.__perimeter


    @perimeter.setter
    def perimeter(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Perimeter value type must be 'float' or 'int' but received type {type(value)}.")
        if value < 0:
            raise ValueError(f"Perimeter value must be non-negative.")
        self.__perimeter = value

    
    @property
    def area(self):
        return self.__area

    
    @area.setter
    def area(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Area value type must be 'float' or 'int' but received type {type(value)}.")
        if value < 0:
            raise ValueError(f"Area value must be non-negative.")
        self.__area = value


