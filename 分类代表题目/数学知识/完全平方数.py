"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。

示例:
12 => 3
解释: 12 = 4 + 4 + 4.
"""


class Solution:
    # 小技巧: 可以使用类变量记住状态
    dp = [0]

    def numSquares(self, n):
        cur_length = len(self.dp)
        if cur_length > n:
            return self.dp[n]

        for cur in range(cur_length, n+1):
            i = 1
            val = float('inf')
            while cur - i ** 2 >= 0:
                val = min([val, self.dp[cur - i ** 2] + 1])
                i += 1
            self.dp.append(val)

        return self.dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(13))