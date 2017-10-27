"""
问题描述：从二叉树的节点A出发，可以向上或者向下走，但是沿途的节点只能经过一次，当到达节点B时，路径上的节点
数叫做A到B的距离。现给定一棵二叉树的头结点head，求整个二叉树上节点间的最大距离。

要求：如果二叉树的节点数为N，时间复杂度要求为O(N)
"""


from binarytree.toolcls import Node


class MaxDistance:
    @classmethod
    def find_max_distance(cls, head):
        record = [0]
        return cls.find_max_distance_detail(head, record)

    @classmethod
    def find_max_distance_detail(cls, head, record):
        if head is None:
            record[0] = 0
            return 0

        lmax = cls.find_max_distance_detail(head.left, record)
        max_from_left = record[0]

        rmax = cls.find_max_distance_detail(head.right, record)
        max_from_right = record[0]

        record[0] = max([max_from_left, max_from_right]) + 1

        cur_node_length = max_from_left + max_from_right + 1

        return max([lmax, rmax, cur_node_length])


if __name__ == '__main__':
    head1 = Node(1)
    head1.left = Node(2)
    head1.right = Node(3)
    head1.left.left = Node(4)
    head1.left.right = Node(5)
    head1.right.left = Node(6)
    head1.right.right = Node(7)
    head1.left.left.left = Node(8)
    head1.right.left.right = Node(9)
    print(MaxDistance.find_max_distance(head1))

    head2 = Node(1)
    head2.left = Node(2)
    head2.right = Node(3)
    head2.right.left = Node(4)
    head2.right.right = Node(5)
    head2.right.left.left = Node(6)
    head2.right.right.right = Node(7)
    head2.right.left.left.left = Node(8)
    head2.right.right.right.right = Node(9)
    print(MaxDistance.find_max_distance(head2))