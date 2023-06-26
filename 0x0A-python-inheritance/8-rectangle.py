#!/usr/bin/python3
"""
contains 'Rectangle' class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class that represents a Rectangle
    inherits from 'BaseGeometry' class
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self._width = width
        self._height = height
