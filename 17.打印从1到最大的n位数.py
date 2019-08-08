"""
题目: 打印从1到最大的n位数

题: 输入数字n,按顺序打印出从1到最大的n位十进制数, 比如输入3, 则打印出 1 2 3 一直到最大的3位数999.
"""

"""
解题思路: 需要考虑大数问题, 这是题目设置的陷阱. 可以把问题转换成数字排列问题, 用递归让代码更简洁.
"""


class Solution:

    def Print1ToMaxOfNDigits(self, n):

        if n <= 0:
            return 

        number = ["0"] * n

        for i in range(10):

            number[0] = str(i)
            self.recur(number, n, 0) 


    def recur(self, number, n, index):

    	# 递归终止条件
        if index == n - 1:
            self.PrintNumber(number)
            return

        for i in range(10):
            number[index + 1] = str(i)
            self.recur(number, n, index + 1)


    def PrintNumber(self, number):
        """
		开头是0的字符串不打印
        """

        # 定义函数内全局变量 判读是否以0开头
        isBeginning0 = True

        n = len(number)

        for i in range(n):

        	# 若上一个数字是0 下一个数字不是0 则更新全局变量 不是以0开头
            if isBeginning0 and number[i] != "0":
                isBeginning0 = False

            if not isBeginning0:
                print("{}".format(number[i]), end="")

        # 换行
        print("")



