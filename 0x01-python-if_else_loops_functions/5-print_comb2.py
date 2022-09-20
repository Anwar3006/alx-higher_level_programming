#!/usr/bin/python3
"""Prints all numbers from 0 to 99"""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print(f"{number:02}", end=", ")
