#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new = my_list[:idx]
    new += my_list[(idx + 1):]
    return new
