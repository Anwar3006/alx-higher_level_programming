#!/usr/bin/python3
"""Prints  prints all possible different combinations of two digits. 
    01 and 10 are considered the same combination of the two digits 0 and 1
    Print only the smallest combination of two digits"""
for number_i in range(0,10):
    for number_j in range(number_i + 1, 10):
        if number_i == 8 and number_j == 9:
            print("{}{}".format(number_i, number_j))
        else:
            print(f"{number_i}{number_j}", end= ", ")
            