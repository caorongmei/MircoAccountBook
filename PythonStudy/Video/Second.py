#coding=utf-8
import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

res=requests.get('http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9371003.shtml')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
h1=soup.select('#artibodyTitle')[0].text
timesource=soup.select('.time-source')[0].contents[0].strip()
medianame=soup.select('.time-source span a')[0].text
#print(medianame)

article=[]
for p in soup.select('#artibody p'):
    article.append(p.text.strip().encode("utf-8"))
    print(p.text.strip().encode("utf-8"))

#print('\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]]))
#print('\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]]))

# edit=soup.select('.article-editor')[0].text
# print(edit)
#
# comments=requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyhfnrf9371003&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20')
# jd=json.loads(comments.text.strip('var data='))
# print(jd['result']['count']['total'])

#通过截取字符串
# newurl='http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9371003.shtml'
# print(newurl.split('/'))
# id=newurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
# print(id)

#正则表达式
# m=re.search('doc-i(.*).shtml',newurl)
# print(m.group(1))

#写一个方法，建立评论数抽取函式

commentsUrl='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
def getCommentCount(newsUrl):
    m=re.search('doc-i(.*).shtml',newsUrl)
    newid=m.group(1)
    comments=requests.get(commentsUrl.format(newid))
    jd=json.loads(comments.text.strip(('var data=')))
    print(jd['result']['count']['total'])

news='http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9371003.shtml'
getCommentCount(news)







