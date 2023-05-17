#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum = 0
    i = 0
    dic = {'X': 10, 'I': 1, 'V': 5, 'C': 100, 'L': 50, 'D': 500, 'M': 1000}
    for i in range(len(roman_string) - 1):
        if roman_string[i] == 'C' and roman_string[i + 1] in 'MD':
            sum -= 100
        elif roman_string[i] == 'X' and roman_string[i + 1] in 'LC':
            sum -= 10
        elif roman_string[i] == 'I' and roman_string[i + 1] in 'VX':
            sum -= 1
        else:
            sum += dic[roman_string[i]]
    sum += dic[roman_string[-1]]
    return sum
