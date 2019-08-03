"""
题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

"""
解题思路：有两个栈stackA,stackB，A为入栈，B为出栈的。
入栈时，直接进入A即可，
出栈时，
	先判断B中是否有元素，如果没有肯定不能pop()，应将A中所有元素倒压在B里面，再pop()最上面（后面）的元素，
	如果有，直接pop()就可以了。两个栈各自先进后出，在一起又实现了队列的先进先出。
"""

stack1 = []
stack2 = []

class queue(object):

	def __init__(self):

		self.s1 = []
		self.s2 = []

	def push(self, value):
		self.s1.append(value)

	def pop(self):

		if self.s2:
			return self.s2.pop()

		elif not self.s1:
			return None

		else:
			while self.s1:
				v = self.s1.pop()
				self.s2.append(v)

			return self.s2.pop()
