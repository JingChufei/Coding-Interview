"""
题目: 构建乘积数组

题: 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]. 不能使用除法.
"""

"""

"""

#-*-coding:utf-8-*-

class Solution:
    def multiply(self, A):

        n=len(A)

        C=[1] * len(A)
        D=[1] * len(A)
        B=[1] * len(A)

        for i in range(1, n):
            C[i] = C[i - 1] * A[i - 1]

        for j in (range(0, n - 1))[::-1]:
            D[j] = D[j + 1] * A[j + 1]
        
        for k in range(0, n):
            B[k] = C[k] * D[k]

        return B
