#!/usr/bin/python3

"""module that contains 'Square' class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that represents a square shape"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.validate_integer("width", value, False)
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def __update(self, id=None, size=None, x=None, y=None):
        """internal method to update swuare attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """public method to update squre attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {'x': self.x, 'y': self.y, 'size': self.width, 'id': self.id}
        return dic
