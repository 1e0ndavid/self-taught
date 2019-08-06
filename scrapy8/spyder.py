#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 01:30:07 2019

@author: davidleon
"""
 
import requests
import re

def getContent(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.text
    else:
        return None
    
def getLine(url):
    html  = getContent(url)
    pattern = re.compile('<em class="">(.*?)</em>[\s\S]*?<span class="title">(.*?)</span>[\s\S]*?<p class="">[\s\S](.*?)&nbsp[\s\S]*?<br>[\s\S]*?(.*)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp')
    items = re.findall(pattern, html)
    ls=[]
    for item in items:
        dic = {}
        dic['rank'] = item[0].strip()
        dic['name'] = item[1].strip()
        dic['director'] = item[2].strip()
        dic['data'] = item[3].strip()
        dic['country'] = item[4].strip()
        ls.append(dic)
    return ls

def travel(url, filePath):
    file = open(filePath,'w')
    for i in range(0, 250, 25):
        tmp= url+'?start='+str(i)
        for info in getLine(tmp):
            print(info)
            file.write(info['rank']+','+info['name']+','+info['director']+','+info['data']+','+info['country']+'\n')

if __name__ == "__main__":
    url = 'https://movie.douban.com/top250'
    travel(url,'movieInfo.txt')