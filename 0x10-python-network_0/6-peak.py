def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    for i in range(len(list_of_integers)):
        if i > 0 and i < len(list_of_integers) - 1:
            if list_of_integers[i - 1] < list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        else:
            if i == 0 and list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
            elif list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
    return list_of_integers[0]
