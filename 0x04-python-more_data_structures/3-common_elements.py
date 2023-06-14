#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = (set_1 & set_2)
    new_list = []
    for ele in new_set:
        new_list.append(ele)
    return (new_list)
