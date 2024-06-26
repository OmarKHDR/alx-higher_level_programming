#!/usr/bin/python3
def print_last_digit(number):
    out = abs(number) % 10
    print(out, end="")
    return out
