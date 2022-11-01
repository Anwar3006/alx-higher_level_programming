#!/usr/bin/python3
"""Defines a Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for private instance attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for private instance attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if a is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

    def __str__(self):
        """Return string representation"""

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)
