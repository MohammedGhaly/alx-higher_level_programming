#!/usr/bin/python3
"""script that posts an email in an http request"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    headers = {'email', sys.argv[2]}
    r = requests.post(url, data=headers)
    print(r.text)
