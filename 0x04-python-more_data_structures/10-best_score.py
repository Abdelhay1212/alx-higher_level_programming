#!/usr/bin/python3

def best_score(a_dictionary):
    max_n = 0
    if not a_dictionary:
        return 'None'
    for key in a_dictionary:
        if max_n < a_dictionary[key]:
            max_n = a_dictionary[key]
            max_key = key
    return max_key
