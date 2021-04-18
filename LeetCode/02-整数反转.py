class Solution:
    def reverse(self, x):
        str_1 = str(x)  # 转成字符串
        abs_x = abs(x)  # 对x取绝对值
        # 1.因为正负区间范围不同，所以先判断负数情况：
        if str_1[0] == "-":
            # 输入的是负数，输出也是负数
            re = -int(str(abs_x)[::-1])  # re是反转后的数字，注意前面要加负号
        else:
            # 输入的是正数
            re = int(str_1[::-1])
        if re < -2147483648 or re > 2147483647:
            return 0
        else:
            return re

    # 解法2
    def reverse2(self, x):
        min = -2 ** 31
        max = 2 ** 31 - 1
        max_lenth = len(str(max))  # 求出字符串长度
        sx = str(x)  # 数字转成字符串
        is_negative = False  # 非负数
        if sx[0] == '-':
            sx = sx[len(sx):0:-1]  # 去掉负号
            is_negative = True  # 负数
        if len(sx) > max_lenth:  # ？？？
            return 0
        else:
            if is_negative:
                result = -int(sx)
                if result >= min:
                    return result
                else:
                    return 0
            else:
                sx = sx[::-1]
                result = int(sx)
                if result <= max:
                    return result
                else:
                    return 0


x = -156
s = Solution()
a = s.reverse(x)
b = s.reverse2(x)
print(a)
print(b)
