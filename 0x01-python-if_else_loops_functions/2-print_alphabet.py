#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""
for characters in range(97, 123):
    print(f"{chr(characters)}", end="")
