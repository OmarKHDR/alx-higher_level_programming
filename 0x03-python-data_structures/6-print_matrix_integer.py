#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return None
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" ")
        print("{}".format('\n'), end="")
