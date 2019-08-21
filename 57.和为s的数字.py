"""
题目: 和为s的数字

题目描述: 输入一个递增排序的数组和一个数字s, 在数组中查找两个数, 使得他们的和正好是s, 如果有多对数字的和等于S, 则输出任意一对即可.
 
输出描述: 对应每个测试案例, 输出两个数, 小的先输出.
"""

"""
双指针
"""

#-*-coding:utf-8-*-

class Solution:

    def FindNumbersWithSum(self, array, s):


        n = len(array)
        l = 0
        r = n - 1

        while l < r:

            if array[l] + array[r] == s:
                return [array[l], array[r]]

            elif array[l] + array[r] < s:
                l += 1

            else:
                r -= 1

        return []


s = Solution()
a = [1, 2, 4, 7, 11, 15]
s = 15
s.FindNumbersWithSum(a, s)

"""
题目: 和为s的连续正数序列

题目描述: 输入一个正数s, 打印出所有和为s的连续正数序列(至少含有两个数)
例如: 输入15, 由于 1+2+3+4+5 == 4+5+6 == 7+8 == 15, 所以打印出3个连续序列 1~5, 4~6, 7~8
"""

"""
双指针
    small 序列的起始
    big 序列的终止
由于至少含有两个数 所以 small 最大为 (s + 1) // 2
"""

def solution(s):

    # 双指针
    small = 1
    big = 2

    res = []

    threshold = (s + 1) // 2

    while small < threshold:

        # small 到 big 的和
        temp = (small + big) * (big - small + 1) / 2

        if temp < s:
            big += 1
        elif temp > s:
            small += 1
        else:
            res.append([i for i in range(small, big+1)])
            big += 1

    return res
