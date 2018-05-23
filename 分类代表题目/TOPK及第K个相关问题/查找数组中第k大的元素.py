"""
问题: 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，
而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        cur = start
        left = start - 1
        right = end
        while cur < right:
            if nums[cur] < nums[end]:
                left += 1
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
            elif nums[cur] == nums[end]:
                cur += 1
            else:
                right -= 1
                nums[cur], nums[right] = nums[right], nums[cur]

        nums[end], nums[right] = nums[right], nums[end]
        if k <= left:
            return self.partition(nums, start, left, k)
        elif left < k <= right:
            return nums[right]
        else:
            return self.partition(nums, right + 1, end, k)


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    s = Solution()
    print(s.findKthLargest(arr, 2))