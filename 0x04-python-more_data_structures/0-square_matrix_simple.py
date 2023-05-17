#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[num**2 for num in item] for item in matrix]
    return new
