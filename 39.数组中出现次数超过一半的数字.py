"""
题目: 数组中出现次数超过一半的数字

题: 数组中有一个数字出现的次数超过数组长度的一半, 请找出这个数字.
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}.
由于数字2在数组中出现了5次, 超过数组长度的一半, 因此输出2.如果不存在则输出0.
"""

"""

"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        if not numbers:
            return 0

        n = len(numbers)

        res = numbers[0]
        count = 1

        for i in range(1, n):

            if count == 0:
                res = numbers[i]
                count = 1

            elif numbers[i] == res:
                count += 1

            else:
                count -= 1

        def CheckMoreThanHalf(numbers, number):

            count = 0
            for i in range(len(numbers)):
                if numbers[i] == number:
                    count += 1

            if count * 2 > len(numbers):
                return True
            return False

        if CheckMoreThanHalf(numbers, res):
            return res
        return 0

        return res
