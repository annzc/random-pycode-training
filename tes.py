from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json, sys

k = sys.argv[1]
n = sys.argv[2]
url = 'http://carihadis.com/'+k+'/'+n
raw = urlopen(url)
soup = bs(raw, 'html.parser')
nass = soup.find('p', {'class':'MsoBodyText'})
terjemah = soup.find('p',{'class':'MsoNormal','style':'text-align:justify;text-justify:kashida;text-kashida:  0%;text-indent:14.2pt;tab-stops:right 0cm;direction:ltr;unicode-bidi:embed'})
terjemah = terjemah.findAll('span')
print(terjemah)
