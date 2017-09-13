"""
问题描述：给定一棵二叉树的头结点head,已知所有节点的值都不一样，返回其中最大的符合搜索二叉树条件
的最大拓扑结构的大小。
"""

from binarytree.toolcls import Node


class BiggestTop:
    @classmethod
    def find_biggest_top(cls, head):
        if head is None:
            return 0
        count_list = list()
        cls.visit_by_pre_order(head, count_list)
        return max(count_list)

    @classmethod
    def visit_by_pre_order(cls, head, count_list):
        if head is None:
            count_list.append(0)
            return
        count_list.append(cls.top_length(head))
        cls.visit_by_pre_order(head.left, count_list)
        cls.visit_by_pre_order(head.right, count_list)

    @classmethod
    def top_length(cls, head):
        if head is None:
            return 0
        queue = [head]
        count = 0
        while len(queue) > 0:
            node = queue.pop(0)
            temp = head
            if node.value != temp.value:
                while temp is not None:
                    if node.value == temp.value:
                        if node.left is not None:
                            queue.append(node.left)
                        if node.right is not None:
                            queue.append(node.right)
                        count += 1
                        break
                    elif node.value < temp.value:
                        temp = temp.left
                    else:
                        temp = temp.right
            else:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count += 1

        return count


if __name__ == '__main__':
    head = Node(6)
    head.left = Node(1)
    head.left.left = Node(0)
    head.left.right = Node(3)
    head.right = Node(12)
    head.right.left = Node(10)
    head.right.left.left = Node(4)
    head.right.left.left.left = Node(2)
    head.right.left.left.right = Node(5)
    head.right.left.right = Node(14)
    head.right.left.right.left = Node(11)
    head.right.left.right.right = Node(15)
    head.right.right = Node(13)
    head.right.right.left = Node(20)
    head.right.right.right = Node(16)
    print(BiggestTop.find_biggest_top(head))