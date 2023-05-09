#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) in range(97, 123):
            print('{:c}'.format(ord(ch) - 32), end='')
        else:
            print('{:c}'.format(ord(ch)), end='')
    print()
