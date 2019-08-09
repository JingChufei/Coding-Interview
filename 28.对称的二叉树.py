"""
题目: 对称的二叉树

请实现一个函数, 用来判断一颗二叉树是不是对称的. 注意, 如果一个二叉树同此二叉树的镜像是同样的, 定义其为对称的
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

    def isSymmetrical(self, root: TreeNode) -> bool:
        # write code here

        if not root:
        	return True

        return self.recur(root.left, root.right)


    def recur(self, root1, root2):

    	if not root1 and not root2:
    		return True

    	if not root1 or not root2:
    		return False

    	return root1.val == root2.val and self.recur(root1.left, root2.right) and self.recur(root1.right, root2.left)

        

