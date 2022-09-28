#!/usr/bin/python3

def roman_to_int(roman_string):
    result, i = 0, 0

    while i < len(roman_string):
        s1 = value_at(roman_string[i])

        if (i + 1) < len(roman_string):
            s2 = value_at(roman_string[i + 1])
            if s1 >= s2:
                result = result + s1
                i = i + 1
            else:
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 1
    return result


def value_at(idx):
    if idx == 'M':
        return 1000
    if idx == 'D':
        return 500
    if idx == 'C':
        return 100
    if idx == 'L':
        return 50
    if idx == 'X':
        return 10
    if idx == 'V':
        return 5
    if idx == 'I':
        return 1
    else:
        return 0
