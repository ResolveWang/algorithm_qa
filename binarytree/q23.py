"""
问题描述：给定一个整数N，如果N<1，代表空树结构，否则代表中序遍历的结果为{1, 2, 3, ..., N}。
请返回可能的二叉树结构有多少。

例如，N=-1时，代表空树结构，返回1；N=2时，满足中序遍历为{1， 2}的二叉树结构只有两种结构，所以
结果返回为2

进阶：N的含义不变，假设可能的二叉树结构有M种，请返回M个二叉树的头结点，每一颗二叉树代表一种可能
的结构。
"""

from itertools import product
from copy import deepcopy

from binarytree.toolcls import Node
from binarytree.q3 import PrintTree


class TreeFromInt:
    @classmethod
    def get_total_num(cls, n):
        if n < 2:
            return 1

        total = 0
        for i in range(1, n+1):
            total += cls.get_tree_num_from_int(n, i)

        return total

    @classmethod
    def get_tree_num_from_int(cls, n, i):
        if i == 1:
            return cls.get_total_num(n-1)
        if i == n:
            return cls.get_total_num(n-1)
        return cls.get_total_num(i-1) * cls.get_total_num(n-i)

    @classmethod
    def get_roots(cls, n):
        return cls.get_root(1, n)

    @classmethod
    def get_root(cls, start, end):
        res = list()
        if start > end:
            res.append(None)

        for i in range(start, end+1):
            node = Node(i)
            left_nodes = cls.get_root(start, i-1)
            right_nodes = cls.get_root(i+1, end)
            r = product(left_nodes, right_nodes)
            for left, right in r:
                node.left = left
                node.right = right
                res.append(deepcopy(node))
            #
            # for left in left_nodes:
            #     for right in right_nodes:
            #         node.left = left
            #         node.right = right
            #         res.append(cls.clone_tree(node))

        return res

    # @classmethod
    # def clone_tree(cls, node):
    #     if node is None:
    #         return
    #     res = Node(node.value)
    #     res.left = cls.clone_tree(node.left)
    #     res.right = cls.clone_tree(node.right)
    #     return res


if __name__ == '__main__':
    n = 4
    print(TreeFromInt.get_total_num(n))
    rs = TreeFromInt.get_roots(n)
    for r in rs:
        PrintTree.print_tree(r)
