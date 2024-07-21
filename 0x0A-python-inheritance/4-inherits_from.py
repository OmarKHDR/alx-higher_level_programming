#!/usr/bin/python3

"""is instances???????"""


def is_kind_of_class(obj, a_class):
    """ s*h*itty func
        args: yes it is
    """
    return (isinstance(obj, a_class) and not (type(obj) is a_class))
