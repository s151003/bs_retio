#!/usr/bin/python
# -*- coding: utf-8 -*-
def gaitame():
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from time import sleep

	driver = webdriver.PhantomJS()
	driver.get('http://www.gaitame.com/market/')
	driver.set_page_load_timeout(5)
	driver.find_element_by_class_name('ga06-clone')
	html = driver.page_source

	soup = BeautifulSoup(html,"lxml")
	div = soup.find("div", id="ga06_1")

	#symbol
	symbol = []
	spans = div.find_all('img')
	for span in spans:
		symbol.append(span['alt'])



	#long
	b_retio = []
	spans = div.find_all("span", class_="buyP")
	for span in spans:
		b_retio.extend(span.stripped_strings)

	# short
	s_retio = []
	spans = div.find_all("span", class_="sellP")
	for span in spans:
		s_retio.extend(span.stripped_strings)

	driver.quit()
	return symbol,b_retio,s_retio
