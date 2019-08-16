"""
题目: 最长不含重复字符的子字符串

题: 请从字符串中找出一个最长的不包含重复字符的子字符串, 计算该最长字符串的长度.
假设字符串中只包含‘a’-‘z’的字符. 例如, 在字符串"arabcacfr"中, 最长的不含重复字符的子字符串是"acfr", 长度为4.
"""

"""
哈希表
"""

#-*-coding:utf-8-*-
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        # 哈希表 key: 用过的字符 value: 原先出现的最大索引
        usedChar = {}
        for i in range(len(s)):
            """
            当前字符在原先出现过 且 当前start小于等于当前字符原先出现的索引 
            即当前最长子串中包含当前字符 则start更新为原先索引+1 跳过原先字符
            此时 不用判断是否为最长子串 因为 减去的大于等于1 加上的为1
            """
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            
            else:
                maxLength = max(maxLength, i - start + 1)

            # 更新哈希表 key: 用过字符 value: 出现的最大索引
            usedChar[s[i]] = i
        
        return maxLength


if __name__=="__main__":
    print(Solution().lengthOfLongestSubstring('arabcacfr'))
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('pwwkew'))
