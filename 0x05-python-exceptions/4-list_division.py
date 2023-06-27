#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError):
            i += 1
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            i += 1
            new_list.append(0)
            print("division by 0")
        except IndexError:
            i += 1
            new_list.append(0)
            print("out of range")
    return (new_list)
