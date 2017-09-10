"""
问题描述：给定一棵二叉树的头结点和一个整数k，二叉树节点为整型，求累加和为sum的
最长路径长度，路径是指从某个节点往下，每次最多选择一个孩子节点或者不选所形成的节点链。

思路：借助"未排序数组中累加和为规定值的最长子数组长度问题"的思路来解决
"""


from binarytree.toolcls import Node


class LongestTreePath:
    @classmethod
    def get_longest_tree_path(cls, head, k):
        if head is None:
            return 0
        sum_node_map = dict()
        sum_node_map.setdefault(0, 0)
        return cls.visit_by_first_order(head, 0, sum_node_map, k, 1, 0)

    @classmethod
    def visit_by_first_order(cls, head, sum, node_map, k, level, max_length):
        if head is None:
            return max_length
        sum += head.value
        if sum not in node_map:
            node_map[sum] = level
        if (sum - k) in node_map:
            sum_k_level = node_map[sum - k]
            if level - sum_k_level > max_length:
                max_length = level - sum_k_level
        max_length = cls.visit_by_first_order(head.left, sum, node_map, k, level + 1, max_length)
        max_length = cls.visit_by_first_order(head.right, sum, node_map, k, level + 1, max_length)

        return max_length


if __name__ == '__main__':
    head = Node(-3)
    head.left = Node(3)
    head.right = Node(-9)
    head.left.left = Node(1)
    head.left.right = Node(0)
    head.left.right.left = Node(1)
    head.left.right.right = Node(6)
    head.right.left = Node(2)
    head.right.right = Node(1)

    print(LongestTreePath.get_longest_tree_path(head, 6))
    print(LongestTreePath.get_longest_tree_path(head, -9))
