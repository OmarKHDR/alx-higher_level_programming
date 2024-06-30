#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0,) * (2 - len(tuple_a))
    b = tuple_b + (0,) * (2 - len(tuple_b))
    return tuple([x + y for x, y in zip(a, b)])
