#!/usr/bin/python3
'''
script that takes in a URL and an email address, sends a POST request
with the email as a parameter, and finally displays the body of the response.
'''
import requests as rq
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    headers = {'email', sys.argv[2]}
    r = rq.post(url, headers)
    print(r.text)
