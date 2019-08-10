"""
题目: 顺时针打印矩阵（同LeetCode 螺旋矩阵打印）同 LeetCode 54

题:  输入一个矩阵, 按照从外向里以顺时针的顺序依次打印出每一个数字, 
"""

"""

"""

# -*- coding:utf-8 -*-

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if matrix == []:
            return list()
        
        # 定义 上下左右 未遍历边界
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        result = list()
        # 螺旋遍历
        while True:
            
            for j in range(left, right + 1):
                result.append(matrix[up][j])
                
            up += 1
            if up > down:
                break
                
            for i in range(up, down + 1):
                result.append(matrix[i][right])
                
            right -= 1
            if right < left:
                break
                
            for j in range(right, left - 1, -1):
                result.append(matrix[down][j])
                
            down -= 1
            if down < up:
                break
                
            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
                
            left += 1
            if left > right:
                break
                
        return result
            

