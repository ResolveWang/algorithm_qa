"""
问题: 统计所有小于非负数整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit_arr = [0 for i in range(n)]
        count = 0
        index = 2
        while index < n:
            if bit_arr[index] == 0:
                count += 1
                j = index
                while index*j < n:
                    bit_arr[index*j] = 1
                    j += 1
            index += 1
        return count