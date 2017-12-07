import urllib2
from bs4 import BeautifulSoup

url = "https://www.oanda.com/lang/ja/forex-trading/analysis/open-position-ratios"
headers = 'Mozilla/5.0'

req = urllib2.Request(url)
req.add_header("User-agent", headers)

soup = BeautifulSoup(urllib2.urlopen(req))
graph = soup.find("div", id="content").find("ol")

#symbol
symbol = []
spans = graph.find_all("span", class_="position-ratio-label")
for span in spans:
	symbol = symbol + [span.string]
print symbol

#long
b_retio = []
spans = graph.find_all("span", class_="long-position")
for span in spans:
	b_retio.extend(span.stripped_strings)
print b_retio

#long
s_retio = []
spans = graph.find_all("span", class_="short-position")
for span in spans:
	s_retio.extend(span.stripped_strings)
print s_retio