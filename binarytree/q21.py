"""
问题描述：已知一棵二叉树的所有节点值都不同，给定这棵二叉树正确的先序、中序和后续数组，请分别用三个
函数实现任意两种数组结合重构原来的二叉树，并返回重构二叉树的头结点。
"""


from binarytree.toolcls import Node
from binarytree.q3 import PrintTree


class ReconstructTree:
    @classmethod
    def reconstruct_in_pre_order(cls, pre_arr, in_arr):
        if len(pre_arr) == 0 or len(in_arr) == 0:
            return None
        d = dict()
        for index, value in enumerate(in_arr):
            d[value] = index

        return cls.reconstruct_in_pre_order_detail(pre_arr, 0, len(pre_arr)-1, in_arr, 0, len(in_arr)-1, d)

    @classmethod
    def reconstruct_in_pre_order_detail(cls, pre_arr, pre_start, pre_end, in_arr, in_start, in_end, d):
        if pre_start > pre_end:
            return
        root = Node(pre_arr[pre_start])
        pos = d.get(pre_arr[pre_start])
        # 注意 这里 pos - in_start表示前序遍历数组的长度，再加上pre_start就表示分割后的前序数组的范围
        root.left = cls.reconstruct_in_pre_order_detail(pre_arr, pre_start + 1, pre_start+(pos-in_start), in_arr,
                                                        in_start, pos-1, d)
        root.right = cls.reconstruct_in_pre_order_detail(pre_arr, pre_start+(pos-in_start)+1, pre_end, in_arr,
                                                         pos+1, in_end, d)

        return root

    @classmethod
    def reconstruct_in_mid_order(cls, mid_arr, pos_arr):
        if len(mid_arr) == 0 or len(pos_arr) == 0:
            return None
        d = dict()
        for index, value in enumerate(mid_arr):
            d[value] = index
        return cls.reconstruct_in_mid_order_detail(mid_arr, 0, len(mid_arr) - 1, pos_arr, 0, len(pos_arr) - 1, d)

    @classmethod
    def reconstruct_in_mid_order_detail(cls, mid_arr, mid_start, mid_end, pos_arr, pos_start, pos_end, d):
        if pos_start > pos_end:
            return

        root = Node(pos_arr[pos_end])
        pos = d.get(pos_arr[pos_end])
        root.left = cls.reconstruct_in_mid_order_detail(mid_arr, mid_start, pos-1, pos_arr, pos_start, pos_start +
                                                        pos - mid_start - 1, d)
        root.right = cls.reconstruct_in_mid_order_detail(mid_arr, pos+1, mid_end, pos_arr, pos_start + pos - mid_start,
                                                         pos_end - 1, d)

        return root

    @classmethod
    def reconstruct_in_pre_pos_order(cls, pre, pos):
        if not pre or not pos:
            return

        d = dict()
        for index, value in enumerate(pos):
            d[value] = index
        return cls.reconstruct_in_pre_pos_order_detail(pre, 0, len(pre)-1, pos, 0, len(pos)-1, d)

    @classmethod
    def reconstruct_in_pre_pos_order_detail(cls, p, pi, pj, s, si, sj, d):
        head = Node(s[sj])
        sj -= 1

        if pi == pj:
            return head

        pi += 1
        index = d.get(p[pi])

        head.left = cls.reconstruct_in_pre_pos_order_detail(p, pi, pi+index-si, s, si, index, d)

        head.right = cls.reconstruct_in_pre_pos_order_detail(p, pi+index-si+1, pj, s, index+1, sj, d)
        return head


if __name__ == '__main__':
    cur_pre = [1, 2, 4, 5, 8, 9, 3, 6, 7]
    cur_in = [4, 2, 8, 5, 9, 1, 6, 3, 7]
    cur_pos = [4, 8, 9, 5, 2, 6, 7, 3, 1]
    head = ReconstructTree.reconstruct_in_pre_order(cur_pre, cur_in)
    PrintTree.print_tree(head)

    head = ReconstructTree.reconstruct_in_mid_order(cur_in, cur_pos)
    PrintTree.print_tree(head)

    head = ReconstructTree.reconstruct_in_pre_pos_order(cur_pre, cur_pos)
    PrintTree.print_tree(head)