#!/usr/bin/python3
"""
module containing Rectangle class
"""


class Rectangle:
    """class that represents a Rectangle shape"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''default init to initialize instances'''
        Rectangle.number_of_instances += 1
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

        rect = (str(self.print_symbol) * self.width + '\n') * self.height
        return rect[:-1]

    def __repr__(self):
        '''returns the class representation'''
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        '''executed before deleting the objects of this class'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the rectangle object with the larger area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area2 > area1:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
