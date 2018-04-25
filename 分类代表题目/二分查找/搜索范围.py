"""
问题描述: 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。如果数组中不存在目标值，返回 [-1, -1]。

例子:
nums = [5,7,7,8,8,10], target = 8  => [3,4]
nums = [5,7,7,8,8,10], target = 6  => [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        left_index = self.binary_search_left(nums, 0, len(nums) - 1, target)
        right_index = self.binary_search_right(nums, 0, len(nums) - 1, target)
        return [left_index, right_index]

    def binary_search_left(self, nums, start, end, target):
        if start > end:
            return -1

        if start == end and nums[start] == target:
            return start
        elif start == end:
            return -1

        mid = (start + end) >> 1
        if (mid == 0 and nums[mid] == target) or (nums[mid] == target and nums[mid - 1] != target):
            return mid
        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

        return self.binary_search_left(nums, start, end, target)

    def binary_search_right(self, nums, start, end, target):
        if start > end:
            return -1

        if start == end and nums[start] == target:
            return start
        elif start == end:
            return -1
        mid = (start + end) >> 1

        if (mid == len(nums) - 1 and nums[mid] == target) or (nums[mid] == target and nums[mid + 1] != target):
            return mid

        if nums[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
        return self.binary_search_right(nums, start, end, target)