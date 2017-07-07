#coding=utf-8

class Employee:
    '所有员工的基类'
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployee(self):
        print "name:",self.name,"salary:",self.salary

t=Employee('haha','89')
t.displayCount()
t.displayEmployee()


