#!/usr/bin/python3
"""

a module that contains a function that divides the elements of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
    matrix: list of lists of int/floats
    div: number that divides the matrix

    Returns:
    A new matrix with the result of the division

    Raises:
    TypeError: If the elements of the matrix not of type list
               If the elemetns of the matrix elements not of type int/float
               If div is not of type int/float
               If the lists of matrix don't have the same length

    ZeroDivisionError: If div is zero
    """

    type_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    size_msg = 'Each row of the matrix must have the same size'
    zero_msg = 'division by zero'
    div_msg = 'div must be a number'

    if type(div) not in [int, float]:
        raise TypeError(div_msg)

    if div == 0:
        raise ZeroDivisionError(zero_msg)

    if matrix is None:
        raise TypeError(type_msg)

    if not isinstance(matrix, list):
        raise TypeError(type_msg)

    if len(matrix) == 0:
        raise TypeError(type_msg)

    if not all(element is not None for element in matrix):
        raise TypeError(type_msg)

    if not all(type(element) == list for element in matrix):
        raise TypeError(type_msg)

    if not all(type(num) in [int, float] for elem in matrix for num in elem):
        raise TypeError(type_msg)

    if not all((len(matrix[0]) == len(element)) for element in matrix):
        raise TypeError(size_msg)

    nu = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return nu
