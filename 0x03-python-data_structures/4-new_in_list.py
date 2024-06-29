#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = [i for i in my_list]
    if idx > len(my_list) or idx < 0:
        return newlist
    newlist.insert(idx, element)
    return newlist
