"""
继承--设计
"""


# 违反了开闭原则
# 如果增加火车，需要增加“火车类”，再修改人类中的goto方法

class Vechicle:
    """
    交通工具 抽象
    """

    def transport(self, str_position):
        pass


class Person:
    def __init__(self, name):
        self.name = name

    def goto(self, vehicle, str_position):  # 这里的vehicle是实例对象
        # if type(vehicle) == Car:
        #     vehicle.run(str_position) # 实例对象调用类方法
        # elif type(vehicle) == Airplane:
        #     vehicle.fly(str_position)
        vehicle.transport(str_position)


# 这样写以后增加交通工具，就不违反开闭原则
class Car(Vechicle):
    def transport(self, str_position):
        print("汽车开到", str_position)


class Airplane(Vechicle):
    def transport(self, str_position):
        print("飞机飞到", str_position)


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.goto(a01, "东北")
