import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import json
import codecs

def getJoke():
	siteList = [{'urlPath' : 'https://crackmeup-api.herokuapp.com/',
		'categories' : ['random', 'blond', 'dark', 'dirty', 'gender', 'gross','walks-into-a-bar'],
		'key' : 'joke'
	}]
	siteIndex = 0
	site = siteList[siteIndex]

	randomCategory = random.randint(0, len(site['categories']) - 1)
	urlPath = site['urlPath'] + site['categories'][randomCategory]
	jokeSite = urlopen(urlPath)
	joke = jokeSite.read()
	reader = codecs.getreader("utf-8")
	jsonLoader = json.loads(reader(joke))
	jokeSite.close()
	return jsonLoader[site['key']]

                                    

