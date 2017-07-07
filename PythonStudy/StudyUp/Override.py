#coding=utf-8

class Parent:
    def myMethod(self):
        print '父类-调用'

    def showTime():
        print 'show time'

class Child(Parent):
    def myMethod(self):
        print '子类--调用'
    def showTime(self):
        print 'kk'


c=Child()
c.myMethod()