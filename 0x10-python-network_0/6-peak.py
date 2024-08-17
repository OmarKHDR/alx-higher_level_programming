#!/usr/bin/python3
"""docs is docs"""


arr = {}
def find_peak(list_of_integers):
    """ k is for hello world
    """
    if list_of_integers is None:
        return None
    if list_of_integers in arr.keys():
        return arr[list_of_integers]
    else:
        arr.append(list_of_integers)
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i > peak:
                peak = i
        
        return peak
