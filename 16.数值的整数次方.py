"""
题目: 数值的整数次方

题: 实现函数double Power(double base, int exponent)，求base的exponent次方、不得使用库函数，同时不需要考虑大数问题。

"""

"""
考察边界处理
"""


class Solution:

    def Power(self, base, exponent):

    	# 定义全局变量 来标识是否出错
    	g_InvalidInput = False

    	if base == 0 and exponent < 0:
    		g_InvalidInput = True
    		return 0

    	if exponent >= 0:
    		return self.PowerWithUnsignedExponent(base, exponent)

    	return 1 / self.PowerWithUnsignedExponent(base, -exponent)


    def PowerWithUnsignedExponent(self, base, exponent):

    	res = 1
    	for i in range(exponent):
    		res *= base

    	return res


"""
用递归优化 PowerWithUnsignedExponent():
	例: 要求一个数的32次方, 我们先求16次方, 再取平方, 以此类推
	公式:
		a^n = a^(n / 2) * a^(n / 2) n为偶数
		a^n = a^((n - 1) / 2) * a^((n - 1) / 2) * a n为奇数
"""

class Solution:

	def __init__(self):
		# 定义实例变量 来标识是否出错
		self.g_InvalidInput = False

    def Power(self, base, exponent):

    	if base == 0 and exponent < 0:
    		self.g_InvalidInput = True
    		return 0

    	if exponent >= 0:
    		return self.PowerWithUnsignedExponent(base, exponent)

    	return 1 / self.PowerWithUnsignedExponent(base, -exponent)


    def PowerWithUnsignedExponent(self, base, exponent):

    	# 特殊情况
    	if exponent == 0:
    		return 1

    	# 递归终止条件
    	if exponent == 1:
    		return base

    	res = self.PowerWithUnsignedExponent(base, exponent >> 1)
    	res = res * res

    	# 判断奇偶
    	if exponent % 2 == 1:
    		res = res * base

    	return res
    	
