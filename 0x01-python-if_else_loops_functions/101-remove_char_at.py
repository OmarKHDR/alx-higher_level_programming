#!/usr/bin/python3

def remove_char_at(str, n):
    return str[:(n-1, n)[n >= 0]] + (str[n + 1:], '')[n == -1]
