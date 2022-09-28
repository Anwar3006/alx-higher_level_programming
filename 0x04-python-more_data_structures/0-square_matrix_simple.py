#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function computes the square value of all integers of a matrix."""
    squares = []
    if len(matrix) > 0:
        for elements in matrix:
            l = []
            for x in elements:
                l.append(x ** 2)
            squares.append(l)
    return squares
