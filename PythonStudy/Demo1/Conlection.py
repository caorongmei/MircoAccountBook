# coding=utf-8

# 列表：python 没有数组概念，但是列表和数组的概念接近

people=["张三","李四","王五"]

names=("张三","李四","王五")

print people[2]

# 集合
xitems=set("10009988776")
xitems.add("s")
xitems.remove("s")
#xitems.discard("0")
print xitems
yitems=set("666555500")

# 交集 &   并集 |  差集 -

print("交集：{0}".format(xitems&yitems))
print("并集：{0}".format(xitems|yitems))
print("差集：{0}".format(xitems-yitems))

# 字典
dic={'a':'1','b':'2',"c":"8"}
print dic['a']









