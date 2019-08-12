"""
题目: 连续子数组的最大和 LeetCode 53

题: 输入一个整形数组, 数组里有正数也有负数.
数组中的一个或连续多个整数组成一个子数组.求所有子数组的和的最大值.要求时间复杂度为O(n)
"""

"""
动态规划
"""

#-*-coding:utf-8-*-
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        n = len(nums)
        res = nums[0]

        # 动态规划函数
        dp = nums[0]

        for i in range(1, n):

            dp = max(dp + nums[i], nums[i])
            if dp > res:
                res = dp

        return res

