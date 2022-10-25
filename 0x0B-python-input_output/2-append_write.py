#!/usr/bin/python3
"""Defines a text appending function"""


def append_write(filename="", text=""):
    """Appends a text file
    Args:
        filename (str): name of file
        text (str): string to append to @filename
    Return
        The number of characters added"""
    with open(filename, mode='a') as f:
        return f.write(text)
