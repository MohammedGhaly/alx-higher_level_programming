#!/usr/bin/python3
"""
    contains 'add_attribute' function
"""


def add_attribute(obj, name, value):
    """
        adds a new attribute if t is possible.
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
