#!/usr/bin/python3

""" Creates an empty class  'Square'
"""


class Square:
    """
    Square class with size private attribute
    """
    def __init__(self, size) -> None:
        """
        Instantiation with size
        Args:
        size: size of the Square
        """
        self.__size = size
