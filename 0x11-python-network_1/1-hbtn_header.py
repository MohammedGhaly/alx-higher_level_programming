#!/usr/bin/python3
'''
a Python script that takes in a URL, sends a request
displays the value of the X-Request-Id variable.
'''


import sys
import urllib.request as uq


if __name__ == '__main__':
    url = sys.argv[1]
    req = uq.Request(url)
    with uq.urlopen(req) as res:
        print(res.info().get('X-Request-Id'))
