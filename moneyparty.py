#!/usr/bin/python
# -*- coding: utf-8 -*-
def moneyparty(reqSym):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from time import sleep
    driver = webdriver.PhantomJS()
    driver.get('https://www.moneypartners.co.jp/market/ratio/')
    html = driver.page_source

    soup = BeautifulSoup(html,"lxml")

    if reqSym == "All":
    	found = "All"
		
    # long short
    spans = soup.find_all("tspan")
    count = 0
    b_retio = []
    s_retio = []
    for span in spans:
        count += 1
        if len(spans)/2 < count:
            b_retio.extend(span.stripped_strings)
        else:
            s_retio.extend(span.stripped_strings)
    driver.quit()
	
	
    # symbol
    # 手打ちしてやった・・・
    symbols = ["USD/JPY","EUR/JPY","AUD/JPY","NZD/JPY","TRY/JPY","MXN/JPY","GBP/JPY","CHF/JPY","CAD/JPY","EUR/USD","GBP/USD","ZAR/JPY","HKD/JPY","SGD/JPY","AUD/USD","EUR/AUD","EUR/GBP","AUD/NZD","GBP/AUD","NZD/USD"]
    count = 0
    for i in symbols:
        if reqSym == symbols[count]:
    		found = count
        count =+ 1
    print found
    return symbols,b_retio,s_retio,found
