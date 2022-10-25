#!/usr/bin/python3
"""Defines a text reading function"""


def read_file(filename=""):
    """Reads a text file
    Args:
        filename (str): name of file
    
    Return
        Content of @filename"""
    with open(filename, encoding="utf-8") as f:
        for lines in f:
            print(lines, end='')
