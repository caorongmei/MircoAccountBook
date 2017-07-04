#coding=utf-8
from bs4 import BeautifulSoup
html_sample='\
<html>\
<body>\
<h1 id="title">Hello World</h1>\
<a href="#" class="link">This is link1</a>\
<a href="#" class="link">This is link2</a>\
</body>\
</html>'
soup=BeautifulSoup(html_sample,'html.parser')
#print(type(soup))
#print(soup.text)

#找出含有 h1标签的元素 ，使用select
header=soup.select('h1')
print(header)
print(header[0])
print(header[0].text)

#找出含有 a标签的元素
alink=soup.select('a')
print(alink)
for link in alink:
    #print(link)
    print(link.text)

#使用select找出所有Id为title的元素 （id前面需加 #）
soup2=BeautifulSoup(html_sample,'html.parser')
alink2=soup2.select('#title')
print(alink2)
for link in soup2.select('.link'):
    print(link)

#使用select 找出所有 a 标签的href链接
alink3=soup2.select('a')
for link in alink3:
    print(link['href'])

#举出一个小例子，关于如何标签属性值
a='<a href="#" qoo=123 abc=567>i am a link</a>'
soup4=BeautifulSoup(a,'html.parser')
print(soup4.select('a')[0]['qoo'])
print(soup4.select('a')[0]['abc'])
print(soup4.select('a')[0]['href'])



















