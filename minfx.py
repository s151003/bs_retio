#!/usr/bin/python
# -*- coding: utf-8 -*-
def minfx(reqSym):
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from time import sleep
	driver = webdriver.PhantomJS()
	driver.get('https://min-fx.jp/market/buysell-ratio/')
	html = driver.page_source

	soup = BeautifulSoup(html,"lxml")

	# スラッシュがないので取り除く
	reqSym =  reqSym.replace('/', '')
	if reqSym is "All":
		found = "All"

	# symbol
	symbol = []
	count = 0
	imgs = soup.find_all("img",height="25")
	for img in imgs:
		count = count + 1
		if reqSym == img['alt']:
			found = count
		symbol.append(img['alt'])

	# people はポジションの人数比率
	# レシオはポジション数量比率
	
	div = soup.find("div", id="ratiodatawrapper")
	# buy
	b_retio = []
	peopleB_retio = []
	count = 1
	spans = div.find_all("div", class_="ratio-counter buy")
	for span in spans:
		if count % 2 == 0:
			peopleB_retio.extend(span.stripped_strings)
		else:
			b_retio.extend(span.stripped_strings)
		count += 1

	# sell
	s_retio = []
	peopleS_retio = []
	count = 1
	spans = div.find_all("div", class_="ratio-counter sell")
	for span in spans:
		if count % 2 == 0:
			peopleS_retio.extend(span.stripped_strings)
		else:
			s_retio.extend(span.stripped_strings)
		count += 1
	driver.quit()

	return symbol,b_retio,s_retio,found

