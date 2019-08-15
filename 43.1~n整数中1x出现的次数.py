"""
题目: 1~n整数中x出现的次数

题: 输入一个整数n, 求1~n这n个整数的十进制表示中1出现的次数.
例如, 输入12, 1~12这些整数中包含1的数字有1, 10, 11, 12一共出现了5次.
"""

"""
例如 1~2593 5 出现次数 https://blog.csdn.net/u010005281/article/details/80085255
"""

#-*-coding:utf-8-*-
class Solution:

    def NumberOf1BetweenXAndN_Solution(self, n: int, x: int) -> int:

        res = 0

        # 从 个位 开始计数
        order = 1

        while n // order > 0:

            # 高位
            high = n // (order * 10)
            # 余数
            mod = n % (order * 10)
            # 目前位的数字
            cur = mod // order
            # 低位
            low = mod % order

            # 目前位数字小于x 则目前位x的个数只与高位有关 high * order
            if cur < x:
                res += high * order
            # 目前位数字大于x 则目前位x的个数只与高位有关 (high + 1) * order
            elif cur > x:
                res += high * order + order
            # 目前位数字等于x 则目前位x的个数 与高位低位都有关 high * order + low + 1
            else:
                res += high * order + low + 1

            order *= 10

        return res



