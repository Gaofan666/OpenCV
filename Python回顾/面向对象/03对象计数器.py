"""
练习：定义对象计数器
定义老婆类，创建三个老婆对象
可以通过类变量记录老婆对象个数
可以通过类方法打印老婆对象个数
"""


class Wife:
    num = 0

    def __init__(self, name):
        self.name = name
        Wife.num += 1

    @classmethod
    def print_wife_num(cls):
        print("老婆有%d个" % Wife.num)


w01 = Wife("露露")
w02 = Wife("哈鲁")
w03 = Wife("tongjin")

Wife.print_wife_num()