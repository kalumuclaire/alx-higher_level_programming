#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in matrix:
        for a in c:
            print("{:d}".format(a), end=" " if j != c[-1] else "")
        print()
