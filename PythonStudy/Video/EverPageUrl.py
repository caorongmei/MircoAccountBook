import  requests
import json

res=requests.get('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=1&callback=newsloadercallback&_=1498031108189')
#print(res.text)
str=res.text.lstrip(' newsloadercallback(').rstrip(');')
jd=json.loads(str)
for ent in jd['result']['data']:
    print(ent['url'])

