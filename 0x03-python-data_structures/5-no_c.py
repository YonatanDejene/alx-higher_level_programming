#!/usr/bin/python3
# Task 5-no_c.py

def no_c(my_string):
    # Remove C and c from the list
    replica = [x for x in my_string 
									if x != 'c' and x != 'C']
    return ("".join(replica))
