#!/usr/bin/python3
"""Defines an integer/float addition function."""


def add_integer(a, b=98):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return (a + b)
