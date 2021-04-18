"""
思路：

整体思路是尽可能多的排除掉无关 行/列 ，可以从 第一排最后一个/第一列最后一个 开始搜索，这里选择从 第一排最后一个 开始
由于行列规则等价，搜索策略 先按行排除/按列排除 也是等价的，这里选择 按行排除
搜索规则：小于 target 则向左搜索，大于 则向下搜索，可以保证 global search
若超出 矩阵大小 则意味着没有匹配 target，输出 False

"""


class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        while matrix[i][j] != target:  # 从矩阵第一行最后一个元素开始遍历
            if matrix[i][j] < target: # 如果元素小于target，遍历下一行
                i += 1
            else: # 如果
                j -= 1
            if i >= row or j < 0: # 超出范围返回False
                return False
        return True

