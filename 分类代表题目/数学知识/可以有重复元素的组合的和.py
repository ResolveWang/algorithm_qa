"""
问题: 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以
使数字和为 target 的组合。candidates 中的数字可以无限制重复被选取。

举例:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return list()
        # 这里预先对所有元素进行排序，则可以避免收集重复的路径
        candidates.sort()
        res = list()
        self.process(target, [], candidates, 0, res)
        return res

    def process(self, target, path, candidates, index, res):
        """深度优先搜索"""
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(index, len(candidates)):
            self.process(target - candidates[i], path + [candidates[i]], candidates, i, res)