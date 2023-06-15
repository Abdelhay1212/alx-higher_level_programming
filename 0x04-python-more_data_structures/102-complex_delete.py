#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = {}
    for key in a_dictionary:
        if a_dictionary[key] != value:
            new_dic[key] = a_dictionary[key]
    a_dictionary.clear()
    a_dictionary.update(new_dic)
    return new_dic
