#!/usr/bin/python
# -*- coding: utf-8 -*-
def xm(reqSym):
	import urllib2
	from bs4 import BeautifulSoup

	url = "http://www.xmtrading.com/jp/"
	headers = 'Mozilla/5.0'

	req = urllib2.Request(url)
	req.add_header("User-agent", headers)

	soup = BeautifulSoup(urllib2.urlopen(req),"lxml")

	# スラッシュがないので取り除く
	reqSym =  reqSym.replace('/', '')
	if reqSym is "All":
		found = "All"

	# symbol
	count = 0
	symbol = []
	divs = soup.find("div", id="dashboard-wrap").find_all("b")
	for div in divs:
		count = count + 1
		if reqSym == div.string:
			found = count
		symbol = symbol + [div.string]

	# buy
	b_retio = []
	links = soup.find_all("i", class_="green-bar-nbr")
	for i in links:
		b_retio = b_retio + [i.string]

	# sell
	s_retio = []
	links = soup.find_all("i", class_="red-bar-nbr")
	for i in links:
		s_retio = s_retio + [i.string]

	return symbol, b_retio, s_retio,found
