import urllib2
from bs4 import BeautifulSoup

url = "http://www.xmtrading.com/jp/"
headers = 'Mozilla/5.0'

req = urllib2.Request(url)
req.add_header("User-agent", headers)

soup = BeautifulSoup(urllib2.urlopen(req))

# buy
links = soup.find_all("i", class_="green-bar-nbr")
for i in links:
	b_resio = i.string
	print b_resio

# sell	
links = soup.find_all("i", class_="red-bar-nbr")
for i in links:
	s_resio = i.string
	print s_resio
