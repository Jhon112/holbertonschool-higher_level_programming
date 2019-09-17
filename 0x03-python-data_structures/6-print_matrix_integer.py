#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for i in l:
            if (l.index(i) == len(l) - 1):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
        print("")
