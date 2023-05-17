#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _sorted = sorted(a_dictionary)
    for item in _sorted:
        print("{}: {}".format(item, a_dictionary[item]))
