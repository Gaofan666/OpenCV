"""
使用property（读取，写入），封装变量
"""

class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # 本质：单下划线+类名+双下划线+变量名  （障眼法）
        # self.__age = age  # 方法一：双下划线隐藏变量，用户无权更改
        # self.set_age(age)
        self.age=age  # 方法三：先定义变量，再拦截变量进行函数运算
        self.set_weight(weight)
        # self.__weight = weight  # 方法二：不直接定义私有变量，而是定义函数进行筛选，从函数中定义

    # 提供公开的读写方法
    def get_age(self):  # 隐藏之后用户如何读取
        return self.__age

    def set_age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("太老了，我不要")
    # 拦截对age变量的读写操作,可以填 None
    age = property(get_age,set_age) # 函数名不能写小括号

    def get_weight(self):  # 隐藏之后用户如何读取
        return self.__weight

    def set_weight(self, value):
        if 45 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("太胖了，我不要")


# w01 = Wife("铁锤公主", 18, 45)
#
# print(w01.name)
# print(w01.__dict__) # python内置变量，存储对象的实例变量
#
# w01._Wife__age = 22  # 识破障眼法，改变私有变量
# print(w01.__dict__)

w01 = Wife("铁扇公主", 22, 50)
print(w01.age, w01.get_weight()) # 使用property可以直接访问age,而不用get_age

