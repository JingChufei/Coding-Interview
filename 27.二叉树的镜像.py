"""
题目: 二叉树的镜像

题: 操作给定的二叉树, 将其变换为源二叉树的镜像.
"""

"""

"""

# -*- coding:utf-8 -*-
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Solution:

    def Mirror(self, root: TreeNode) -> TreeNode:
        # write code here

        if not root:
        	return

        left = self.Mirror(root.left)
        right = self.Mirror(root.right)

        root.left = right
        root.right = left

        return root
