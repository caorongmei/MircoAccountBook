from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


pages = set()
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    #return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
print(links)
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     if newArticle not in pages:
#         print(newArticle)
#         pages.add(newArticle)
#         links = getLinks(newArticle)
# print(pages)