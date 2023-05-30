#!/usr/bin/python3
""" Creates a class called Square
"""


class Square:
    """
    Square class with size private attribute
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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
        Print a square with the character # at position given
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" "*self.__position[0], end='')
            print('#'*self.__size)

    @property
    def position(self):
        """
        position setter. Set the position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Handle position setting with errors
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
