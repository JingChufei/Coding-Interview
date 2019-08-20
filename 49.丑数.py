"""
题: 丑数

题目: 把只包含因子2, 3和5的数称作丑数(Ugly Number)
例如6, 8都是丑数, 但14不是, 因为它包含因子7.
习惯上我们把1当做是第一个丑数. 求按从小到大的顺序的第N个丑数.
"""

"""
数学规律
"""

#-*-coding:utf-8-*-
class Solution:

    def GetUglyNumber_Solution(self, index):

        if index <= 0:
            return 0

        # res按升序存储所有丑数
        res = [1]
        # 计数
        nextIndex = 1
        # t2 为 res[t2] * 2 > res[-1] 的最小索引
        # t3 为 res[t2] * 3 > res[-1] 的最小索引
        # t5 为 res[t2] * 5 > res[-1] 的最小索引
        t2 = t3 = t5 = 0

        while nextIndex < index:

            # 下一个丑数是这三个数中的最小值
            min_val = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            # 将下一个丑数添加到res中
            res.append(min_val)

            # 更新t2 t3 t5
            while res[t2] * 2 <= min_val:
                t2 += 1
            while res[t3] * 3 <= min_val:
                t3 += 1
            while res[t5] * 5 <= min_val:
                t5 += 1

            nextIndex += 1

        return res[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.GetUglyNumber_Solution(6))
    
