#!/usr/bin/python3
"""Function that returns all characters as uppercase."""


def uppercase(str):
    for i in str:
        if  ord(i) >= 97 and ord(i) <= 123:
            i = chr(ord(i) - 32)
        print(f"{i}", end= "")
    print("")
