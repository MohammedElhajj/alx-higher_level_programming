#!/usr/bin/python3
# A function computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
    # Return a new matrix with the same size and squared values
    new_matrix = matrix.copy()

    for idx in range(len(new_matrix)):
        new_matrix[idx] = list(map((lambda x: x ** 2), matrix[idx]))
    return (new_matrix)
