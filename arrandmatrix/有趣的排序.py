"""
问题描述: 度度熊有一个N个数的数组，他想将数组从小到大 排好序，但是萌萌的度度熊只会
下面这个操作： 任取数组中的一个数然后将它放置在数组的最后一个位置。 问最少操作多少
次可以使得数组从小到大有序？

输入描述:
首先输入一个正整数N，接下来的一行输入N个整数。(N <= 50, 每个数的绝对值小于等于1000

输出描述:
输出一个整数表示最少的操作次数。

输入例子1:
4
19 7 8 25

输出例子1:
2
"""


import sys
import copy


class Solution:
    def get_least_opers(self, arr):
        if len(arr) <= 1:
            print(0)
            return

        cloned_arr = copy.copy(arr)
        cloned_arr.sort()
        pos = self.get_first_unorder_val(arr)
        if pos == -1:
            print(0)
            return
        index = 0
        while index < len(cloned_arr):
            if cloned_arr[index] == arr[pos]:
                print(len(cloned_arr)-index)
                return
            index += 1

    def get_first_unorder_val(self, arr):
        cloned_arr = copy.copy(arr)
        cloned_arr.sort()
        smaller_pos = -1
        index = 0

        while index < len(cloned_arr):
            val = cloned_arr[index]
            for pos, value in enumerate(arr):
                if value == val:
                    if pos >= smaller_pos:
                        smaller_pos = pos
                    else:
                        return pos
            index += 1

        return -1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    args = list(map(int, sys.stdin.readline().split()))
    s = Solution()
    s.get_least_opers(args)
