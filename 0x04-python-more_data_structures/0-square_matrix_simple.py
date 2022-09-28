#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function computes the square value of all matrix elements."""

    squares = []
    if len(matrix) > 0:
        for elements in matrix:
            squares.append(list(map(lambda x: x ** 2, elements)))
    return squares
