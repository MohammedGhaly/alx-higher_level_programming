#!/usr/bin/python3
class Square:
    """
    square class
    """
    def __init__(self, size=0) -> None:
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size**2

    def my_print(self):
        for i in range(self.__size):
            print('#'*self.__size)
        if self.__size == 0:
            print()
