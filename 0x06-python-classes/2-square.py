#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Represent the class Square"""

    def __init__(self, size=0):
        """Initialize new Square.

        Args:
            size (int): The new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
