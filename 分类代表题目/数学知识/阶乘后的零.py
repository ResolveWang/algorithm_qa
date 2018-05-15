"""
给定一个整数 n，返回 n! 结果尾数中零的数量。
示例:
5! => 1

思路:
０的个数取决于5的个数，问题可以转化为求5的因素，每个数可能有０,1,2...x个
５的因数
"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        cur = 5
        while n / cur >= 1:
            i += 1
            cur = 5 * cur

        res = 0
        start = 1
        while start <= i:
            res += int(n / 5 ** start)
            start += 1
        return res