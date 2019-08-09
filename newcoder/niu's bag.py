
"""
https://www.nowcoder.com/practice/bf877f837467488692be703735db84e6?tpId=98&tqId=32831&tPage=1&rp=1&ru=%2Fta%2F2019test&qru=%2Fta%2F2019test%2Fquestion-ranking
"""


class Solution:


    def bag(self, w, n, v):

        # 放满了
        if w == 0:
            return 1

        # 没的可放了
        if n == 0:
            return 1

        # 取出一个
        item = v[0]

        # 可以放
        if item <= w:

            # 选择 放 或 不放
            return self.bag(w - item, n - 1, v[1:]) + self.bag(w, n - 1, v[1:])

        # 不可以放
        else:

            return self.bag(w, n - 1, v[1:])


		
