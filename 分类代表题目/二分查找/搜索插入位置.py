"""
问题描述: 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，
返回它将会被按顺序插入的位置。

例子: [1,3,5,6], 5 => 2     [1,3,5,6], 2 => 1    [1,3,5,6], 7 => 4
"""


class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) >> 1
            if nums[mid] == target:
                return mid
            elif mid == 0:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    return 0
            elif mid == len(nums) - 1:
                if nums[mid] > target:
                    return mid
                else:
                    return mid + 1
            elif mid - 1 >= 0 and nums[mid - 1] < target < nums[mid]:
                return mid
            elif mid - 1 >= 0 and nums[mid - 1] == target:
                return mid - 1
            elif mid + 1 < len(nums) and nums[mid] < target < nums[mid + 1]:
                return mid + 1
            elif mid + 1 == len(nums) - 1 and nums[mid+1] == target:
                return mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        if start > end:
            return start


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5], 5))