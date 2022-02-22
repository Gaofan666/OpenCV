list01 = [43, 4, 5, 5, 6, 7, 87]


# 继承
def find(func_condition):
    for item in list01:
        # 调用：具体条件的抽象，  执行：具体函数
        if func_condition(item):
            yield item

# lambda匿名函数，item：条件
re = find(lambda item: item > 10)
for i in re:
    print(i)

# 更多用法自己百度