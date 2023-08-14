#!/usr/bin/python3
# Task 7-add_tuple.py


def add_tuple(tuple_a=(), tuple_b=()):
    # Add a couple of tuples.
    if len(tuple1) < 2:
        if len(tuple1) == 0:
            tuple_1 = 0, 0
        else:
            tuple1 = tuple1[0], 0
    if len(tuple2) < 2:
        if len(tuple2) == 0:
            tuple2 = 0, 0
        else:
            tuple2 = tuple2[0], 0
		all_tuple = tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]
    return (all_tuple)
