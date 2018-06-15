"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
找出只出现一次的那两个元素。

示例:
[1,2,1,3,2,5] ＝> [3,5]

要求:
时间复杂度为O(N)，空间复杂度为O(1).结果输出的顺序不需要有序
"""


class Solution:
    def singleNumber(self, nums):
        xor = 0
        a = 0
        b = 0
        for i in nums:
            xor ^= i

        mask = 1
        while xor & mask == 0:
            mask = mask << 1

        for i in nums:
            if i & mask:
                a ^= i
            else:
                b ^= i
        return [a, b]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 1, 3, 2, 5]
    print(s.singleNumber(arr))
