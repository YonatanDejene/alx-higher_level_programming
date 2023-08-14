#!/usr/bin/python3
# Task 1. Secure access to an element in a list

def element_at(my_list, idx):
	# Get an element form a specific index
	if idx < 0 or idx > (len(my_list) - 1):
        	return None
    	return (my_list[idx])
