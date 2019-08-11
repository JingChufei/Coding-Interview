"""
题: 二叉搜索树与双向链表

题目: 输入一棵二叉搜索树, 将该二叉搜索树转换成一个排序的双向链表.
要求不能创建任何新的结点, 只能调整树中结点指针的指向.
"""

"""
递归
"""

# -*- coding:utf-8 -*-

class Solution:

    def Convert(self, root):
        # write code here
        if not root:
            return

        head = root
        
        # 寻找树中最小的值作为双向链表的head    
        while head.left:
            head = head.left

        self.recur(root)

        return head
    
    def recur(self, root):

        if not root.left and not root.right:
            return

        # 有左子树
        if root.left:

            pre = root.left

            # 将左子树转化为双向链表
            self.recur(root.left)

            # 寻找双向链表中最右边的值(即最大值) 为root的前一个值pre
            while pre.right:
                pre = pre.right

            # 链接 pre root
            pre.right = root
            root.left = pre

        # 有右子树
        if root.right:

            next = root.right

            # 将右子树转化为双向链表
            self.recur(root.right)

            # 寻找双向链表中最左边的值(即最小值) 为root的后一个值next
            while next.left:
                next = next.left

            # 链接 root next
            next.left = root
            root.right = next


