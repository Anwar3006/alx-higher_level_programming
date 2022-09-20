#!/usr/bin/python3
"""Function that returns the last digit of an input."""


def print_last_digit(number):
    last_digit = abs(number) % 10
    print(f"{last_digit}", end="")
    return last_digit
