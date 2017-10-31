"""
问题描述：给定一棵完全二叉树的头结点head，返回这棵树的节点个数。

要求：如果完全二叉树的节点数为N，请实现时间复杂度低于O(N)的解法。
"""


from binarytree.toolcls import Node


class BCTNodeCounter:
    @classmethod
    def get_bct_node_num(cls, head):
        if head is None:
            return 0

        return cls.bs(head, 1, cls.get_most_left_level(head, 1))

    @classmethod
    def bs(cls, head, l, h):
        if h == l:
            return 1
        if h == cls.get_most_left_level(head.right, l + 1):
            return cls.bs(head.right, l+1, h) + (1 << (h-l))
        else:
            return cls.bs(head.left, l+1, h) + (1 << (h-l-1))

    # 由于是完全二叉树，所以左边的层级可以代表整棵树的层级
    @classmethod
    def get_most_left_level(cls, head, start):
        while head is not None:
            start += 1
            head = head.left
        return start - 1


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    num = BCTNodeCounter.get_bct_node_num(head)
    print(num)