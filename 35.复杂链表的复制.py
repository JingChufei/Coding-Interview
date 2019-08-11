"""
题: 输入一个复杂链表 (每个节点中有节点值, 以及两个指针, 一个指向下一个节点, 另一个特殊指针指向任意一个节点),
返回结果为复制后复杂链表的head.
(注意, 输出结果中请不要返回参数中的节点引用, 否则判题程序会直接返回空)
"""


class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None



class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here

        if not head:
            return None

        self.clone_node(head)
        self.random_connect(head)
        return self.split(head)


    def clone_node(self, head):
        """
        复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
        """
        cur = head

        while cur:
            # clone
            clone = RandomListNode(-1)
            clone.val = cur.val
            clone.next = cur.next

            # cur 指向 其克隆节点
            cur.next = clone
            # 更新 cur
            cur = clone.next


    def random_connect(self, head):
        """
        将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针的后一个结点
        """

        cur = head

        while cur:

            # 若原始节点有random 则 原始节点的克隆节点的random 指向 原始节点random的克隆节点
            if cur.random:
                cur.next.random = cur.random.next

            # 更新 cur 为下一个原始节点
            cur = cur.next.next

    def split(self, head):
        """
        拆分链表: 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
        """

        cur = head

        clone_head = cur.next
        clone = clone_head

        cur.next = clone.next
        cur = cur.next

        while cur:

            # 克隆节点的next 指向 下一个克隆节点
            clone.next = cur.next
            # 更新 clone
            clone = clone.next
            # 原始节点的next 指向 下一个原始节点
            cur.next = clone.next
            # 更新 cur
            cur = cur.next

        return clone_head



