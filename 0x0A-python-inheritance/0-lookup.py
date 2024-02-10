#!/usr/bin/python3
def lookup(obj):
    # Use the dir() function to get a list of attributes and methods
    attributes_and_methods = dir(obj)
    
    # Return the list
    return attributes_and_methods

# Example usage:
my_list = [1, 2, 3]
result = lookup(my_list)
print(result)
