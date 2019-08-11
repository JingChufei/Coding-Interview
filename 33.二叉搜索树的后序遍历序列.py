"""
题: 二叉搜索树的后序遍历序列

题目: 输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历的结果. 
如果是则输出Yes, 否则输出No. 假设输入的数组的任意两个数字都互不相同.
"""

"""
递归
"""

# -*- coding:utf-8 -*-
class Solution:

    def VerifySquenceOfBST(self, sequence: list) -> bool:
        # write code here

        # 若为空 则不是二叉搜索树
        if not sequence:
            return False

        # 递归终止条件 只剩一个节点
        if len(sequence) == 1:
            return True

        # 后序遍历中 根节点值为最后一个元素
        root_val = sequence[-1]

        # index 指向右子树的第一个值
        index = len(sequence) - 1

        for i in range(len(sequence) - 1):

            if sequence[i] > root_val:
                index = i
                break

        # 若右子树的值中有小于根的 则不是二叉搜索树
        for j in range(index, len(sequence) - 1):

            if sequence[j] < root_val:
                return False

        # 如果没有左子树 则只用判断右子树是否为二叉搜索树
        if index == 0:
            return self.VerifySquenceOfBST(sequence[index:-1])

        # 如果没有右子树 则只用判断左子树是否为二叉搜索树
        if index == len(sequence) - 1:
            return self.VerifySquenceOfBST(sequence[:index])

        # 左右子树都有 判断是否都为二叉搜索树
        return self.VerifySquenceOfBST(sequence[:index]) and self.VerifySquenceOfBST(sequence[index:-1])


class Solution:

    def VerifySquenceOfBST(self, sequence):
        # write code here

        if not sequence or len(sequence) <= 0:
            return False

        root = sequence[-1]
        i = 0
        
        # 找出左小右大的分界点i, 此时i属于右子树
        for node in sequence[:-1]:
            if node > root:
                break
            i+=1
        
        # 如果在右子树中有比根节点小的值, 直接返回False
        for node in sequence[i:-1]:
            if node < root:
                return False

        # 判断左子树是否为二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 判断右子树是否为二叉搜索树
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

　　　　 return left and right
