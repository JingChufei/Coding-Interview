def heap_sort(l):


    def sift_down(start, end):
        """
        从 start索引 开始, 调整完全二叉树, 使 以start为根的树为最大堆
        end 为 以列表表示的完全二叉树的最大索引
        """
        root = start

        while True:

            # 左孩子索引
            child = 2 * root + 1

            # 若无孩子节点 则跳出循环
            if child > end:
                break

            # 选择左右孩子中的较大值索引
            if child + 1 <= end and l[child] < l[child + 1]:
                child += 1

            # 根节点的值 小于 孩子节点的值, 则 交换位置 并 更新根节点索引
            if l[root] < l[child]:
                # 交换位置
                l[root], l[child] = l[child], l[root]
                # 更新索引
                root = child

            # 根节点的值已经是最大 则跳出循环
            else:
                break


    # 创建最大堆
    # 从下往上调整所有父节点
    for start in range(len(l) // 2 - 1, -1, -1):
        sift_down(start, len(l) - 1)

    # 堆排序
    for end in range(len(l) - 1, 0, -1):
        # 从堆中取出最大值 (l[0]) 即交换堆顶和最后的元素
        l[0], l[end] = l[end], l[0]
        # 调整堆顶元素 end - 1 是因为此时 end索引 表示已经取出的元素
        sift_down(0, end - 1)

def main():
    l = [3, 6, 2, 3, 4, 1, 7]
    heap_sort(l)
    print(l)

if __name__ == "__main__":
    main()
