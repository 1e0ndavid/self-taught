#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:50:47 2019

@author: davidleon
"""

import requests

headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

r=requests.post("http://baike.baidu.com/item/哆啦A梦",headers=headers,allow_redirects=False)

r.encoding='UTF-8'
print(r.url)
print(r.headers)
print(r.request.headers)