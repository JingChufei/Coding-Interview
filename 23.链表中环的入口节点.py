"""
题目: 如果一个链表中包含环, 如何找出环的入口节点?
"""

"""
思路:
	1.链表中是否有环
		快慢指针 是否能相遇
	2.环的起点 https://github.com/JingChufei/LeetCode/blob/master/142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.md
		双指针
			one从相遇地点开始往后走
			two从head开始走
			相遇地点即是 环的起点
	3.环的长度
		相遇地点开始往后走 边走边计数 再次到达相遇地点 即可知道环的长度
"""

# -*- coding:utf-8 -*-
class ListNode:  

    def __init__(self, val):  
        self.val = val 
        self.next = None  



class Solution:  

    def EntryNodeOfLoop(self, head):

    	if not head:
    		return None

    	slow = head
    	fast = head

    	entry = head

    	while fast and fast.next:

    		slow = slow.next
    		fast = fast.next.next

    		if slow == fast:

    			while entry != slow:

    				entry = entry.next
    				slow = slow.next

    			return entry

    	return None




