"""
问题描述：给定一棵二叉树的头结点head,已知其中所有节点的值都不一样，找出含有节点
最多的搜索二叉树，并返回这棵子树的头结点。

要求：如果节点数为N，要求时间复杂度为O(N)，额外空间复杂度为O(h)，h为二叉树的高度。
"""


import sys

from binarytree.toolcls import Node
from binarytree.q3 import PrintTree


class BiggestSubBstTree:
    @classmethod
    def get_biggest_sub_bst_tree(cls, head):
        if head is None:
            return
        record = [0 for _ in range(3)]
        return cls.visit_in_last_order(head, record)

    @classmethod
    def visit_in_last_order(cls, head, record):
        if head is None:
            record[0] = 0
            record[1] = sys.maxsize
            record[2] = -sys.maxsize
            return None
        value = head.value
        left = head.left
        right = head.right

        left_bst = cls.visit_in_last_order(head.left, record)
        left_size = record[0]
        left_min = record[1]
        left_max = record[2]

        right_bst = cls.visit_in_last_order(head.right, record)
        right_size = record[0]
        right_min = record[1]
        right_max = record[2]
        # 这里找左子树最小的点，是为了right_bst的right_min，同理，右子树最大的点也是为了left_bst的left_max
        record[1] = min(left_min, value)
        record[2] = max(right_max, value)

        if left == left_bst and right == right_bst and left_max < value < right_min:
            record[0] = left_size + right_size + 1
            return head

        record[0] = max(left_size, right_size)
        if left_size > right_size:
            return left_bst
        else:
            return right_bst


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

    PrintTree.print_tree(head)
    bst = BiggestSubBstTree.get_biggest_sub_bst_tree(head)
    PrintTree.print_tree(bst)
