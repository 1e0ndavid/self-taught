#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:08:41 2019

@author: davidleon
"""

import requests

url = 'https://www.baidu.com/'
r = requests.get(url)
print(r.text)
'''

data = {
        "name": "djb",
        "school": "dut"}

r = requests.post("http://www.baidu.com/", data = data)
print(r.text)
'''