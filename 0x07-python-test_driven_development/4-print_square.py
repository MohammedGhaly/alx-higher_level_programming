#!/usr/bin/python3
"""

module that includes 'print_square' function

"""


def print_square(size):
    """ Function that prints a square of 'size' length of #
    Args:
        size : integer

    Returns:
        Success

    Raises:
        TypeError:
                size is not integer
        ValueError:
            size < 0
    """
    size_err = 'size must be an integer'
    zero_err = 'size must be >= 0'

    if type(size) is not int:
        raise TypeError(size_err)
    if size < 0:
        raise ValueError(zero_err)

    for i in range(size):
        print('#'*size)
