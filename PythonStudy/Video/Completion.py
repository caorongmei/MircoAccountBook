#coding=utf-8
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
import re
import pandas

def getCommentCount(newsUrl):
    m=re.search('doc-i(.*).shtml',newsUrl)
    newid=m.group(1)
    commentsUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comments=requests.get(commentsUrl.format(newid))
    jd=json.loads(comments.text.strip(('var data=')))
    return jd
    #print(jd['result']['count']['total'])

def getNewsDetail(newsUrl):
    res=requests.get(newsUrl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'lxml')
    result=[]
    title=soup.select('#artibodyTitle')[0].text
    result.append(title)
    source=soup.select('.time-source span a')[0].text
    result.append(source)
    datetime=soup.select('.time-source')[0].contents[0].strip()
    result.append(datetime)
    editor=soup.select('.article-editor')[0].text
    result.append(editor)
    article='\n'.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result.append(article)
    # result='title:'+title+'\n'+'source:'+source+'\n'+'datetime:'+datetime+'\n'+'editor:'+editor+'\n'+'article:'+article
    return result

# news='http://news.sina.com.cn/c/nd/2017-06-20/doc-ifyhfnrf9371003.shtml'
# print(getNewsDetail(news))

def parseListLinks(url):
    newsdetails=[]
    res=requests.get(url)
    str = res.text.lstrip(' newsloadercallback(').rstrip(');')
    jd = json.loads(str)
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails


url='http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1498031108189'
news_total=[]
for i in range(1,3):
    newsurl=url.format(i)
    newsary=parseListLinks(newsurl)
    news_total.extend(newsary)
    #print(len(news_total))
    df=pandas.DataFrame(news_total)
    df.to_excel('0628.xlsx')
    # print(df)
    df.head()




