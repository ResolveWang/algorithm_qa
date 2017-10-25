"""
问题描述：给定一个有序数组sortArr,已知其中没有重复值，用这个有序数组生成一棵平衡二叉搜索树，并且该搜索二叉树
中序遍历结果与sortArr一致。
"""


from binarytree.toolcls import Node
from binarytree.q3 import PrintTree


class ReconstructBalancedBST:
    @classmethod
    def reconstruct(cls, arr):
        if len(arr) == 0 or arr is None:
            return None

        return cls.reconstruct_detail(arr, 0, len(arr)-1)

    @classmethod
    def reconstruct_detail(cls, arr, start, end):
        if start > end:
            return None

        pos = (start + end)//2
        node = Node(arr[pos])

        node.left = cls.reconstruct_detail(arr, start, pos-1)
        node.right = cls.reconstruct_detail(arr, pos+1, end)

        return node


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    PrintTree.print_tree(ReconstructBalancedBST.reconstruct(arr))