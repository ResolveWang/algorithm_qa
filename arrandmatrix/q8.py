"""
问题描述:先给出可整合数组的定义.如果一个数组在排序之后,每相邻两个数差的绝对值
都为１,则该数组为可整合数组.例如,[5, 3, 4, 6, 2]排序之后为[2, 3, 4, 5, 6],
符合每相邻两个数差的绝对值都为１,所以这个数组为可整合数组.
给定一个整型数组arr,请返回其中最大可整合子数组的长度.例如, [5, 5, 3, 2, 6, 4, 3]
的最大可整合子数组为[5, 3, 2, 6, 4],所以返回5.
"""
import sys


class IntegratedNumCounter:
    @classmethod
    def more_cost_method(cls, arr):
        if not arr:
            return 0

        length = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if cls.is_integrated(arr[i:j+1]):
                    length = max([len(arr[i:j+1]), length])

        return length

    @classmethod
    def is_integrated(cls, arr):
        sorted_arr = sorted(arr)
        pre = None
        for i in sorted_arr:
            if pre is not None:
                diff = i - pre
                if diff != 1:
                    return False
            pre = i

        return True

    @classmethod
    def less_cost_method(cls, arr):
        if not arr:
            return 0

        length = 0
        my_set = set()
        for i in range(len(arr)):
            max_value = -sys.maxsize
            min_value = sys.maxsize
            for j in range(i, len(arr)):
                if arr[j] in my_set:
                    break
                my_set.add(arr[j])
                max_value = max([max_value, arr[j]])
                min_value = min([min_value, arr[j]])

                if max_value - min_value == j - i:
                    length = max([length, j-i+1])
            my_set.clear()

        return length


if __name__ == '__main__':
    my_arr = [5, 5, 3, 2, 4, 6, 4]
    print(IntegratedNumCounter.more_cost_method(my_arr))
    print(IntegratedNumCounter.less_cost_method(my_arr))