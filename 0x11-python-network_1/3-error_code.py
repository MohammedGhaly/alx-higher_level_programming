#!/usr/bin/python3
'''
 a Python script that takes in a URL,
 sends a request to the URL and displays the body of the response
'''


import urllib.request as uq
import urllib.parse as up
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = uq.Request(url)
    try:
        with uq.urlopen(req) as res:
            print(res.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
