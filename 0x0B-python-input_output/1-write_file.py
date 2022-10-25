#!/usr/bin/python3
"""Defines a text writing function"""


def write_file(filename="", text=""):
    """Reads a text file
    Args:
        filename (str): name of file
        text (str): string to write to @filename
    Return
        The number of characters written"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
