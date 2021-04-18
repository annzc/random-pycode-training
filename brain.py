from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import sys

query = '+'.join(sys.argv[1:])
url = 'https://brainly.co.id/app/ask?entry=hero&q='+query
raw = urlopen(url)
brainly = bs(raw, 'html.parser').text
print(brainly)
