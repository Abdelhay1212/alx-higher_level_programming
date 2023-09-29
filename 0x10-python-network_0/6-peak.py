#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    l, r = 0, len(list_of_integers) - 1
    while l <= r:
        m = (l + r) // 2
        if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
            r = m - 1
        elif m < len(list_of_integers) - 1 and list_of_integers[m] < list_of_integers[m + 1]:
            l = m + 1
        else:
            return list_of_integers[m]
    return None
