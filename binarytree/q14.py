"""
问题描述：给定一个整型数组arr，已知其中没有重复值，判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果。

进阶：如果整型数组arr中没有重复值，且已知是一棵搜索二叉树的后续遍历结果，通过数组arr重构二叉树。
"""


from binarytree.toolcls import Node

from binarytree.q3 import PrintTree

class ISBST:
    @classmethod
    def is_bst_tree(cls, arr):
        if len(arr) == 0 or not arr:
            return False
        return cls.is_bst_tree_detail(arr, 0, len(arr) - 1)

    @classmethod
    def is_bst_tree_detail(cls, arr, start, end):
        if start == end:
            return True

        less = -1
        more = end
        for i in range(start, end):
            if arr[i] < arr[end]:
                less = i
            else:
                if more == end:
                    more = i

        if less == -1 or more == end:
            return cls.is_bst_tree_detail(arr, start, end-1)

        if more - less != 1:
            return False

        return cls.is_bst_tree_detail(arr, start, less) and cls.is_bst_tree_detail(arr, more, end-1)

    @classmethod
    def recontruct_bst(cls, arr):
        if arr is None:
            return None
        return cls.recontruct_bst_detail(arr, 0, len(arr) - 1)

    @classmethod
    def recontruct_bst_detail(cls, arr, start, end):
        if start > end:
            return None

        less = -1
        more = end

        cur_node = Node(arr[end])

        for i in range(start, end):
            if arr[i] < arr[end]:
                less = i
            else:
                more = i if more == end else more

        cur_node.left = cls.recontruct_bst_detail(arr, start, less)
        cur_node.right = cls.recontruct_bst_detail(arr, more, end-1)
        return cur_node


if __name__ == '__main__':
    my_arr = [2, 1, 3, 6, 5, 7, 4]
    print(ISBST.is_bst_tree(my_arr))
    from binarytree.q1 import RecursiveVisit
    RecursiveVisit.visit_in_first_order(ISBST.recontruct_bst(my_arr))
    PrintTree.print_tree(ISBST.recontruct_bst(my_arr))