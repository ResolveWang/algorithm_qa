"""
问题描述: 峰值元素是指其值大于左右相邻值的元素。给定一个输入数组 nums，
其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。数组可能包含多
个峰值，在这种情况下，返回任何一个峰值所在位置即可。你可以假设 nums[-1] = nums[n] = -∞。

示例:
nums = [1,2,3,1] => 2
3 是峰值元素，函数应该返回其索引 2。

思路:
由于最左和最右是最低点，因此中间一定存在局部最大值．二分查找的标准是每次都
往比mid更大的那边寻找，因为那边总会降低到无穷小
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        return self.process(nums, 0, len(nums) - 1)

    def process(self, nums, start, end):
        if start == end:
            return start

        mid = (start + end) >> 1

        if mid == 0:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            start = mid + 1
        elif nums[mid] < nums[mid - 1]:
            end = mid - 1

        return self.process(nums, start, end)
