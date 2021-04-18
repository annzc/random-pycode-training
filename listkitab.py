from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json, sys

l = sys.argv[1]
api = 'http://api.carihadis.com/'
raw = urlopen(api)
kutubun = json.loads(bs(raw, 'html.parser').text)['kitab']
for i in range(len(kutubun)):
    print(i+1, '.', kutubun[i])

