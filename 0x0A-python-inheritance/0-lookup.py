#!/usr/bin/python3

""" this is a comment for this file """


def lookup(obj):
    """ return dict
        args:
            obj
    """
    return list(type(obj).__dict__)

"""
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))"""