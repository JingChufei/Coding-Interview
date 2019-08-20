"""
题目: 第一个只出现一次的字符

题: 在一个字符串(1 <= 字符串长度 <= 10000, 全部由字母组成)中找到第一个只出现一次的字符, 并返回它的位置
例如 "abaccdeff" 输出 "b"
"""

"""
哈希表
"""

#-*-coding:utf-8-*-
class Solution:

    def FirstNotRepeatingChar(self, s):

        d = {}
        for char in s:

            if char in d:
                d[char] += 1

            else:
                d[char] = 1

        for char in s:

            if d[char] == 1:
                return char




if __name__ == "__main__":
    s = Solution()
    print(s.FirstNotRepeatingChar("abaccdeff"))
    
