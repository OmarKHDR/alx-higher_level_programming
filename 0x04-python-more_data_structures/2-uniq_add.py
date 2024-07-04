#!/usr/bin/python3

def uniq_add(my_list=[]):
    lst = []
    for i in my_list:
        if i not in lst:
            lst.append(i)
