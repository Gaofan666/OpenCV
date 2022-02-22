"""
区分实例方法和类方法，实例对象和类对象
因为类方法没有对象地址self,所以不能访问实例成员
类方法用类名调用
"""


class ICBC:
    """
    工商银行
    """
    # 类变量
    total_money = 1000000  # 总行的钱

    @classmethod
    def print_total_money(cls):
        print(cls, ICBC)  # cls和ICBC是一样的
        print(id(cls), id(ICBC))  # 打印地址
        print("总行还剩%d元" % ICBC.total_money)

    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.total_money -= money  # 从总行中扣除当前支行的金额


i01 = ICBC('青岛支行', 100000)
i02 = ICBC('即墨支行', 100000)
print("总行还剩%d元" % ICBC.total_money)
ICBC.print_total_money()
