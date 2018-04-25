"""
问题描述:

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。如果不存在
下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。必须原地修改，只允许使用额外常数
空间。

例子:
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""




class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if not nums or length < 2:
            return

        index = length - 1
        need_sort = True
        while index >= 1:
            if nums[index] <= nums[index - 1]:
                index -= 1
            else:
                tmp = index - 1
                while index < length and nums[tmp] <= nums[index]:
                    if (index + 1 < length and nums[tmp] >= nums[index + 1]) or index + 1 == length:
                        nums[tmp], nums[index] = nums[index], nums[tmp]
                        self.reverse(nums, tmp + 1, length - 1)
                        break
                    else:
                        index += 1
                need_sort = False
                break
        if need_sort:
            nums.sort()

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
            start += 1


