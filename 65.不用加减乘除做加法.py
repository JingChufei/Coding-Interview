"""
题目: 不用加减乘除做加法

题: 写一个函数 求两个整数之和 不能用四则运算符号
"""

"""
位运算
"""

#-*-coding:utf-8-*-

class Solution:
    def Add(self, a, b):

        # 还有进位
        while b:

            # 加后不考虑进位 与 异或 相同
            sum_ = (a ^ b) & 0xffffffff
            # 进位: 与 后 左移1位
            carry = ((a & b) << 1) & 0xffffffff

            a = sum_
            b = carry

        if a<0x7fffffff:
            return a
        else:
            return ~(a^0xffffffff)
