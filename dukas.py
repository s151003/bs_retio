#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
# driverの指定
driver = webdriver.PhantomJS()

driver.get('https://www.dukascopy.jp/marketwatch/sentiment/')
