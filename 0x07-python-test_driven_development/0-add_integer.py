#!/usr/bin/python3
"""

this module contains a function that adds 2 numbers

"""


def add_integer(a, b=98):
    """ Function that adds two numbers (integer or float)

    Args:
        a: 1st number
        b: 2nd number

    Returns:
        The result of adding the two numbers

    Raises:
        TypeError: If a or b aren't of type integer or float

    """
    if not (isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int)) and not (isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
