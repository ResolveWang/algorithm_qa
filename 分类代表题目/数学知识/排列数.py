"""
问题: 给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        if not nums:
            return list()
        res = list()
        self.process(nums, [], res)
        return res

    def process(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return

        for i in range(len(nums)):
            # 注意这里是如何隐式"pop"掉某个元素的
            new_nums = nums[:i] + nums[i + 1:]
            # 这里可以直接对列表进行相加，返回一个新列表
            self.process(new_nums, path + [nums[i]], res)