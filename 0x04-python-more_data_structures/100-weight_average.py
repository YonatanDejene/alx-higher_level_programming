#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    no = 0
    x = 0

    for y in my_list:
        no += y[0] * y[1]
        x += y[1]

    return (no / x)
