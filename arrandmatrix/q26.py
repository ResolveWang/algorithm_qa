"""
问题描述:给定一个整型数组arr，返回排序后的相邻两个数的最大差值.

举例:
arr=[9, 3, 1, 10],排序后为[1, 3, 9, 10],9和3最大差值是6，返回即可
arr=[5, 5, 5, 5],返回0

要求:
时间复杂度为O(N)
"""

import sys


class MaxDiffValue:
    @classmethod
    def get_max_diff_value(cls, arr):
        if not arr or len(arr) < 2:
            return 0

        length = len(arr)
        max_value = -sys.maxsize
        min_value = sys.maxsize
        for i in arr:
            max_value = max([max_value, i])
            min_value = min([min_value, i])

        if max_value == min_value:
            return 0

        has_num = [False for _ in range(length+1)]
        min_num = [0 for _ in range(length+1)]
        max_num = [0 for _ in range(length+1)]

        for i in arr:
            bid = cls.get_bucket_num(i, length, min_value, max_value)
            if not has_num[bid]:
                min_num[bid] = i
                max_num[bid] = i
                has_num[bid] = True
            else:
                min_num[bid] = min([i, min_num[bid]])
                max_num[bid] = max([i, max_num[bid]])

        max_num_value = 0
        tmp_index = -1
        for i in range(len(has_num)):
            if has_num[i] is True:
                tmp_index = i
                max_num_value = max_num[i]
                break

        max_diff = 0
        for i in range(tmp_index+1, len(has_num)):
            if has_num[i]:
                min_num_value = min_num[i]
                max_diff = max([min_num_value-max_num_value, max_diff])
                max_num_value = max_num[i]

        return max_diff

    @classmethod
    def get_bucket_num(cls, value, length, min_value, max_value):
        return int((value - min_value) * length / (max_value - min_value))


if __name__ == '__main__':
    my_arr = [9, 3, 1, 10]
    print(MaxDiffValue.get_max_diff_value(my_arr))