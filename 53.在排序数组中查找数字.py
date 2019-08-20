"""
题目: 统计一个数字在排序数组中出现的次数.

"""

"""
二分查找
"""

#-*-coding:utf-8-*-

class Solution:

    def GetNumberOfK(self, data, k):

        count = 0
        n = len(data)

        l = 0
        r = n - 1

        while l <= r:

            mid = (l + r) // 2

            if data[mid] == k:
                count += 1
                break

            elif data[mid] < k:
                l = mid + 1

            else:
                r = mid - 1

        if count == 0:
            return 0

        i = mid - 1
        j = mid + 1

        while i >= 0:
            if data[i] == k:
                count += 1
                i -= 1
            else:
                break

        while j <= n - 1:
            if data[j] == k:
                count += 1
                j += 1
            else:
                break

        return count




if __name__ == "__main__":
    s = Solution()
    
