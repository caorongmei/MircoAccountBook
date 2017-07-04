
# coding=utf-8

# Python 定义常量 相比其他语言比较麻烦，不仅仅是单靠const 就可以完成常量定义的。
# 在Python中定义常量需要用 对象 的方法来创建

# 最好要在 External Libraries下的 Lib下新建 const.py文件，写下一下内容
#
# class _const(object):
#     class ConstError(TypeError):pass
#     def __setattr__(self, name, value):
#         if self.__dict__.has_key(name):
#             raise self.ConstError, "Can't rebind const (%s)" %name
#         self.__dict__[name]=value
#     def __delattr__(self, name):
#         if name in self.__dict__:
#             raise self.ConstError, "Can't unbind const (%s)" %name
#         raise NameError, name
# import sys
# sys.modules[__name__] = _const()


import const

const.value=5
print(const.value)

# const.value=6
# print(const.value)

