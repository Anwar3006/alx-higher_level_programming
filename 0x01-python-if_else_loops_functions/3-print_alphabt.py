#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line.
    Print all the letters except q and e"""
for characters in range(97, 123):
    if chr(characters) == 'e' or chr(characters) == 'q':
        continue
    else:
        print("{:c}".format(characters), end="")
