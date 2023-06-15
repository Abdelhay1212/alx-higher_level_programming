#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0
    else:
        roman_int = 0
        for i in range(0, len(roman_string) - 1):
            if roman_num[roman_string[i]] < roman_num[roman_string[i + 1]]:
                roman_int -= roman_num[roman_string[i]]
            else:
                roman_int += roman_num[roman_string[i]]
        roman_int += roman_num[roman_string[-1]]
        return roman_int
