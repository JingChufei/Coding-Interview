"""
题: 序列化二叉树 LeetCode 297

题目: 请实现两个函数, 分别用来序列化和反序列化二叉树
"""

"""
前序遍历
"""

# Serialization 
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def recur(root, string):
            """
            递归辅助函数
            root: 当前根节点 
            string: 前序遍历到当前根节点时的字符串

            返回 前序遍历遍历完 当前根节点所代表的整棵树 后的字符串
            """

            # 递归终止条件
            if not root:
                string += "None,"

            # 前序遍历: 根 左 右
            else:
                string += str(root.val) + ","

                string = recur(root.left, string)
                string = recur(root.right, string)

            return string

        s = recur(root, "")
        return s


    def deserialize(self, s):
        """Decodes your encoded s to tree.
        :type s: str
        :rtype: TreeNode
        """

        def recur(q):
            """
            递归辅助函数
            q: 一棵树(可能是子树) 的前序遍历序列

            返回 这棵树的根节点
            """

            # 递归终止条件
            if q[0] == "None":
                q.pop(0)
                return None

            # 前序遍历: 根 左 右
            root = TreeNode(int(q[0]))
            q.pop(0)

            root.left = recur(q)
            root.right = recur(q)

            return root

        q = s.split(",")
        root = recur(q)
        return root

