from requests import get
from bs4 import BeautifulSoup as bs
import json
import random

ua = [
    'Mozilla/5.0 (X11; CrOS x86_64 13310.76.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.108 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 11895.118.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.159 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12239.92.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.136 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 13099.110.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.136 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 13099.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.127 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 13020.87.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12499.66.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.106 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 13310.59.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.84 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12739.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12607.82.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 13099.85.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.110 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS x86_64 12607.58.0) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/79.0.3945.86 Safari/537.36'
    ]

usr_agent = {
    'User-Agent': random.choice(ua)
    }

usr_query = input('Nama anime : ')

def search_otakudesu(query):
    url = otakudesu = bs(get('https://otakudesu.tv/?s=%s&post_type=anime' % query, headers=usr_agent).text, 'html.parser').find('ul', class_='chivsrc').a['href']
    return url

def scrap_otakudesu(url):
    try:
        otakudesu = bs(get(url).text, 'html.parser')
        title = otakudesu.find('div', class_='jdlrx').text.split('Subtitle')[0]
        sinopsis = otakudesu.find('div', class_='sinopc').text
        info = '\n'.join(str(o.text) for o in otakudesu.find('div', class_='infozingle').findAll('p'))
        thumb = otakudesu.find('img', class_='attachment-post-thumbnail size-post-thumbnail wp-post-image')['src']
        return {
            'thumb': thumb,
            'info': info,
            'sinopsis': sinopsis,
            'title': title
        }
    except Exception as e: return {
        'error': e,
        'msg': 'Failed get metadata'
    }

url = search_otakudesu(usr_query)
scrap_otakudesu(url)
