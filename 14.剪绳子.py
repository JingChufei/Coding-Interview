"""
题目：剪绳子

题：给你一根长度为n的绳子，请把绳子剪成m段(m,n都是整数，且n>1,m>1),
每段绳子的长度记为k[0],k[1],k[2],...,k[m]。请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2，3，3的三段，此时得到的最大乘积为18。

"""

"""
动态规划
"""
class Solution:
    def Cut(self, n):
        
    	# 绳子最少被剪成2段
    	if n < 2:
    		return 0
    	if n == 2:
    		return 1
    	if n == 3:
    		return 2

    	# p[i]为 长度为i的绳子的所有切分的最大乘积(i > 3)
    	p = [0 for i in range(n+1)]
    	p[0] = 0
    	p[1] = 1
    	p[2] = 2
    	p[3] = 3

    	for i in range(4, n+1):

    		# 当前遍历的所有切分的最大乘积
    		temp_max = 0

    		for j in range(1, i//2 + 1):

    			temp = p[j] * p[i - j]

    			if temp > temp_max:
    				temp_max = temp

    		p[i] = temp_max

    	return p[n]

"""
贪婪算法

证明:
	当 n >= 5 时:
		2(n - 2) > n 
		3(n - 3) > n
	说明 当绳子剩下的长度大于等于5时, 就把它剪成长度为2或者3的绳子段
	且 当 n >= 5 时:
		3(n - 3) >= 2(n - 2)

"""
class Solution:
    def Cut(self, n):

        if n < 2:
        	return 0
        if n == 2:
        	return 1
        if n == 3:
        	return 2

        # 尽可能剪长度为3的绳子段
        num_3 = n // 3

        # 当绳子最后剩4时 不能剪去3 因为 2 * 2 > 3 * 1
        if n - num_3 * 3 == 1:
        	num_3 -= 1

        # 绳子剩余2的个数
        num_2 = (n - num_3 * 3) // 2

        return (3 ** num_3) * (2 ** num_2)

