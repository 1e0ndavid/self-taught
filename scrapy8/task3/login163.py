#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:55:57 2019

@author: davidleon
"""

import time
from selenium import webdriver

chrome_driver = '/Applications/Google Chrome.app/Contents/chromedriver'
browser = webdriver.Chrome(executable_path = chrome_driver)

url = 'http://mail.163.com/'
browser.get(url)
time.sleep(3)

login_psw = browser.find_element_by_id('lbNormal')
login_psw.click()

browser.switch_to.frame(0)

email = browser.find_element_by_name('email')
email.send_keys('jianbodai')

password = browser.find_element_by_name('password')
password.send_keys('DAI81991zhen')

login_em = browser.find_element_by_id('dologin')
login_em.click()
time.sleep(10)
