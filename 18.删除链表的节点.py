"""
题目: 删除链表中的节点

题一: 在O(1)时间内删除链表节点. 给定单向链表的头指针和一个节点指针, 定义一个函数在O(1)时间内删除该节点.
"""

"""

"""


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def delete_node(self, head, del_node):
        """
        删除指定节点
        """

       	# 删除的节点不是尾节点
       	if del_node.next:
       		# 下个节点的值 赋给 要删除的节点
       		del_node.val = del_node.next.val
       		# 要删除的节点的next指向下个节点的next 等同于 删除了要删除的节点
       		del_node.next = del_node.next.next

       	# 删除的节点是尾节点 且 不是头节点
       	elif head.next:
       		node = head
       		while node.next != del_node:
       			node = node.next

       		node.next = None

       	# 删除的节点是尾节点 且 是头节点
       	else:
       		head = None

       	return head


"""
题目: 删除链表中重复的节点.

题: 在一个排序的链表中, 请删除重复的节点, 如1-2-3-3-4-4-5在重复的节点被删除后为1-2-5.
"""
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None



class Solution:
    def deleteDuplication(self, head):

    	node = head
    	while node.next:

    		while node.next and node.val == node.next.val:
    			node.next = node.next.next

    		node = node.next

    	return head

