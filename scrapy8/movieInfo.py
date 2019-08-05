#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:52:33 2019

@author: leondavid
"""

import requests
import re
import csv

def movie_info(url):
    headers = {
            'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
    res = requests.get(url, headers = headers)
    ranks = re.findall('<em class="">(.*?)</em>', res.text, re.S)
    names = re.findall('<span class="title">([\u4e00-\u9fa5]+)</span>', res.text, re.S)
    countries = re.findall('&nbsp;/&nbsp;([\u4e00-\u9fa5]+)&nbsp;/&nbsp;', res.text, re.S)
    text = re.sub('导演: ',"",res.text)
    directors = re.findall('<p class="">(.*?)&nbsp;&nbsp;', text, re.S)
    scores = re.findall('<span class="rating_num" property="v:average">(.*?)</span>', res.text, re.S)
    for rank, name, country, director, score in zip(ranks, names, countries, directors, scores):
        writer.writerow([rank, name, country, director, score])

if __name__ == '__main__':
    
    file = open('/Users/davidleon/Desktop/movie1.csv','w+',encoding='utf-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['rank', 'name', 'country', 'director', 'score'])
    
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        movie_info(url)