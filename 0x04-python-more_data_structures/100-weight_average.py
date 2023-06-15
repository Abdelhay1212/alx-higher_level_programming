#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    for tup in my_list:
        mul = 1
        for ele in tup:
            mul *= ele
        total += mul
    return (total / sum(item[1] for item in my_list))
