#!/usr/bin/python3

def no_c(my_string):
    a = 0
    new = my_string.lower()
    while a != -1:
        a = new.find("c")
        if a != -1:
            my_string = my_string[:a] + my_string[a+1:]
            new = new[:a] + new[a+1:]
        else:
            break
    return my_string
