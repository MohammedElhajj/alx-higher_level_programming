#!/usr/bin/python3
# A function to print a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if (col != row[-1]):
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col), end="")
        print()
