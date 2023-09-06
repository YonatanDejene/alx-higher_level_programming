#!/usr/bin/python3
'''Defines class Rectangle.'''


class Rectangle:
    '''Represents rectangle.

    Attributes:
        number_of_instances (int): Number of Rectangle instances.
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initializing new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        '''
        type(self).number_of_instances += 1
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

    def __str__(self):
        '''Returns printable representation of the Rectangle.

        Represents rectangle with the # character.
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        '''Returns string representation of the Rectangle.'''
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        '''Prints message for every deletion of a Rectangle.'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")