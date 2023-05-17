#!/usr/bin/python3
def uniq_add(my_list=[]):
    hashset = set(my_list)
    res = 0
    for item in hashset:
        res += item
    return res
