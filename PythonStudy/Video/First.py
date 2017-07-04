import requests
from bs4 import BeautifulSoup
res=requests.get('http://news.sina.com.cn/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
#print(soup)
for news in soup.select('.list_14'):
    if len(news.select('li'))>0:
        titles=news.select('a')[0].text
        link=news.select('a')[0]['href']
        print(titles+','+link)





