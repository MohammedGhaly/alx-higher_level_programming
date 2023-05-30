#!/usr/bin/python3

"""
Square class with size private attribute
"""


class Square:
    """
    Empty Square class with size private attribute
    """
    def __init__(self, size=0) -> None:
        """
        Instantiation with size
        Args:
            size: size of the Square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
