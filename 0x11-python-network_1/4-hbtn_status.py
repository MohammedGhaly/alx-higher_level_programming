#!/usr/bin/python3
'''
a Python script that fetches https://alx-intranet.hbtn.io/status
'''


import requests as rq


r = rq.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print(f'\t- type: {type(r.content.decode("utf8"))}')
print(f'\t- content: {r.content.decode("utf8")}')
