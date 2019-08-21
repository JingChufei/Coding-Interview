"""
题目: 股票的最大利润

题: [9, 11, 8, 5, 7, 12, 16, 14] 5买入 16卖出
"""

"""

"""

#-*-coding:utf-8-*-

def solution(l):

    n = len(l)
    if n <= 1:
        return 0

    temp_min = l[0]
    interest = 0

    for i in range(1, n):

        if l[i] < temp_min:
            temp_min = l[i]

        else:
            temp_interest = l[i] - temp_min
            if temp_interest > interest:
                interest = temp_interest

    return interest

a = [9, 11, 8, 5, 7, 12, 16, 14]
solution(a)

