"""
题目: 正则表达式匹配

题: 请实现一个函数用来匹配包括'.'和'*'的正则表达式.
模式中的字符'.'表示任意一个字符, 而'*'表示它前面的字符可以出现任意次（包含0次).
在本题中, 匹配是指字符串的所有字符匹配整个模式. 例如, 字符串"aaa"与模式"a.a"和"ab*ac*a"匹配, 但是与"aa.a"和"ab*a"均不匹配.
"""

"""
递归
"""

class Solution:
    def match(self, s: str, pattern: str) -> bool:

    	# 递归终止条件
    	if len(s) == 0 and len(pattern) == 0:
    		return True

    	if len(s) > 0 and len(pattern) == 0:
    		return False

    	# 当模式中的第二个字符是"*"时:
    	if len(pattern) >= 2 and pattern[1] == "*":

    		#如果字符串第一个字符跟模式第一个字符匹配(相等或匹配到"."), 可以有3种匹配方式:
    		if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == "."):

    			# 字符* 匹配 0个 1个 大于1个
    			return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)

    		#如果字符串第一个字符跟模式第一个字符不匹配, 只有1种匹配方式:
    		else:
    			# 字符* 匹配 0个
    			return self.match(s, pattern[2:])

        # 当模式中的第二个字符不是"*"时:
    	else:

          	#1.如果字符串第一个字符和模式中的第一个字符匹配(相等或匹配到"."), 那么有1种匹配方式:
    		if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == "."):

    			# 匹配1个
    			return self.match(s[1:], pattern[1:])

    		# 不匹配
    		else:

    			return False


