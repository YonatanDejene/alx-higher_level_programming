#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for j in range(4, 6):
            d = add(c, j)
        return d
    else:
        return sub(a, b)
