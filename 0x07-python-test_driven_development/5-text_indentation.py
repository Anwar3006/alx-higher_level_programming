#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """Prints a text with indentations
    Args:
        text: A string to indent
    Raises:
        TypeError: If text isn't a string
    Return:
        Indented text at ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
