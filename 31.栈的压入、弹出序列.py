"""
题目: 栈的压入 弹出元素

题: 输入两个整数序列, 第一个序列表示栈的压入顺序, 请判断第二个序列是否为该栈的弹出顺序. 假设压入栈的所有数字均不相等.

例如序列1,2,3,4,5是某栈的压入顺序, 序列4,5,3,2,1是该压栈序列对应的一个弹出序列,
但4,3,5,1,2就不可能是该压栈序列的弹出序列. (注意: 这两个序列的长度是相等的)
"""

"""
压栈序列 pushV
弹出序列 popV
辅助栈 stack

思路:

    当 弹出序列不为空时 循环
        当 还有元素待压入 且 要压入的元素与要弹出的元素相同时 则不用压入辅助栈 直接从两序列删除即可
        当 辅助栈有元素 且 栈顶元素等于要弹出的元素时 则弹出元素 并 从弹出序列中删除
        当 还有要压入的元素时 压入元素 并 从压入序列中删除
        否则 不是弹出序列 False

    退出循环 弹出序列元素全部被弹出 则是弹出序列 True
"""

# -*- coding:utf-8 -*-

class Solution:


    def IsPopOrder(self, pushV, popV):
        # write code here

        stack=[]

        # 当还有元素需要弹出时 继续循环
        while popV:

            # 相当于元素进栈后立即出栈
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)

            # 如果当前辅助栈中的栈顶元素刚好是要弹出的元素, 那么直接弹出
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)

            # 不断往辅助栈中压入元素
            elif pushV:
                stack.append(pushV.pop(0)) 

            else:
                return False

        return True

                


