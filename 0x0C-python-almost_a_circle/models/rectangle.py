#!/usr/bin/python3

"""
module that contains class 'rectangle'
"""

from models.base import Base


class Rectangle(Base):
    """
    rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """x coordinate setter"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """y coordinate setter"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validates the value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """calculates the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """overrides the __str__ method"""
        return f"""[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"""

    def display(self):
        """prints the rectangle in '#' symbols"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """internal method updates the values of rectangle attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        """public method to update rectangle attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {'x': self.x, 'y': self.y, 'width': self.width,
               'height': self.height, 'id': self.id}
        return dic
