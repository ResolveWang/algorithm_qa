"""
问题: 给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

思路:
我们从最后一个位置开始遍历数组，每当我们遍历到一个可以达到末尾位置的位置时，就更新末尾位置为当前位置，最后根
据最新的末尾位置是否为0即可
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        index = len(nums) - 1
        last_good_pos = index - 1
        while index >= 0:
            if nums[index] + index >= last_good_pos:
                last_good_pos = index
            index -= 1

        return last_good_pos == 0