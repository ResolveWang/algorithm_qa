"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
数组中不存在重复的元素。

示例:
nums = [4,5,6,7,0,1,2], target = 0 => 4
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        end = len(nums) - 1
        rotated_point = self.get_rotated_point(nums, 0, end)
        if rotated_point == 0:
            return self.binary_search(nums, 0, end, target)
        else:
            if target == nums[0]:
                return 0
            elif target > nums[0]:
                return self.binary_search(nums, 0, rotated_point - 1, target)
            else:
                return self.binary_search(nums, rotated_point, end, target)

    def get_rotated_point(self, nums, start, end):
        if start == end:
            return start

        mid = (start + end) >> 1
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] < nums[end]:
            if nums[mid] < nums[mid - 1]:
                return mid
            else:
                end = mid - 1

        return self.get_rotated_point(nums, start, end)

    def binary_search(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1

        mid = (start + end) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end -= 1
        else:
            start += 1

        return self.binary_search(nums, start, end, target)

