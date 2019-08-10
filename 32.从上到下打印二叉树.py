"""
题目1: 从上到下打印二叉树

题: 不分行从上到下打印二叉树每个节点 同一层的节点按照从左到右的顺序打印
"""

"""
迭代
"""

# -*- coding:utf-8 -*-
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class Solution:

    def PrintFromTopToBottom(self, root: TreeNode) -> list:
        # write code here

        if not root:
            return []

        result = []

        # 辅助队列 先进先出
        queue = [root]

        while queue:

            root = queue.pop(0)
            result.append(root.val)

            if root.left:
                queue.append(root.left)

            if root.right:
                queue.append(root.right)

        return result


"""
题目2: 分行从上往下打印二叉树

题: 分行从上到下打印二叉树每个节点 同一层的节点按照从左到右的顺序打印
例如
1
2 3
4 5 6 7
"""
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        result = []

        # 辅助队列
        queue = [(root, 0)]

        while queue:

            root, order = queue.pop(0)

            if len(result) - 1 < order:
                result.append([])

            result[order].append(root.val)

            if root.left:
                queue.append((root.left, order+1))
            if root.right:
                queue.append((root.right, order+1))

        return result




class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = list()
        if not root:
            return []
        
        # 队列
        q = list()
        q.append(root)
        
        while q:
            
            # 存放该层节点的val
            order = list()
            # 该层节点个数
            n = len(q)
            
            for i in range(n):
                # 出队列
                node = q.pop(0)
                # 记录该节点val
                order.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # 切片 浅拷贝
            result.append(order[:])
            
        return result


"""
题目3: 之字形打印二叉树

题: 分行从上到下打印二叉树每个节点 同一层的节点按照从左到右的顺序打印
例如
1
3 2
4 5 6 7
"""
class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return None

        result = []

        # 辅助队列
        queue = [(root, 0)]

        while queue:

            root, order = queue.pop(0)

            if len(result) - 1 < order:
                result.append([])

            if order % 2 == 0:
                result[order].append(root.val)
            else:
                result[order].insert(0, root.val)

            if root.left:
                queue.append((root.left, order+1))
            if root.right:
                queue.append((root.right, order+1))

        return result



class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = list()
        if not root:
            return []
        
        # 队列
        q = list()
        q.append(root)
        
        # 定义 从左往右 还是 从右往左 的bool值
        l2r = 1
        
        while q:
            
            # 该层节点val列表
            order = list()
            # 该层节点个数
            n = len(q)
            
            if l2r:
                for i in range(n):
                    node = q.pop(0)
                    order.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
            else:
                for i in range(n):
                    node = q.pop(0)
                    order.insert(0, node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            result.append(order[:])
            # 更改 l2r
            l2r = l2r ^ 1
            
        return result
