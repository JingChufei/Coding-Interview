"""
题目：二叉搜索树的第K大节点

题：给定一颗二叉搜索树，请找出其中的第k小的结点。
"""

"""
中序遍历
"""

#-*-coding:utf-8-*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def KthNode(self, root, k):

        if not root or k <= 0:
            return None

        res=[]
        
        # 中序遍历
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root)
            inorder(root.right)

        inorder(root)

        if len(res) < k:
            return None
        return res[k - 1]



if __name__ == "__main__":
    s = Solution()
    
