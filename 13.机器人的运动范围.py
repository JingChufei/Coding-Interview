"""
题目：机器人的运动范围

题：地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？
"""

"""
回溯法
递归
"""

class Solution:
    def movingCount(self, threshold: int, m: int, n: int) -> int:

        self.threshold = threshold
    	self.lx = m - 1
    	self.ly = n - 1

        # 不能重复计数
        seen = [[0 for j in range(n)] for i in range(m)]

        self.recur(threshold, 0, 0, seen)

        count = 0
        for i in range(m):
        	for j in range(n):
        		count += seen[i][j]

        return count


    def recur(self, threshold, x, y, seen):

    	d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    	if self.check(x, y):

    		seen[x][y] = 1

    		for i in range(4):

    			x_ = x + d[i][0]
    			y_ = y + d[i][1]

    			if 0 <= x_ <= self.lx and 0 <= y_ <= self.ly and not seen[x_][y_]:
    				self.recur(threshold, x_, y_, seen)


    def check(self, x, y):

    	sum = 0
    	while x > 0:
    		sum += x % 10
    		x = x // 10
    	while y > 0:
    		sum += y % 10
    		y = y // 10

    	if sum > self.threshold:
    		return False
    	return True



