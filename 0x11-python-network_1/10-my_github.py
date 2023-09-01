#!/usr/bin/python3
'''
a script that takes GitHub credentials to display your id
'''
import requests
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    r = get(url, auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
