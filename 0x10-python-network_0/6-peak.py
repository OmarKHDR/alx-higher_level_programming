#!/usr/bin/pytohn3
"""docs is docs"""


def find_peak(list_of_integers):
    """ k is for hello world
    """
    if list_of_integers is None:
        return None
    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i
    
    return peak
