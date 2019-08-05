"""
题目: 矩阵中的路径 LeetCode 79

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

"""
回溯法
递归
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.lx = len(board) - 1
        self.ly = len(board[0]) - 1
        
        m = len(board)
        n = len(board[0])
        
        # 不允许重复使用字母
        seen = [[0 for i in range(n)] for j in range(m)]
        
        # 从board的每一个位置开始寻找
        for i in range(m):
            for j in range(n):
                if self.search(board, word, 0, i, j, seen):
                    return True
                
        return False
        
        
    # word[index:] 与 board[x][y]开头的所有情况 是否匹配?
    def search(self, board, word, index, x, y, seen):
        
        # 坐标变换方式 上 右 下 左
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # 当前search的是word最后一个字符
        if index == len(word) - 1:
            return board[x][y] == word[index]
        
        # 当前search的不是word最后一个字符 

        # 若匹配 须递归查看后面的字符是否匹配
        # 若不匹配 返回False
        if board[x][y] == word[index]:
            
            seen[x][y] = 1
            
            # 上左下右递归
            for i in range(4):
                
                x_ = x + d[i][0]
                y_ = y + d[i][1]
                
                # 1.不越界 2.没看过 3.后面也匹配
                if 0 <= x_ <= self.lx and 0 <= y_ <= self.ly and not seen[x_][y_] and self.search(board, word, index+1, x_, y_, seen):
                    return True
                   
            # 上右下左 递归完之后没有匹配的单词 还原seen
            seen[x][y] = 0
        
        
        # word[index:] 与 board[x][y]开头的所有情况 不匹配
        return False
            



