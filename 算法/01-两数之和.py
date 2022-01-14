"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案
"""
import time
t1 = time.time()


class Solution:
    # 暴力迭代
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 排序+双指针
    def twoSum1(self, nums, target):
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if (temp[i] + temp[j]) > target:
                j = j - 1
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            else:
                break
        p = nums.index(temp[i])
        nums.pop(p)
        k = nums.index(temp[j])
        if k >= p:
            k = k + 1
        return [p, k]

    # 哈希
    def twoSum2(self, nums, target):
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target - nums[i]) is not None:
                return [hashset.get(target - nums[i]), i]
            hashset[nums[i]] = i


a = Solution()
nums = [3, 3]
re = a.twoSum(nums, 6)
print(time.time()-t1)
re1 = a.twoSum1(nums, 6)
re2 = a.twoSum2(nums, 6)


