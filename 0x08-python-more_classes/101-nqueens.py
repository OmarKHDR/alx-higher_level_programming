#!/usr/bin/python3
import sys
""" the problem of n queens"""


def main():

    n = len(sys.argv)
    if n != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isnumeric():
        print("N must be a number")
        exit(1)
    nQueens = int(sys.argv[1])
    if nQueens < 4:
        print("N must be at least 4")
        exit(1)

    putQueen([], nQueens)


def isInCheck(queens_board, pos):
    for queen in queens_board:
        if pos[0] == queen[0]:
            return True
        if pos[1] == queen[1]:
            return True
        if abs(pos[0] - queen[0]) == abs(pos[1] - queen[1]):
            return True
    return False


def putQueen(queens_board, n):
    row = len(queens_board)
    if row == n:
        print(queens_board)
        return

    for col in range(n):
        pos = [row, col]
        if not isInCheck(queens_board, pos):
            queens_board.append(pos)
            putQueen(queens_board, n)
            queens_board.pop()


if __name__ == "__main__":
    main()
