from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://pythonscraping.com/pages/page1.html')
beast = bs(html.read(), 'html.parser')
nameList = beast.findAll('div')
for name in nameList:
    print(name.text)
