# 思路 y是1-19 x是1-y  返回xy

for y in range(1, 10):
    for x in range(1, y + 1):
        print('%d*%d=%d' % (x, y, x * y), end='')
    print('')
