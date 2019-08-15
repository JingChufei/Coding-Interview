"""
题目: 数字序列中某一位的数字

题: 数字以 0123456789101112131415...的格式序列化到一个字符序列中.
在这个序列中, 第5位(从0开始计数)是5, 第13位是1, 第19位是4, 等等.
请写一个函数, 求任意第n位对应的数字.
"""

"""
找规律
    0~9 有10个数字
    10~99 有 90 * 2 个数字
    100~999 有 900 * 2 个数字
"""

#-*-coding:utf-8-*-
class Solution:

    def digitAtIndex(self, index: int) -> int:

        # 个位情况
        if index <= 9:
            return index

        # 大于个位情况
        start = 10
        index = index - 10
        count = 90
        order = 2

        while index > count * order:

            index -= count * order
            order += 1
            count *= 10

        num = index // order
        mod = index % order

        base = 10 ** (order - 1)

        res = base + num

        return res // (10 ** (order - mod - 1)) % 10


if __name__ == "__main__":
    s = Solution()
    print(s.digitAtIndex(8))
