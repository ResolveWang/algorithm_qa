"""
问题描述:输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

思路:
关于数组的题目，要是出现"一对"这个词，一般想着使用双指针或者归并排序的过程
"""


# -*- coding:utf-8 -*-
class Solution:
    def find_numbers_with_sum(self, array, tsum):
        if not array or len(array) < 2:
            return list()
        if array[0] + array[1] > tsum:
            return list()
        if array[-1] + array[-2] < tsum:
            return list()

        left = 0
        right = len(array) - 1
        while array[left] + array[right] != tsum and left < right:
            if array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1

        if left == right:
            return list()

        return array[left], array[right]


if __name__ == '__main__':
    print(Solution().find_numbers_with_sum([1, 2, 3, 4, 5], 7))