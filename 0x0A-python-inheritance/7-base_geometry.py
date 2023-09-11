#!/usr/bin/python3
'''Defines base geometry class BaseGeometry.'''


class BaseGeometry:
    '''Reprsents base geometry.'''

    def area(self):
        '''Not yet implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            ValueError: If value is <= 0.
            TypeError: If value is not an integer.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
