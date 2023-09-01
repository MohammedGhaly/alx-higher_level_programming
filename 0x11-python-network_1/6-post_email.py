#!/usr/bin/python3
"""script that posts an email in an http request"""
import requests as rq
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    headers = {'email', sys.argv[2]}
    r = rq.post(url, headers)
    print(r.text)
