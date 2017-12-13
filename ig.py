from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.PhantomJS()
driver.get('https://www.dailyfx.com/sentiment')
sleep(3)
html = driver.page_source
soup = BeautifulSoup(html,"lxml")

print soup.find("div", class_= "sentiment-panel-container")
driver.quit()