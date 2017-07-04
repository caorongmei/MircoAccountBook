# #coding=utf-8
#
#
# # ord(): 获取字符的整数表示
# # chr(): 把编码转换成对应的字符
#
# print ord('A')
#
# print chr(25)
#
# classmates=['aa','bb','cc']
# print classmates
#
# print len(classmates)
#
# print max(1,2,3,7,9,10)

# 函数

# def myABC(x):
#     if x>=0:
#         return 10
#     else:
#         return  8
#
# print myABC(9)
#
# # 空函数,函数里面什么都不做，可用关键字 pass
# def nop():
#     pass
#
# print 6)


#递归函数

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print fact(4)

# 使用递归函数的优点是裸机简单清晰，缺点是过深的调用会导致栈溢出
#  针对尾递归优化的语言可以通过尾递归防止栈溢出

# 高级特性
# 比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：

L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2

print L




















