"""
继承——变量
"""


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    # 子类若没有构造函数，使用父类的
    def __init__(self, name, score):
        # 子类若具有构造函数，必须先效用父类构造函数
        super().__init__(name) # 不要写self.name=name，没有这么干的
        self.score = score


s01 = Student("森林", 10)
print(s01.name, s01.score)
