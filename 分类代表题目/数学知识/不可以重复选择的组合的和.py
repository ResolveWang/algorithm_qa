"""
问题: 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字
和为 target 的组合。candidates 中的每个数字在每个组合中只能使用一次。

示例:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return list()
        candidates.sort()
        res = list()
        seen = set()
        self.process(candidates, [], target, res, 0, seen)

        return res

    def process(self, nums, path, target, res, index, seen):
        if target == 0:
            if '#'.join(map(str, path)) not in seen:
                # 存放已经走过的路径，如果开始数组没排序，那么这里可以先排序
                # 也可以和本部分全排列的问题做法一样，直接除去nums中对应的值
                seen.add('#'.join(map(str, path)))
                res.append(path)
            return

        if target < 0:
            return

        if index < len(nums):
            self.process(nums, path, target, res, index + 1, seen)
            self.process(nums, path + [nums[index]], target - nums[index], res, index + 1, seen)

