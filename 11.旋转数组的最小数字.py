"""
题目:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):

    	n = len(rotateArray)

    	left = 0
    	right = n - 1
    	mid = left

    	while rotateArray[left] >= rotateArray[right]:

    		# 相差1 表明left指向左边有序数组的最后一个元素, right指向右边有序数组的第一个元素, 即最小元素
    		if right - left == 1:
    			mid = right
    			break

    		mid = (left + right) // 2

    		# 如果 左边有序列表的起始值 == 右边有序列表的末尾值 == 中间值, 那么无法判断中间的元素位于哪一边, 即无法缩小范围, 只能顺序查找
    		if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
    			return minValue(rotateArray, left, right)

    		# mid指向元素在左边的有序列表
    		if rotateArray[mid] >= rotateArray[left]:
    			left = mid
    		# mid指向元素在右边的有序列表
    		else:
    			right = mid

    	return rotateArray[mid]


    def minValue(self, rotateArray, left, right):
    	"""
		顺序查找
    	"""

    	res = rotateArray[left]

    	for i in range(left+1, right+1):
    		if res > rotateArray[i]:
    			res = rotateArray[i]

    	return res
