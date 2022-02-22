list01 = [1, 2, "定金", True, 34, False, "lala"]


def find01():
    for item in list01:
        if type(item) == int:
            yield item + 1


# 生成器函数
re = find01()
print(re)  # 生成器对象
for item in re:
    print(item)  # 元素

# 生成器表达式 重要★
re = (item + 1 for item in list01 if type(item) == int)
print(re)

# 列表推导式
re = [item + 1 for item in list01 if type(item) == int]
for item in re:
    print(item)

# 字典推导式
dict01 = {1: "周一", 2: "周二", "小明": 50, "小红": 90}
dict02 = {k: v for k, v in dict01.items() if type(k) == int}  # 别忘了加.items()
dict03 = {v: k for k, v in dict01.items()}  # 交换kv
print(dict02)
print(dict03)

# 集合推导式
tupledemo = (1, 1, 2, 3, 4, 5, 6, 6)
setnew = {x ** 2 for x in tupledemo if x % 2 == 0}
print(setnew)
