#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Function that returns a set of common elements in two sets."""

    for element in set_1 and set_2:
        if element in set_1 and set_2:
            return element
