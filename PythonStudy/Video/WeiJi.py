# -*- coding: utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests

# 用requests 方法
html=requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
html.encoding='utf-8'
bsObj= BeautifulSoup(html.text, "html.parser")

#用 urlopen 方法
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bsObj2= BeautifulSoup(html, "html.parser")
# print(bsObj2)

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print link.attrs['href']

