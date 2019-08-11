"""
题目: 二叉树中和为某一值的路径

题: 输入一颗二叉树和一个整数, 打印出二叉树中结点值的和为输入整数的所有路径.
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径.


"""

"""
递归
"""

# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表, 内部每个列表表示找到的路径
    def FindPath(self, root: TreeNode, expectNumber: int) -> List[List[int]]:

        if not root:
            return []

        res = []
        path = [root.val]

        self.recur(root, expectNumber, path, res)

        return res


    def recur(self, root, num, path, res):

        # 叶子节点 递归终止
        if not root.left and not root.right:

            if num - root.val == 0:
                res.append(path)

        # 左子树递归
        if root.left:
            self.recur(root.left, num - root.val, path + [root.left.val], res)            

        # 右子树递归
        if root.right:
            self.recur(root.right, num - root.val, path + [root.right.val], res)           


class Solution:
    # 返回二维列表, 内部每个列表表示找到的路径
    def FindPath(self, root: TreeNode, expectNumber: int) -> List[List[int]]:

        if not root:
            return []

        res = []
        path = []

        self.recur(root, expectNumber, path, res)

        return res


    def recur(self, root, num, path, res):
        """
        root: 当前节点
        num: 当前还剩多少值
        path: 从根节点到当前节点(不包括当前节点)路径
        res: 路径列表
        """

        # 叶子节点 递归终止
        if not root.left and not root.right:

            if num - root.val == 0:
                path += [root.val]
                res.append(path)

        # 左子树递归
        if root.left:
            self.recur(root.left, num - root.val, path + [root.val], res)            

        # 右子树递归
        if root.right:
            self.recur(root.right, num - root.val, path + [root.val], res)             
        




