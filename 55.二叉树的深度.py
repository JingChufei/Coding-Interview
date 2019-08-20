"""
题: 输入一棵二叉树, 求该树的深度.
从根结点到叶结点依次经过的结点(含根, 叶结点)形成树的一条路径, 最长路径的长度为树的深度.
"""

"""
递归
"""

#-*-coding:utf-8-*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.max_length = 0

    def TreeDepth(self, root):

        if not root:
            return 0

        self.recur(root, 1)
        return self.max_length

    def recur(self, root, n):

        if not root.left and not root.right:

            if n > self.max_length:
                self.max_length = n

        else:

            if root.left:
                self.recur(root.left, n + 1)
            if root.right:
                self.recur(root.right, n + 1)





if __name__ == "__main__":
    s = Solution()
    
