# import the required library
import requests as req
from bs4 import BeautifulSoup as bs
import random

response = req.get(
    url='https://en.wikipedia.org/wiki/Web_scraping'
)
soup = bs(response.content, 'html.parser')

title = soup.find(id='firstHeading')
print(title.string)

# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
    # We are only interested in other wiki articles
    if link['href'].find("/wiki/") == -1: 
        continue

    # Use this link to scrape
    linkToScrape = link
    break

print(linkToScrape)
