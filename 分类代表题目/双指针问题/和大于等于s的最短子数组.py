"""
问题: 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的子数组。
如果不存在符合条件的子数组，返回 0。

示例:
输入: [2,3,1,2,4,3], s = 7
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的子数组。

方法:
子数组问题三板斧
1.以xxx位置开头的情况
2.以xxx位置结尾的情况
3.双指针

本题使用双指针即可解决，时间复杂度为O(n)
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        min_length = float('+inf')
        left = 0
        right = 0
        cur = 0
        while right < len(nums):
            cur += nums[right]
            while cur >= s:
                min_length = min([min_length, right - left + 1])
                cur -= nums[left]
                if left == right:
                    right += 1
                    left += 1
                else:
                    left += 1
            else:
                right += 1

        return min_length if min_length != float('+inf') else 0