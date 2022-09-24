#!/usr/bin/python3
import calculator_1 as cal
from sys import argv

if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    Quant = len(argv) - 1
    if Quant != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
