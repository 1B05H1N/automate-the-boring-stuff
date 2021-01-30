import bs4
import requests 

res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup.select('span.a-size-medium:nth-child(2)')
elems[0].text.strip()

