#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square(num):
        return num**2

    new_matrix = []
    for i in matrix:
        i = list(map(square, i))
        new_matrix.append(i)
    return new_matrix
