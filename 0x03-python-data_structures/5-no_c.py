#!/usr/bin/python3

def no_c(my_string):
    for _ in range(my_string.count('c')):
        my_string.remove('c')
    for _ in range(my_string.count('C')):
        my_string.remove('C')
    return my_string
