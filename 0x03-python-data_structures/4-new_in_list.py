#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return newlist
    newlist.pop(idx)
    newlist.insert(idx, element)
    return newlist
