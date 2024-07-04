#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{0}: {1}".format(i, a_dictionary[i]))
