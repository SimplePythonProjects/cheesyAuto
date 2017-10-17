import os
import urllib
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def getComic():
    siteList = [{'urlPath': 'http://explosm.net/comics/random',
                  'id': 'main-comic',
                  'srcAppendPath': 'http:'}]
    siteIndex = 0
    site = siteList[siteIndex]


    randomComicPage = urlopen(site['urlPath'])
    soup = BeautifulSoup(randomComicPage.read(),'html.parser')

    mainComic = soup.find(id=site['id'])
    print(mainComic.get('src'))
    urlretrieve(site['srcAppendPath'] + mainComic.get('src'), 'img.png')

