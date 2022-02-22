"""
继承
多个子类在概念上是一致的，可以抽象为父类，项目中一般那都是先有子类后有父类
"""


class Person:
    def say(self):
        print("说话")



class Student(Person):
    def study(self):
        print("学习")


class Teacher(Person):
    def teach(self):
        print("讲课")


t01 = Teacher()
print(isinstance(t01, Teacher)) # 判断t01是不是老师类

print(issubclass(Teacher,Person)) # 判断一个类型是否属于另一个类型
