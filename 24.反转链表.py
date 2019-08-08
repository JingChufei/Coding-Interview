"""
题目: 反转链表

题: 输入一个链表, 反转链表并输出反转后链表的头节点.
"""

"""
三个指针 pre cur temp(用于存储cur的下一个指针)
"""

# -*- coding:utf-8 -*-
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def ReverseList(self, head: ListNode) -> ListNode:

    	if not head or not head.next:
    		return head

    	pre = head
    	cur = pre.next

    	# 头节点指向None
    	head.next = None

    	while cur:

    		# 存储下一个节点
    		temp = cur.next

    		# 翻转
    		cur.next = pre

    		# 更新
    		pre = cur
    		cur = temp

    	return pre

"""
两个指针
	head 翻转后的尾节点
	res 头节点

递归
	递归函数返回 翻转后的以head为尾节点的链表的头节点 res
"""      
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        else:
            res = self.reverseList(head.next)

            # 翻转
            head.next.next = head

            # 尾节点指向None
            head.next = None

            # 返回当前头节点
            return res
        



