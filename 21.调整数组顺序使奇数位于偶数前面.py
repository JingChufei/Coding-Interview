"""
题目: 调整数组的顺序使奇数位于偶数前面

题一: 输入一个整数数组, 实现一个函数来调整该数组中数字的顺序, 使得所有奇数位于数组的前半部分, 所有偶数位于数组的后半部分.
"""

"""
解题思路: 维护两个指针 类似快速排序
"""

class Solution:
    def reOrderArray(self, a):
        # write code here

        n = len(a)

        left = 0
        right = n - 1

        while left < right:

        	while left < right and a[left] % 2 == 1:
        		left += 1

        	a[left], a[right] = a[right], a[left]

        	while left < right and a[right] % 2 == 0:
        		right -= 1

        	a[left], a[right] = a[right], a[left]

        return a
