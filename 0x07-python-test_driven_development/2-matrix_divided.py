#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if matrix is not type(list(int)) or matrix is not type(list(float)):
        raise TypeError("matrix must be a matrix (list of lists) of\
         integers/floats")
    for row in matrix:
        if len(matrix(row)) != len(matrix(row + 1)):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [list(map(lambda x: round(x / div, 2), row) for row in matrix)]