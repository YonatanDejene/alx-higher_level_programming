#!/usr/bin/python3
# Task 4-new_in_list.py

def new_in_list(my_list, idx, element):
    # Replace an element in a replica list at a certain index.
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    replica = [x for x in my_list]
    replica[idx] = element
    return (replica)
