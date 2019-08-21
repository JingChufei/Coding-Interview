"""
题目: 把n个骰子扔在地上, 所有骰子朝上一面的点数之和为s. 输入n, 打印出s的所有可能的值出现的概率.
"""

"""
动态规划
dp[c][k] 表示 c - 1 个骰子点数和为k, 则
dp[c][k] = dp[c-1][k-1] + dp[c-1][k-2] + dp[c-1][k-3] + dp[c-1][k-4] + dp[c-1][k-5] + dp[c-1][k-6]
"""

#-*-coding:utf-8-*-


def get_ans(n):

    dp = [[0 for j in range(6 * n)] for i in range(n)]
 
    for i in range(6):
        dp[0][i] = 1

    for i in range(1, n): 

        for j in range(i, 6 * (i + 1)):   # [i][i-1]的时候, 频数为0(例如2个骰子不可能投出点数和为1)

            dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] +dp[i - 1][j - 4] + \
                            dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]
 
    count = dp[n - 1]
    return count  # 算得骰子投出每一个点数的频数, 再除以总的排列数即可得到频率
