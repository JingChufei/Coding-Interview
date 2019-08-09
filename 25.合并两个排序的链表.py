"""
题目: 合并两个排序的链表

题: 输入两个单调递增的链表, 输出两个链表合成后的链表, 当然我们需要合成后的链表满足单调不减规则.
"""

"""
归并排序
"""

# -*- coding:utf-8 -*-
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def Merge(self, head1: ListNode, head2: ListNode) -> ListNode:

    	if not head1:
    		return head2
    	if not head2:
    		return head1

    	pre = ListNode(-1)
    	cur = pre

    	while head1 and head2:

    		if head1.val <= head2.val:
    			cur.next = head1
    			head1 = head1.next

    		else:
    			cur.next = head2
    			head2 = head2.next

    		cur = cur.next

    	if head1:
    		cur = head1
    	if head2:
    		cur = head2

    	return pre.next



