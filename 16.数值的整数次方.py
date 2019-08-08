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
