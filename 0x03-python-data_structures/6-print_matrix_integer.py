#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a = matrix[i][j]
            print("{:d}".format(a), end=("", " ")[j < len(matrix[i])])
        else:
            print()
