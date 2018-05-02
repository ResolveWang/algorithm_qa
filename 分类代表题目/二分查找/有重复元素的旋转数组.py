"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例:
nums = [2,5,6,0,0,1,2], target = 0 => true
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        rotated_point = self.get_rotated_point(nums, 0, len(nums) - 1)
        if rotated_point == 0:
            return self.process(nums, 0, len(nums) - 1, target)
        else:
            if nums[-1] == target:
                return True
            elif nums[-1] > target:
                return self.process(nums, rotated_point, len(nums) - 1, target)
            else:
                return self.process(nums, 0, rotated_point - 1, target)

    def get_rotated_point(self, nums, start, end):
        if start == end:
            return start
        mid = (start + end) >> 1
        if nums[mid] > nums[end]:
            start = mid + 1
        elif nums[mid] == nums[end]:
            end -= 1
        elif nums[mid] < nums[end]:
            if nums[mid - 1] > nums[mid]:
                return mid
            else:
                if mid - 1 >= 0:
                    end = mid - 1
                else:
                    return start

        return self.get_rotated_point(nums, start, end)

    def process(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return True
            else:
                return False

        mid = (start + end) >> 1
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            start += 1
        else:
            end -= 1

        return self.process(nums, start, end, target)


if __name__ == '__main__':
    arr = [2, 2, 2, 0, 2, 2]
    s = Solution()
    print(s.get_rotated_point(arr, 0, len(arr)-1))
    print(s.search([2, 2, 2, 0, 2, 2], 0))