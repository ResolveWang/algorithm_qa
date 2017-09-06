"""
问题描述：二叉树可以使用常规的三种遍历结果来描述其结构，但是不够直观，尤其是当二叉树中有
重复值的时候，仅通过三种遍历的结果来构造二叉树的真实结构更是难上加难，有时则根本不可能。
给定一棵二叉树的头结点head，已知二叉树节点值的类型为32位整型，请实现一个打印二叉树的函数，
可以直观地展示树的形状，也便于画出真实的结构。

思路：
1）将二叉树逆时针旋转90度，根据其是左子树、右子树或者根节点，选择不同的标志进行组合
2）注意要考虑到大整数，对同一层的兄弟节点要对齐
"""


from binarytree.toolcls import Node


class PrintTree:
    @classmethod
    def print_tree(cls, head):
        if head is None:
            return
        cls.print_in_order(head, 0, 'H', 17)

    @classmethod
    def print_in_order(cls, head, height, char, length):
        if head is None:
            return
        cls.print_in_order(head.right, height + 1, 'v', length)
        cls.print_cur(head, height, char, length)
        cls.print_in_order(head.left, height + 1, '^', length)

    @classmethod
    def print_cur(cls, head, height, char, length):
        print_str = char + str(head.value) + char
        left_str = int((length - len(print_str)) / 2)
        right_str = length - len(print_str) - left_str
        print(' ' * length * height + ' ' * left_str + char + str(head.value) + char + ' ' * right_str)


if __name__ == '__main__':
    import sys

    head = Node(1)
    head.left = Node(-222222222)
    head.right = Node(3)
    head.left.left = Node(sys.maxsize)
    head.right.left = Node(55555555)
    head.right.right = Node(66)
    head.left.left.right = Node(777)
    PrintTree.print_tree(head)