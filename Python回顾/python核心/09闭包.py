"""
1.	三要素：
-- 必须有一个内嵌函数。
-- 内嵌函数必须引用外部函数中变量。
-- 外部函数返回值必须是内嵌函数。
2.	语法
-- 定义：
def 外部函数名(参数):
		外部变量
		def 内部函数名(参数):
			使用外部变量
		return 内部函数名
-- 调用：
	   变量 = 外部函数名(参数)
	   变量(参数)
3.	定义：在一个函数内部的函数,同时内部函数又引用了外部函数的变量。
4.	本质：闭包是将内部函数和外部函数的执行环境绑定在一起的对象。
5.	优点：内部函数可以使用外部变量。
6.	缺点：外部变量一直存在于内存中，不会在调用结束后释放，占用内存。
7.	作用：实现python装饰器。

"""


def fun01():
    a = 1

    def fun02():
        print(a)

    return fun02


# 调用外部函数，返回内嵌函数
re = fun01()
# 调用内嵌函数
re()

# 面向函数式编程，没有类和封装这个概念
def give_gife_money(money):
    print("得到了%d压岁钱" % money)

    def child_buy(target, price):
        """
        孩子购买商品
        :param target:需要购买的商品
        :param price:商品单价
        :return:
        """
        # 内层函数改变外层函数变量用nonlocal，
        # nonlocal不能定义新的外层函数变量，只能改变已有的外层函数变量
        nonlocal money
        if money > price:
            money -= price
            print("孩子花了%.1f元，购买了%s" % (price, target))
        else:
            print("余额不足")

    return child_buy


# 下列代码是一个连续的逻辑，实际就是这个用途
action = give_gife_money(10000)
action("棒棒糖", 2.5)
action("小汽车", 500)
action("手机", 12000)
