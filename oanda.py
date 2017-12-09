def oanda(reqSym):
	import urllib2
	from bs4 import BeautifulSoup

	url = "https://www.oanda.com/lang/ja/forex-trading/analysis/open-position-ratios"
	headers = 'Mozilla/5.0'

	req = urllib2.Request(url)
	req.add_header("User-agent", headers)

	soup = BeautifulSoup(urllib2.urlopen(req),"lxml")
	graph = soup.find("div", id="content").find("ol")

	if reqSym == "All":
		found = "All"
	#symbol
	count = 0
	symbol = []
	spans = graph.find_all("span", class_="position-ratio-label")

	for span in spans:
		count = count + 1
		if reqSym == span.string:
			found = count
		symbol = symbol + [span.string]

	#long
	b_retio = []
	spans = graph.find_all("span", class_="long-position")
	for span in spans:
		b_retio.extend(span.stripped_strings)

	#short
	s_retio = []
	spans = graph.find_all("span", class_="short-position")
	for span in spans:
		s_retio.extend(span.stripped_strings)

	return symbol,b_retio,s_retio,found
