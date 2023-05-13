#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for ch in my_string:
        if ch not in 'cC':
            new += ch
    return new
