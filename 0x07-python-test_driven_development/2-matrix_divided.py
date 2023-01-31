#!/usr/bin/python3
"""This module defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """A function to divide all elements of a matrix

    Args:
        matrix(list): the list of lists of int or floats to be divided
        div(int, float): the divisor number

    Returns:
        A new matrix of the division result
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(i, int) or isinstance(i, float))
                for i in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda i: round(i / div, 2), row)) for row in matrix])

