#!/usr/bin/python3
"""A function that finds the peak of unordered list"""


def find_peak(list_of_integers):
    """finds the peak of list_of_integers"""

    left, right = 0, len(list_of_integers) - 1
    while left <= right:
        m = (left + right) // 2
        if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            right = m - 1
        elif m < len(list_of_integers) - 1 and\
                list_of_integers[m] < list_of_integers[m + 1]:
            left = m + 1
        else:
            return list_of_integers[m]
    return None
