"""
题目: 二进制中1的个数

题: 输入一个整数, 输出该数二进制表示中1的个数. 其中负数用补码表示.

"""


class Solution:
    def number_of_1(self, n):

    	count = 0

    	if n < 0:
    		n = abs(n)

    	while n > 0:

    		# n & 1 两数的二进制表示做 与 运算, 若为1 表示n的二进制表示的最右边位为1
    		if n & 1:
    			count += 1

    		"""
			位运算 n的二进制表示 右移1位

			虽然在结果上和除以2等价 但是除法比位移效率低得多
    		"""
    		n = n >> 1

    	return count

"""
牛逼解法
	把1个整数减去1 再和原来整数做 与 运算, 会把该整数二进制表示的最右边的1变为0
"""
class Solution:
    def number_of_1(self, n):

    	count = 0

    	if n < 0:
    		n = abs(n)

    	while n:
    		count += 1

    		n = (n - 1) & n

    	return count

