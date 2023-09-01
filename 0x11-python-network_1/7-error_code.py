#!/usr/bin/python3
'''
a script that checks for errors using status code before printing page content
'''
import requests as rq
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = rq.get(url)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
