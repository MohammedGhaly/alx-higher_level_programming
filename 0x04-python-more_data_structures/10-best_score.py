#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    key = ''
    max_score = 0
    for item in a_dictionary:
        if a_dictionary[item] > max_score:
            max_score = a_dictionary[item]
            key = item
    return key
