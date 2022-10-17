#!/usr/bin/python3
"""Defines a square printing function with #"""


def print_square(size):
    """Prints the square pattern of length (size)
    Args:
        size: integer length of pattern
    Raises:
        TypeError: If size isn't an integer or less than zero
        ValueError: If size is 0
    Return:
        Pattern of square of length size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size == 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
