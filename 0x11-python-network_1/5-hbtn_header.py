#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL"""
import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
