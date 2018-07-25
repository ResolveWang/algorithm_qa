"""
问题描述:
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [1] * len(nums)
        index = 1
        while index < len(nums):
            j = 0
            while j < index:
                if nums[j] < nums[index]:
                    if dp[j] + 1 > dp[index]:
                        dp[index] = dp[j] + 1
                j += 1
            index += 1

        return max(dp)