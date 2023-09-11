#!/usr/bin/python3
'''Defines function that adds attributes to objects.'''


def add_attribute(obj, att, value):
    '''Adds new attribute to an object if possible.

    Args:
        value (any): The value of att.
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)