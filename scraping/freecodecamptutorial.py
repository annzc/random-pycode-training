#!/data/data/com.termux/files/usr/bin/python2

# import required libraries
import urllib2
from bs4 import BeautifulSoup as bs

# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = bs(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

# After we have the tag, we can get the data by getting its text.
name = name_box.text.strip() # strip() is used to remove starting and trailing

print(name) # print out the scraped name of object

# get the price
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text

print(price) # print out the price
