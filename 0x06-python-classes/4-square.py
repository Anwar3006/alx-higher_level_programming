#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Function to be used for getting/retrieving
        the private instance attribute(size) value"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        """Function to be used for setting 
        the private instance attribute value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)