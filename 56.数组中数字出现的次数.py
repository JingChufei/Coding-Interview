"""
题目: 数组中数字出现的次数

题: 一个整型数组里除了两个数字之外, 其他的数字都出现了两次. 请写程序找出这两个只出现一次的数字.
"""

"""
思路: 位运算
注: 异或 为数字的二进制, 在每一位上进行运算, 相同为0 不同为1
将数组分为两部分, 每部分都为 只有一个数字出现一次, 其余数字出现两次
如何分呢? 
    所有数字异或一遍 之后的结果为 只出现一次的两个数的异或
    这个值从右数 第一个为1的位置 表示在这个位置 这两个数一个为0一个为1
    按照这个位置来划分 为0的在一边 为1的在另一边 则出现两次的被分到一边 且 要求的两个数被分到两边
    最后分别异或 即得所求
"""

#-*-coding:utf-8-*-

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):

        if len(array) < 2:
            return

        resultEOR = 0
        for i in array:
            resultEOR = resultEOR ^ i

        index = self.FindFirstBit(resultEOR)

        res1, res2 = 0, 0
        for j in array:
            if self.IsBit(j, index):
                res1 ^= j
            else:
                res2 ^= j
        return [res1, res2]
            
    
    def FindFirstBit(self, num):
        '''
        用于在整数num的二进制表示中找到最右边是1的位
        '''
        indexBit = 0
        while (num & 1 == 0 and indexBit < 32):
            num = num >> 1
            indexBit += 1
        return indexBit


    def IsBit(self, num, indexBit):
        '''
        用于判断在num的二进制表示中从右边起的indexBit位是否为1
        '''
        num = num >> indexBit
        return (num & 1)


"""
拓展
题目: 数组中数字出现的次数

题: 一个整型数组里除了一个数字之外, 其他的数字都出现了三次. 请写程序找出这一个只出现一次的数字.
"""

"""
思路: 位运算
记录数组中所有数字二进制表示的所有位上的和
    若某一位置的和能被3整除, 说明要求的数字在这一位是0
    若某一位置的和不能被3整除, 说明要求的数字在这一位是1
"""
    
