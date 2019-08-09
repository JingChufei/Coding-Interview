"""
题目: 树的子结构

题: 输入两棵二叉树A和B, 判断B是不是A的子结构.
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

    def HasSubtree(self, s: TreeNode, t: TreeNode) -> TreeNode:
        # write code here
        res = False

        if s and t:

            if s.val == t.val:
                res = self.isSubTree(s, t)

            if not res:
                res = self.HasSubtree(s.left, t)

            if not res:
                res = self.HasSubtree(s.right, t)

        return res
    
    def isSubTree(self, s, t):

        if t == None:
            return True

        if s == None:
            return False

        if s.val != t.val:
            return False

        return self.isSubTree(s.left,t.left) and self.isSubTree(s.right,t.right)

