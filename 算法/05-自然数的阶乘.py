def func(x):
    m = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        m *= i
    return m


x = 10
v = func(x)
print("%d的阶乘是%d" % (x, v))
