"""
问题描述：给定一个整型数组arr，已知其中没有重复值，判断arr是否可能是节点值类型为整型的搜索二叉树后序遍历的结果。

进阶：如果整型数组arr中没有重复值，且已知是一棵搜索二叉树的后续遍历结果，通过数组arr重构二叉树。
"""


from binarytree.toolcls import Node


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
                less += 1
            else:
                if more == end:
                    more = i

        if less == -1 or more == end:
            return cls.is_bst_tree_detail(arr, start, end-1)

        if more - less != 1:
            return False

        return cls.is_bst_tree_detail(arr, 0, less) and cls.is_bst_tree_detail(arr, more, end-1)


if __name__ == '__main__':
    my_arr = [2, 1, 3, 6, 5, 7, 4]
    print(ISBST.is_bst_tree(my_arr))