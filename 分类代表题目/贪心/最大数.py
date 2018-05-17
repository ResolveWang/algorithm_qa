"""
问题描述: 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例:
[10,2] => 210

[3,30,34,5,9] => 9534330
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''

        num_strs = list(map(str, nums))

        res = self.process(num_strs, '')
        if res[0] == '0':
            return '0'
        return res

    def process(self, strs, cur):
        if not strs:
            return cur

        max_index = -1
        for index, value in enumerate(strs):
            if max_index == -1:
                max_index = index
                continue

            if int(value+strs[max_index]) > int(strs[max_index]+value):
                max_index = index

        return self.process(strs[:max_index] + strs[max_index + 1:], cur + strs[max_index])