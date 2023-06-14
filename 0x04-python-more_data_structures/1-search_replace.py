#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def check_ele(num):
        if num == search:
            return replace
        return num

    return list(map(check_ele, my_list))
