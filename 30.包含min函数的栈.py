"""
题目: 包含min函数的栈

题: 定义栈的数据结构, 请在该类型中实现一个能够得到栈最小元素的min函数. 在该栈中, 调用min push pop的时间复杂度都是O(1)
"""

"""
维护一个 min_stack 栈顶存放当前最小元素
"""

# -*- coding:utf-8 -*-

class Solution:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):

        self.stack.append(value)

        if self.min_stack == [] or value < self.min():
            self.min_stack.append(vaule)

        else:
            self.min_stack.append(self.min())


    def pop(self):

        if self.stack == []:
            return None

        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack[-1]


