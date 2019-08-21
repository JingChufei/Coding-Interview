"""
题目: 队列的最大值

描述: 给定一个数组和滑动窗口的大小, 请找出所有滑动窗口里的最大值
例如: 数组 [2, 3, 4, 2, 6, 2, 5, 1] 窗口大小3 那么一共存在6个滑动窗口 最大值分别为[4, 4, 6, 6, 6, 5]
"""

"""
双端队列
"""

#-*-coding:utf-8-*-

class Solution:

    def maxInWindows(self, num, window):

        if not num or window <= 0:
            return []

        res = []

        if len(num) >= window and window >= 1:

            # 队列中存的是索引 队首索引为当前滑动窗口最大值的索引
            deque=[]

            for i in range(window):

                while deque and num[i] >= num[deque[-1]]:
                    deque.pop()

                deque.append(i)
            
            for i in range(window, len(num)):

                # 添加上一步滑动窗口的最大值
                res.append(num[deque[0]])

                # 要入队的元素大于队列末尾索引代表元素 则删除队列末尾
                while (deque and num[i] >= num[deque[-1]]):
                    deque.pop()

                # 队首索引 小于等于 i - window, 即队首索引已经不在滑动窗口内, 则删除队首索引
                if deque and deque[0] <= i - window:
                    deque.pop(0)

                # 新元素入队
                deque.append(i)

            # 将最后一个滑动窗口的最大值添加到res
            res.append(num[deque[0]])

        return res
