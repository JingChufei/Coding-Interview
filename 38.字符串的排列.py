"""
题: 字符串的排列

题目: 输入一个字符串, 按字典序打印出该字符串中字符的所有排列.
例如输入字符串abc, 则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba.
"""

"""
全排列 递归
"""

class Solution:
    def Permutation(self, s):
        # write code here

        if s == "":
            return []

        l = list(s)
        l.sort()

        res = []
        path = []
        self.recur(l, path, res)
        return res

    def recur(self, l, path, res):

        # 递归终止 已经将所有元素都安排好了位置
        if len(l) == 0:
            res.append("".join(path))

        # 遍历当前剩余的元素 将每一个元素(不重复)都放在当前的第一个位置 然后递归剩余元素
        for i in range(len(l)):

            # 避免重复字符
            if i > 0 and l[i] == l[i - 1]:
                continue

            """
            选择 l[i] 坐在这个位置
            将 l[i] 从 l 中"删掉"
            将 l[i] 放在当前位置 path + [l[i]]
            """
            self.recur(l[:i] + l[i+1:], path + [l[i]], res)
