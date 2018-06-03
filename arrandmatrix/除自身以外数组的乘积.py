"""
问题: 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
[1,2,3,4] => [24,12,8,6]

要求:
请不要使用除法，且在 O(n) 时间复杂度内完成此题。
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1 for _ in nums]
        tmp = 1

        p = 1
        for i in range(len(nums)):
            ret[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= p
            p *= nums[i]

        return ret
