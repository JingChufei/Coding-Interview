"""
题目: 表示数值的字符串

题: 请实现一个函数用来判断字符串是否表示数值 (包括整数和小数)
例如, 字符串"+100", "5e2", "-123", "3.1416" 和 "-1E-16" 都表示数值. 
但是"12e", "1a3.14", "1.2.3", "+-5" 和 "12e+4.3" 都不是.
"""

"""
A[.[B]][e|EC] 或 .B[e|EC]
"""

# -*- coding:utf-8 -*-
class Solution:
    
    def isNumeric(self, s: str) -> bool:
        # write code here
        if not s or len(s) <= 0:
            return False

        a = [i.lower() for i in s]

        # 若有e 以e为界 将 数字部分A和B 和 指数部分C 分开
        if 'e' in a:
            index = a.index('e')
            front = a[:index]
            behind = a[index+1:]

            # 指数部分必须为整数
            if '.' in behind or len(behind) == 0:
                return False

            isfront = self.isDigit(front)
            isbehind = self.isDigit(behind)

            return isfront and isbehind

        # 无e 只有数字部分A和B
        else:
            return self.isDigit(a)
        
    def isDigit(self, a):

    	# dot记录 "." 的个数
        dot = 0
        # 允许出现的字符
        allow = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']

        for i in range(len(a)):

            if a[i] not in allow:
                return False

            if a[i]=='.':
                dot += 1

            if a[i] in '+-' and i != 0:
                return False

        if dot > 1:
            return False

        return True




