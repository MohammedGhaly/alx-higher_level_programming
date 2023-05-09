#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) in range(97, 123):
            upper = ord(ch) - 32
        else:
            upper = ord(ch)
        print('{:c}'.format(upper), end='')
    print()
