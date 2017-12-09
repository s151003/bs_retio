#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver

# driverの指定
driver = webdriver.PhantomJS()
driver.get('http://yahoo.co.jp')

# キャプチャ
driver.save_screenshot('yahoo.png')

driver.quit()