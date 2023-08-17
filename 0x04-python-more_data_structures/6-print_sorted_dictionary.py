#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orderList = list(a_dictionary.keys())
    orderList.sort()
    for j in list_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
