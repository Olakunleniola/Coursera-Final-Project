#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
for img in os.listdir():
    try:
        with open('supplier-data/images/' + img, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
    except:
        pass
