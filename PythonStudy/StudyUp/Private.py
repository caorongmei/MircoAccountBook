#coding utf-8

class JustCount:
    __secretcount=0
    publiccount=2

    def count(self):
        self.__secretcount+=1
        self.publiccount+=1
        print self.__secretcount

counter=JustCount()
counter.count()
counter.count()
print counter.publiccount

#以下这句代码会报错，因为不能用实例访问私有变量
#print counter.__secretcount


