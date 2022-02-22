"""
使用属性property，封装变量
"""


class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age  # 方法四：使用属性@property
        self.set_weight(weight)

    @property  # 创建property对象，只负责拦截读取操作
    def age(self):  # 隐藏之后用户如何读取，注意啊，函数名改为age了
        return self.__age

    @age.setter  # 负责拦截写入操作
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("太老了，我不要")

    def get_weight(self):  # 隐藏之后用户如何读取
        return self.__weight

    def set_weight(self, value):
        if 45 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("太胖了，我不要")


w01 = Wife("铁扇公主", 22, 50)
w01.age = 23
print(w01.age, w01.get_weight())  # 使用property可以直接访问age,而不用get_age
