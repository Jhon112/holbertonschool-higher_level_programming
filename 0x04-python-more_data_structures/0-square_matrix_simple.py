#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for a in matrix:
        new_matrix.append(list(map(lambda x: x*x, a)))
    return (new_matrix)
