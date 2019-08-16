"""
题: 把数组排成最小的数

题目: 输入一个正整数数组, 把数组里所有数字拼接起来排成一个数, 打印能拼接出的所有数字中最小的一个.
例如输入数组{3，32，321}, 则打印出这三个数字能排成的最小数字为321323.
"""

"""
定义比较规则
"""

#-*-coding:utf-8-*-
class Solution:

    def MaxNumberLength(self, numbers):

        res = ""

        str_list = list(map(str, numbers))

        n = len(str_list)
        self.quick_sort(str_list, 0, n - 1)
        
        return "".join(str_list)
        


    def quick_sort(self, numbers, left, right):

        if left >= right:
            return 

        v = numbers[left]
        lt = left
        i = left + 1
        gt = right + 1

        while i < gt:

            if self.compare_if_equal(numbers[i], v):
                i += 1

            elif self.compare_if_smaller(numbers[i], v):
                numbers[lt + 1], numbers[i] = numbers[i], numbers[lt + 1]
                lt += 1
                i += 1

            else:
                numbers[gt - 1], numbers[i] = numbers[i], numbers[gt - 1]
                gt -= 1

        numbers[left], numbers[lt] = numbers[lt], numbers[left]
        lt -= 1

        self.quick_sort(numbers, left, lt)
        self.quick_sort(numbers, gt, right)

        

    def compare_if_smaller(self, a: str, b: str) -> bool:
        """
        if a < b
        """

        ab = a + b
        ba = b + a

        n = len(ab)
        for i in range(n):
            if ab[i] < ba[i]:
                return True
            elif ab[i] > ba[i]:
                return False

        return False


    def compare_if_equal(self, a: str, b: str) -> bool:
        """
        if a == b
        """

        ab = a + b
        ba = b + a

        n = len(ab)
        for i in range(n):
            if ab[i] != ba[i]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.MaxNumberLength([3, 321, 32]))

