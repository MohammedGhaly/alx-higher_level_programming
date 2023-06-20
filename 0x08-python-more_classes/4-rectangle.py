#!/usr/bin/python3
"""
module containing Rectangle class
"""


class Rectangle:
    """class that represents a Rectangle shape"""

    def __init__(self, width=0, height=0):
        '''default init to initialize instances'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''a property to return the value of width'''

        return self.__width

    @property
    def height(self):
        '''a property to return the value of height'''

        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''returns the perimeter of the rectangle'''

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """overrides the __str__ method"""
        if self.width == 0 or self.height == 0:
            return ''

        rect = (('#' * self.width) + '\n') * self.height
        return rect[:-1]

    def __repr__(self):
        '''returns the class representation'''
        return f'Rectangle({self.width}, {self.height})'
