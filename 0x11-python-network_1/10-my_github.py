#!/usr/bin/python3i
'''
a script that takes GitHub credentials to display your id
'''
import requests
import sys

url = 'https://api.github.com/user'
r = get(url, auth=(argv[1], argv[2]))
    print(r.json().get('id'))
