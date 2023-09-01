#!/usr/bin/python3
'''
 script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests as rq
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]

    payload = {'q': q}
    r = rq.post(url, data=payload)
    try:
        res = r.json()
        if res == {}:
            print('No result')
        else:
            print(f'[{res.get("id")}] {res.get("name")}')
    except ValueError:
        print('Not a valid JSON')
