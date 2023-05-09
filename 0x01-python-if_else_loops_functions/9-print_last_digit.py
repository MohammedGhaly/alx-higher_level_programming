#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        res = (-1 * number) % 10
    else:
        res = number % 10
    print('{:d}'.format(res), end='')
    return res
