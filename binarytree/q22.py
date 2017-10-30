"""
问题描述：已知一棵二叉树所有的节点值不同，给定这棵二叉树正确的先序和中序数组，不要重建整棵树，
而是通过这两个数组直接生成正确的后序数组。
"""

from array import array


class GenPosArr:
    @classmethod
    def gen_pos_arr(cls, pre, mid):
        if pre is None or mid is None:
            return

        d = dict()
        for index, value in enumerate(mid):
            d[value] = index

        l = [0 for _ in range(len(pre))]
        cls.gen_pos_arr_detail(pre, 0, len(pre)-1, mid, 0, len(mid)-1, l, len(l)-1, d)
        return l

    @classmethod
    def gen_pos_arr_detail(cls, pre, pre_start, pre_end, mid, mid_start, mid_end, l, l_pos, d):
        if pre_start > pre_end:
            return l_pos
        print(pre_start)
        l[l_pos] = pre[pre_start]
        l_pos -= 1
        index = d[pre[pre_start]]

        l_pos = cls.gen_pos_arr_detail(pre, pre_start+index-mid_start+1, pre_end, mid, index+1, mid_end, l, l_pos, d)
        return cls.gen_pos_arr_detail(pre, pre_start+1, pre_start+index-mid_start, mid, mid_start, index-1, l, l_pos, d)


if __name__ == '__main__':
    pre_arr = [1, 2, 4, 5, 3, 6, 7]
    mid_arr = [4, 2, 5, 1, 6, 3, 7]
    pos_arr = GenPosArr.gen_pos_arr(pre_arr, mid_arr)
    print(pos_arr)
