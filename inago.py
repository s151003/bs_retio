#!python
#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = "https://inagoflyer.appspot.com/btcmac"

driver = webdriver.PhantomJS()

def main():

	driver.get(url)
	print("Connection successful.")
	
	#fetch and print BuyVol
	for buyvol in driver.find_elements_by_id("buyVolumePerMeasurementTime"):
		print("BuyVolume:"+buyvol.text)
	
	#fetch and print SellVol
	for sellvol in driver.find_elements_by_id("sellVolumePerMeasurementTime"):
		print("SellVolume:"+sellvol.text)
	
	driver.quit()

if __name__ == '__main__':
	main()