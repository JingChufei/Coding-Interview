# 题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39

"""
1.动态规划
"""
class Solution:
    def Fibonacci(self, n):
        # write code here

        small = 0
        big = 1

        if n <= 0:
        	return 0
        if n == 1:
        	return 1

        for i in range(2, n + 1):
        	sum_i = big + small

        	# 更新
        	small = big
        	big = sum_i

        return big


"""
2.递归
"""
class Solution:
	def Fibonacci(self, n):

		# 递归终止条件
		if n == 0:
			return 0
		if n == 1:
			return 1

		return self.Fibonacci(n-1) + self.Fibonacci(n-2)


"""
题目拓展1：跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

动态规划
"""

class Solution:
	def jumpFloor(self, n):

		first = 1
		second = 2

		if n == 1:
			return first
		if n == 2:
			return second

		for i in range(n - 2):

			res = second + first

			# 更新
			first = second
			second = res

		return second

"""
题目拓展2：变态跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

数学归纳
"""

class Solution:
	def jumpFloor(self, n):

		if n <= 0:
			return 0

		return 2 ** (n - 1)


"""
题目拓展3：矩形覆盖

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？ 

解题思路：这道题本质上还是斐波那契数列问题，注意分析n=0,1,2,3,...的值的情况。
"""

class Solution:
	def rectCover(self, n):

		first = 1
		second = 2

		if n == 1:
			return first
		if n == 2:
			return second

		for i in range(n - 2):
			res = second + first

			first = second
			second = res

		return second


"""
题目拓展3：矩形覆盖

我们可以用3*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个3*1的小矩形无重叠地覆盖一个3*n的大矩形，总共有多少种方法？ 

解题思路：动态规划
"""

class Solution:
	def rectCover(self, n):

		if n <= 2:
			return 1
		if n == 3:
			return 2

		first = 1
		second = 1
		third = 2

		for i in range(4, n + 1):

			res = third + first

			# 更新
			first = second
			second = third
			third = res

		return third




