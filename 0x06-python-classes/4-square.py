#!/usr/bin/python3
"""Define the class Square."""


class Square:
    """Represent the class Square."""

    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): The new Square size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the class Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return : current area of the square."""
        return (self.__size * self.__size)
