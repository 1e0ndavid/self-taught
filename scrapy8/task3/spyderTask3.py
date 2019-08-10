#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:26:18 2019

@author: davidleon
"""

from selenium import webdriver

chrome_driver = '/Applications/Google Chrome.app/Contents/chromedriver'
browser = webdriver.Chrome(executable_path = chrome_driver)
browser.get('http://www.baidu.com')
