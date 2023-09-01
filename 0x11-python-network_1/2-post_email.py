#!/usr/bin/python3
'''
 a Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body.
'''


import urllib.request as uq
import urllib.parse as up
import sys


if __name__ == "__main__":
    url, email = (sys.argv[1], sys.argv[2])
    data = {'email': email}
    data = up.urlencode(data)
    data = data.encode('ascii')

    req = uq.Request(url, data)
    with uq.urlopen(req) as res:
        print(res.read().decode('utf8'))
