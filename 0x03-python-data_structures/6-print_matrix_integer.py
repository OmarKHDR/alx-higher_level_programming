#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{}".format(matrix[i][j]), end= (" " if j < len(matrix[i]) else ""))
        else:
            print()