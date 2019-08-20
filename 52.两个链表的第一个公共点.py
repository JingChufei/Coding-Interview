"""
题目: 两个链表的第一个公共节点

题: 输入两个链表, 找出它们的第一个公共节点.
"""

"""
第一个链表独立部分长度为A
第二个链表独立部分长度为B
公共部分长度为C
则 A+C+B = B+C+A
"""

#-*-coding:utf-8-*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, head1, head2):

        cur1 = head1
        cur2 = head2

        while cur1 != cur2:

            if not cur1.next:
                cur1 = head2
            else:
                cur1 = cur1.next

            if not cur2.next:
                cur2 = head1
            else:
                cur2 = cur.next

        return cur1





if __name__ == "__main__":
    s = Solution()
    

