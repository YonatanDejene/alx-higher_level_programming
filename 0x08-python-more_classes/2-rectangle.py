#!/usr/bin/python3
'''Defining a Rectangle class.'''


class Rectangle:
    '''Representing a class rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initializing the new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get or set the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get or set the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of the Rectangle.'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns perimeter of the Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))