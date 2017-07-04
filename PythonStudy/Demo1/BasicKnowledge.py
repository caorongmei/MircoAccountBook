
# coding=utf-8


def Haha():
    print("haha!!")
print("就这么来")
Haha()

# for循环
# for循环执行代码结束的标志性就是没有缩进
# print 支持拼接需要用.format
# range 表示范围 0<=i<3

for i in range(0, 3):
    print(i)
    print("Index:{0}--{1}".format(i, "haha"))
print("end")


# 定义函数def
# 无论是函数、判断、还是循环 都是以没有缩进表示结束的
def HelloWorld():
    print("hello world!--haha")


def GetMax(x, y):
    if x > y:
        return x
    else:
        return y


HelloWorld()
print (GetMax(9, 3))


# 面向对象
# __init__ 构造函数是有一共4个_
class FirstTest:
    def __init__(self, name):
        self._name = name
        print("hello python! {0} coming!".format(name))

    def SayHi(self):
        print("hello python! {0} coming!".format(self._name))


F = FirstTest("xiaoming")
F.SayHi()


class FirstTest1:
    def __init__(self, name):
        self._name = name

    def SayFirst(self):
        print("Hello {0}".format(self._name))


F = FirstTest1("CNBlogs")
F.SayFirst()


# 继承
class FirstObj:
    def __init__(self, name):
        self._name = name

    def SayHi(self):
        print("sayhi to {0}".format(self._name))


class SecondObj(FirstObj):
    def __init__(self, name):
        FirstObj.__init__(self, name)

    def SayHello(self):
        print("syhello to {0}".format(self._name))


S = SecondObj("xiaomei")
S.SayHi()
S.SayHello()
