"""
问题:
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为O(n)，空间复杂度为O(1)。

示例:
[1,1,1,3,3,2,2,2] ＝> [1,2]
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b, ca, cb = 0, 0, 0, 0

        for i in nums:
            if i == a:
                ca += 1
            elif i == b:
                cb += 1
            elif ca == 0:
                a = i
                ca += 1
            elif cb == 0:
                b = i
                cb = 1
            else:
                ca -= 1
                cb -= 1

        ca = 0
        cb = 0
        for i in nums:
            if i == a:
                ca += 1
            if i == b:
                cb += 1
        rs = []
        if ca > len(nums) / 3:
            rs.append(a)
        if cb > len(nums) / 3 and a != b:
            rs.append(b)
        return rs