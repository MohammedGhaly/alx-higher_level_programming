#!/usr/bin/python3
""" Creates a class called Square
"""


class Square:
    """
    Square class with size private attribute
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

    @property
    def size(self):
        """
        size getter. returns the value of size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter. Set the size square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size**2

    def my_print(self):
        """
        Prints a square with the character # at position given
        """
        for i in range(self.__size):
            print('#'*self.__size)
        if self.__size == 0:
            print()
