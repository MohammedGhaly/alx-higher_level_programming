#!/usr/bin/python3
"""
contains 'BaseGeometry' class
"""


class BaseGeometry:
    """
    class that represents a basic geometric shape
    """

    def area(self):
        """
        calculates the area of the geometric shape if it is valid
        raises an Exception otherwise
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates value:
        raises a TypeError exception if not integer,
        raises a ValueError exception if value is less than 0,
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
