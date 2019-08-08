"""
题目: 链表中倒数第k个节点

题: 输入一个链表，输出该链表中倒数第k个结点.
"""

"""
思路: 
	两个指针 first second
	first 先走 k - 1 步
	second 跟着走 直到 first 走到尾
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        first = head

        for i in range(k - 1):
        	first = first.next

        second = head
        while first.next:
        	first = first.next
        	second = second.next

        return second

