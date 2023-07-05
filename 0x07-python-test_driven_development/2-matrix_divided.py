#!/usr/bin/python3


def matrix_divided(matrix, div):
    """divide the elements of a matrix by div
    args:
        matrix: the passed matrix
        div: the number to devide by
    """

    length = len(matrix[0])
    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for i in matrix:
            inner_matrix = []
            for j in i:
                if not isinstance(j, int) and not isinstance(j, float):
                    raise TypeError("matrix must be a matrix (list of lists)\
                                    of integers/floats")
                else:
                    inner_matrix.append(round(j / div, 2))
            new_matrix.append(inner_matrix)
        return new_matrix
