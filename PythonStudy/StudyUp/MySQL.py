#coding=utf-8
import mysqldbhelper


#ToDo 学习连接数据库
def TestDB():
    db=mysqldbhelper.DatabaseConnection("localhost","root","123456","test")
    print db.get_one("select * from name ", "")




