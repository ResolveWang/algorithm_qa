"""
给定一个长度为N(N>1)的整型数组arr,可以划分为左右两个部分,左部分为arr[0..K],
右部分为arr[K+1..N-1],K可以取值的范围是[0,N-2].求这么多划分方案中,左部分中
的最大值减去右部分的最大值的绝对值中,最大是多少？
"""
import sys


class LeftRightMaxDiff:
    @classmethod
    def get_left_right_max_diff(cls, arr):
        if not arr or len(arr) < 2:
            return

        max_value = -sys.maxsize
        for index in range(len(arr)):
            max_value = max([max_value, arr[index]])

        return max(max_value-arr[0], max_value-arr[-1])


if __name__ == '__main__':
    my_arr = [2, 7, 3, 1, 1]
    print(LeftRightMaxDiff.get_left_right_max_diff(my_arr))