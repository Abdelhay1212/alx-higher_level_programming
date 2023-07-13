#!/usr/bin/python3
"""function represent pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []
    _list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(_list[i - 1][j - 1] + _list[i - 1][j])
        _list.append(row)
    return _list
