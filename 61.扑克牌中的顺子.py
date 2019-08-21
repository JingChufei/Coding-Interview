"""
题目: 从扑克牌中随机抽5张牌, 判断是不是一个顺子, 即这5张牌是不是连续的
2~10为数字本身, A为1, J为11, Q为12, K为13, 而大, 小王可以看成任意数字
"""

"""
排序 然后看空隙
"""

#-*-coding:utf-8-*-


class Solution:

    def IsContinuous(self, numbers):

        if not numbers:
            return False

        # 排序
        numbers.sort()
        # 多少个大小王
        zeros = numbers.count(0)

        for i, value in enumerate(numbers[:-1]):

            if value != 0:

                # 有对子就不是顺子
                if value == numbers[i + 1]:
                    return False

                zeros = zeros - (numbers[i + 1] - value - 1)

                if zeros < 0:
                    return False

        return True
