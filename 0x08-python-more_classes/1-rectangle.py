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
