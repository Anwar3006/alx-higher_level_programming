#!/usr/bin/python3
"""Module defines a function to print full name"""


def say_my_name(first_name, last_name=""):
    """Print full name passed as arguments to function.
    Args:
        first_name: any string
        last_name: any string
    Raises:
        TypeError: If first or last name is not a string
    Return:
        First and Last name passed as arguments to function
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
