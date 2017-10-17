import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getPickupLine():
    siteList = [{'urlPath' : 'http://www.pickuplinegen.com/',
                 'id' : 'content'}]
    siteIndex = 0
    site = siteList[siteIndex]


    pickupPage = urlopen(site['urlPath'])
    soup = BeautifulSoup(pickupPage.read(), 'html.parser')

    pickupLine = soup.find(id=site['id']).text
    return pickupLine
        

