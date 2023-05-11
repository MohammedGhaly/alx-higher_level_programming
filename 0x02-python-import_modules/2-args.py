#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print('{} arguments'.format(len(sys.argv) - 1), end='')
    if len(sys.argv) == 1:
        print('.')
    else:
        print(':')
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
