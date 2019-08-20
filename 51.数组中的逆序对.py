"""
题目: 数组中的逆序对

题目描述: 在数组中的两个数字, 如果前面一个数字大于后面的数字, 则这两个数字组成一个逆序对.
输入一个数组, 求出这个数组中的逆序对的总数P.
例如: [7, 5, 6, 4] 5个逆序对 (7, 6) (7, 5) (7, 4) (6, 4) (5, 4)
"""

"""
归并排序
"""

#-*-coding:utf-8-*-
class Solution:

    def InversePairs(self, data):

        if len(data) <= 0:
            return 0

        n = len(data)
        copy = [0] * n

        # copy数组为原数组data的复制,在后面充当辅助数组
        for i in range(n):
            copy[i] = data[i]

        count = self.core(data, copy, 0, n - 1)

        return count
    
    def core(self, data, copy, start, end):

        if start == end:
            copy[start] = data[start]
            return 0

        # n为划分后子数组的长度
        n = (end - start) // 2 

        left = self.core(copy, data, start, start + n)
        right = self.core(copy, data, start + n + 1, end)

        # 初始化i为前半段最后一个数字的下标
        i = start + n
        # 初始化j为后半段最后一个数字的下标
        j = end

        # index为辅助数组的指针，初始化其指向最后一位
        index = end
        # 准备开始计数
        count = 0

        # 对两个数组进行对比取值的操作
        while i >= start and j >= start + n + 1:

            # 存在逆序对
            if data[i] > data[j]:
                count += j - start - n
                copy[index] = data[i]
                index -= 1
                i -= 1
                
            else:
                copy[index] = data[j]
                index -= 1
                j -= 1
        
        # 剩下一个数组未取完的操作
        while i >= start:
            copy[index] = data[i]
            index -= 1
            i -= 1
        while j >= start + n + 1:
            copy[index] = data[j]
            index -= 1
            j -= 1
        
        return count + left + right





if __name__ == "__main__":
    s = Solution()
    print(s.InversePairs([7, 5, 6, 4]))
    

