#!/usr/bin/python
# -*- coding: utf-8 -*-
def scrapBfx():
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from time import sleep
	
	print "BFXスクレイピング開始"
	driver = webdriver.PhantomJS()
	driver.get('https://bfxdata.com/orderbooks/btcusd')
	html = driver.page_source
	sleep(3)
	soup = BeautifulSoup(html,"lxml")

	tbody =soup.find("tbody", id= "volume1hTableBody")
	vols = tbody.find_all("td", class_="volumTableValue")

	sellVol = vols[0].text
	buyVol = vols[1].text
	totalVol = vols[2].text
	driver.save_screenshot('bfx.png')
	driver.quit()
	print "DELETE comma"
	sell = sellVol.replace(',', '')
	buy = buyVol.replace(',', '')
	total = totalVol.replace(',', '')

	sell = float(sell)
	buy = float(buy)
	total = float(total)
	
	return sell,buy,total

def genTweet():
	sell,buy,total = scrapBfx()
	if sell == 0.0:
		sell,buy,total = scrapBfx()
		
		
	print "FLOAT変換後↓"
	print sell,buy,total
	print "-----------"
	if sell > buy:
		if sell < 80:
			strong = "かなり売"
		else:
			strong = "売"
	else:
		if buy < 80:
			strong = "かなり買"
		else:
			strong = "買"
	sellretio = round((sell / total), 2) * 100
	buyretio = round((buy / total), 2) * 100

	sell = str(sell)
	buy = str(buy)
	total = str(total)

	sellretio = str(sellretio)
	buyretio = str(buyretio)
	tweet = ""+strong+"優勢) SELLVOL "+sell+" ("+sellretio+"%) BUYVOL "+buy+" ("+buyretio+"%)"
	
	return tweet
	
