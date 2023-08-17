#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    uniqList = set(my_list)

    for i in uniqList:
        n += i

    return (n)
