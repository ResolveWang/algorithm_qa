"""
问题描述：给定彼此独立的两棵树头结点分别为t1和t2，判断t1树是否包含t2树全部的拓扑结构。
"""

from binarytree.toolcls import Node


class BSTTop:
    @classmethod
    def is_bst_top(cls, t1, t2):
        return cls.visit_in_pre(t1, t2) or cls.is_bst_top(t1.left, t2) or cls.is_bst_top(t1.right, t2)

    @classmethod
    def visit_in_pre(cls, t1, t2):
        if t2 is None:
            return True

        if t1 is None or t1.value != t2.value:
            return False

        return cls.visit_in_pre(t1.left, t2.left) and cls.visit_in_pre(t1.right, t2.right)


if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)
    t1.left.left.left = Node(8)
    t1.left.left.right = Node(9)
    t1.left.right.left = Node(10)

    t2 = Node(2)
    t2.left = Node(4)
    t2.left.left = Node(8)
    t2.right = Node(5)

    print(BSTTop.is_bst_top(t1, t2))