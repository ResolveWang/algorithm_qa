"""
问题描述，给定一棵二叉树的头结点head,按照如下两种标准分别实现二叉树
边界节点的逆时针打印。
标准一：
1.头结点为边界节点。
2.叶节点为边界节点。
3.如果节点在其所在的层中是最左或者最右的，那么也是边界节点
标准二：
1.头结点为边界节点
2.叶节点为边界节点
3.树左边界延伸下去的路径为边界节点
4.树右边界延伸下去的路径为边界节点

要求：
1）如果节点数为N,两种标准实现的时间复杂度要求为O(N)，额外空间复杂度
要求为O(h),h为树的高度
2）两种标准都要求逆时针顺序且不重复打印所有的边界节点
"""

from binarytree.toolcls import Node


class PrintEdgeNode:
    # 求高度的方法
    @classmethod
    def get_height(cls, head, start):
        if head is None:
            return start
        return max(cls.get_height(head.left, start + 1), cls.get_height(head.right, start + 1))

    # 层序遍历，需要求每一层对应的元素，可以使用这种方法
    @classmethod
    def get_each_level(cls, head, level, all_levels):
        if head is None:
            return None

        if not all_levels[level]:
            all_levels[level].append(head)
        if len(all_levels[level]) == 1:
            all_levels[level].append(head)
        else:
            all_levels[level][1] = head
        cls.get_each_level(head.left, level + 1, all_levels)
        cls.get_each_level(head.right, level + 1, all_levels)

    @classmethod
    def print_way1(cls, head):
        if head is None:
            return
        height = cls.get_height(head, 0)
        all_levels = [list() for _ in range(height)]
        cls.get_each_level(head, 0, all_levels)
        i = 0
        while i < height:
            print(all_levels[i][0].value, end=' ')
            i += 1
        cls.print_leaf_not_in_map(head, 0, all_levels)
        cur = height - 1
        while cur > 0:
            print(all_levels[cur][1].value, end=' ')
            cur -= 1

    @classmethod
    def print_leaf_not_in_map(cls, head, l, all_levels):
        if head is None:
            return

        if head is not None and head.left is None and head.right is None and head not in all_levels[l]:
            print(head.value, end=' ')

        cls.print_leaf_not_in_map(head.left, l + 1, all_levels)
        cls.print_leaf_not_in_map(head.right, l + 1, all_levels)

    @classmethod
    def print_left_edge(cls, head, is_print):
        if head is None:
            return
        if is_print or (head.left is None and head.right is None):
            print(head.value, end=' ')
        cls.print_left_edge(head.left, is_print)
        if head.left is None and is_print:
            sec_print = True
        else:
            sec_print = False
        cls.print_left_edge(head.right, sec_print)

    @classmethod
    def print_right_edge(cls, head, is_print):
        if head is None:
            return
        if head.left is None and is_print:
            sec_print = True
        else:
            sec_print = False
        cls.print_right_edge(head.left, sec_print)

        cls.print_right_edge(head.right, is_print)
        if is_print or (head.left is None and head.right is None):
            print(head.value, end=' ')

    @classmethod
    def print_way2(cls, head):
        if head is None:
            return
        print(head.value, end=' ')

        if head.left is not None and head.right is not None:
            cls.print_left_edge(head.left, True)
            cls.print_right_edge(head.right, True)
        else:
            if head.left is not None:
                cls.print_way2(head.left)
            else:
                cls.print_way2(head.right)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.right = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.left.right.left = Node(7)
    head.left.right.right = Node(8)
    head.right.left.left = Node(9)
    head.right.left.right = Node(10)
    head.left.right.right.right = Node(11)
    head.right.left.left.left = Node(12)
    head.left.right.right.right.left = Node(13)
    head.left.right.right.right.right = Node(14)
    head.right.left.left.left.left = Node(15)
    head.right.left.left.left.right = Node(16)
    PrintEdgeNode.print_way1(head)
    print()
    PrintEdgeNode.print_way2(head)