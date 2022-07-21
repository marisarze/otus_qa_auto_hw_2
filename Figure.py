

class Figure:
    _name = None
    _perimeter = None
    _area = None

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f"Name of the Figure instance must be of type 'str' bur received type {type(name)}.")
        self._name = name


    def add_area(self, other):
        if not isinstance(other, Figure):
            raise TypeError(f"Expected to receive the argument of type 'Figure' or its descendants, but received type {type(other)}.")
        return self.area + other.area

    
    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError(f"Name of the Figure instance must be of type 'str' bur received type {type(new_name)}.")
        self._name = new_name


    @property
    def perimeter(self):
        return self._perimeter


    @perimeter.setter
    def perimeter(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Perimeter value type must be 'float' or 'int' but received type {type(value)}.")
        if value < 0:
            raise ValueError(f"Perimeter value must be non-negative.")
        self._perimeter = value

    
    @property
    def area(self):
        return self._area

    
    @area.setter
    def area(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Area value type must be 'float' or 'int' but received type {type(value)}.")
        if value < 0:
            raise ValueError(f"Area value must be non-negative.")
        self._area = value


