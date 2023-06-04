#!/usr/bin/python3
"""

this module include 'say_my_name' function

"""


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"
    Args:
        first_name: first name
        last_name: last name
    Returns:
        No return
    Raises:
        TypeError: If first_name or last_name is not a string
    """
    first_err = 'first_name must be a string'
    last_err = 'last_name must be a string'

    if type(first_name) is not str:
        raise TypeError(first_err)
    if type(last_name) is not str:
        raise TypeError(last_err)

    print('My name is {} {}'.format(first_name, last_name))
