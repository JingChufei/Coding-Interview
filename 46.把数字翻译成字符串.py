"""
题目: 把数字翻译成字符串

题: 给定一个数字, 我们按照如下规则把它翻译为字符串:
0翻译成“a”, 1翻译成“b”，……, 11翻译成“1”,……, 25翻译成“z”.
一个数字可能有多个翻译. 例如: 12258有5种不同的翻译, 分别是“bccfi”, “bwfi”, “bczi”, “mcfi”和“mzi”. 
请编程实现一个函数, 用来计算一个数字有多少种不同的翻译方法.
"""

"""
自下而上 动态规划

1 2 2 5 8
5 3 2 1 1

以8开头 1种
以5开头 1. 5单独翻译为一个字母 情况数为 以8开头的情况数 2. 58组合翻译一个字母 不可行 所以总共有1种
以2开头 1. 2单独翻译为一个字母 情况数为 以5开头的情况数 2. 25组合翻译一个字母 可行 所以总共有 1 + 1 = 2 种
以2开头 1. 2单独翻译为一个字母 情况数为 以2开头的情况数 2. 22组合翻译一个字母 可行 所以总共有 2 + 1 = 3 种
以1开头 1. 1单独翻译为一个字母 情况数为 以2开头的情况数 2. 12组合翻译一个字母 可行 所以总共有 2 + 3 = 5 种

"""

#-*-coding:utf-8-*-
class Solution:
    def getTranslationCount(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number < 0:
            return 0
        numberStr = str(number)

        return self.getTranslateCount(numberStr)
    
    def getTranslateCount(self, numberStr):

        n = len(numberStr)

        # counts[i] 表示以 i位置 为开头, 总共的情况数
        counts = [0] * n 

        # count = 0
        for i in range(n - 1, -1, -1):

            count = 0

            if i < n - 1:
                # i位置独立翻译为一个字母 此时总共的情况数 == 以i+1位置开头的情况数
                count += counts[i + 1]
            else:
                # i位置是倒数第一个位置
                count = 1
            
            if i < n - 1:
                digit1 = int(numberStr[i])
                digit2 = int(numberStr[i + 1])

                # 10~25之间才能组合
                converted = digit1 * 10 + digit2
                if converted >= 10 and converted <= 25:
                    # i位置和i+1位置组合 翻译为一个字母 此时总共的情况数 == 以i+2位置开头的情况数
                    if i < n - 2:
                        count += counts[i + 2]
                    # i位置和i+1位置 是倒数两个位置
                    else:
                        count += 1

            counts[i] = count

        return counts[0]


