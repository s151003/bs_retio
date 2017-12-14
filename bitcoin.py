from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
driver = webdriver.PhantomJS()
driver.get('https://inagoflyer.appspot.com/btcmac')
html = driver.page_source
soup = BeautifulSoup(html,"lxml")

html = driver.page_source
soup = BeautifulSoup(html,"lxml")
buy = soup.find('span',id="buyVolumePerMeasurementTime")
sell = soup.find('span',id="sellVolumePerMeasurementTime")
if sell.string > buy.string:
	print "----- SELL -----"
else:
	print "----- BUY -----"
print "S",sell.string
print "B",buy.string
sleep(1)
driver.quit()
