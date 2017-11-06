"""
问题描述：给定数组arr,arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种
面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。

补充题目：给定数组arr，arr中所有的值都为正数。每个值仅代表一张钱的面值，再给定一个整
数aim代表要找的钱数，求组成aim的最少货币数。
"""

import sys


class CoinsCounter:
    @classmethod
    def min_coins_count_1(cls, arr, aim):
        if not arr or aim < 0 or len(arr) == 0:
            return -1

        n = len(arr)
        max_val = sys.maxsize
        dp = [[0 for _ in range(aim + 1)] for _ in range(n)]
        for i in range(1, aim + 1):
            dp[0][i] = max_val
            if arr[0] <= i and dp[0][i - arr[0]] != max_val:
                dp[0][i] = dp[0][i - arr[0]] + 1

        for i in range(1, n):
            for j in range(1, aim + 1):
                left = max_val
                if arr[i] <= j and dp[i][j - arr[i]] != max_val:
                    left = dp[i][j - arr[i]] + 1
                dp[i][j] = min([left, dp[i - 1][j]])

        return dp[n - 1][aim] if dp[n - 1][aim] != max_val else -1

    @classmethod
    def min_coins_count_2(cls, arr, aim):
        if not arr or aim < 0 or len(arr) == 0:
            return -1

        n = len(arr)
        max_val = sys.maxsize
        dp = [0 for _ in range(aim + 1)]
        for i in range(1, aim + 1):
            dp[i] = max_val
            if arr[0] <= i and dp[i - arr[0]] != max_val:
                dp[i] = dp[i - arr[0]] + 1

        for i in range(1, n):
            for j in range(1, aim + 1):
                left = max_val
                if arr[i] <= j and dp[j - arr[i]] != max_val:
                    left = dp[j - arr[i]] + 1
                dp[j] = min([left, dp[j]])

        return dp[aim] if dp[aim] != max_val else -1

    @classmethod
    def min_coins_count_3(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return -1

        n = len(arr)
        max_val = sys.maxsize
        dp = [[0 for _ in range(aim + 1)] for _ in range(n)]

        for i in range(1, aim + 1):
            dp[0][i] = max_val
            if arr[0] == i:
                dp[0][i] = 1

        for i in range(1, n):
            for j in range(1, aim + 1):
                left = max_val
                if arr[i] <= j and dp[i][j - arr[i]] != max_val:
                    left = dp[i][j - arr[i]] + 1
                dp[i][j] = min([left, dp[i - 1][j]])

        return dp[n - 1][aim] if dp[n - 1][aim] != max_val else -1

    @classmethod
    def min_coins_count_4(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return -1

        n = len(arr)
        max_val = sys.maxsize
        dp = [0 for _ in range(aim + 1)]

        for i in range(1, aim + 1):
            dp[i] = max_val
            if i <= len(arr) - 1:
                if arr[i] == i:
                    dp[i] = 1

        for i in range(1, n):
            for j in range(1, aim + 1):
                left = max_val
                if arr[i] <= j and dp[j - arr[i]] != max_val:
                    left = dp[j - arr[i]] + 1
                dp[j] = min([left, dp[j]])

        return dp[aim] if dp[aim] != max_val else -1


if __name__ == '__main__':
    print(CoinsCounter.min_coins_count_1([100, 20, 5, 10, 2, 50, 1], 17019))
    print(CoinsCounter.min_coins_count_2([100, 20, 5, 10, 2, 50, 1], 17019))

    print(CoinsCounter.min_coins_count_3([10, 100, 2, 5, 5, 5, 10, 1, 1, 1, 2, 100], 223))
    print(CoinsCounter.min_coins_count_4([10, 100, 2, 5, 5, 5, 10, 1, 1, 1, 2, 100], 223))
