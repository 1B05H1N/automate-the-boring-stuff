import bs4, requests

def getAmazonPrice(productUrl):
	headers = {
	    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
	}

	res = requests.get(productUrl, headers=headers)
	res.raise_for_status()


	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems = soup.select('#newOfferAccordionRow .header-price')
	return elems[0].text.strip()


price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=tmm_pap_swatch_0?_encoding=UTF8&amp;qid=&amp;sr=')

print('The price is ' + price)