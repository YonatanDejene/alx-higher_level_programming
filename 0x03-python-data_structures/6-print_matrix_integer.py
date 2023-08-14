#!/usr/bin/python3
# Task 6-print_matrix_integer.py
def print_matrix_integer(matrix=[[]]):
    # Prints a matrix
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " 
                  if col != row[-1] else " ")
        print()
