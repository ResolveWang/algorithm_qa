"""
问题描述: 度度熊最近对全排列特别感兴趣,对于1到n的一个排列,度度熊发现可以在中间根据大小关
系插入合适的大于和小于符号(即 '>' 和 '<' )使其成为一个合法的不等式数列。但是现在度度熊
手中只有k个小于符号即('<'')和n-k-1个大于符号(即'>'),度度熊想知道对于1至n任意的排列中
有多少个排列可以使用这些符号使其为合法的不等式数列。

输入描述:
输入包括一行,包含两个整数n和k(k < n ≤ 1000)
输出描述:
输出满足条件的排列数,答案对2017取模。

示例1
输入
5 2
输出
66
"""
import sys


def solve(n, k):
    dp = [[0] * (k + 1) for i in range(n + 1)]
    for i in range(1, n - k + 1):
        dp[i][0] = 1
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j - 1] * (i - j) + dp[i - 1][j] * (j + 1)) % 2017
    print(dp[n][k])


if __name__ == '__main__':
    n, k = list(map(int, sys.stdin.readline().strip().split()))
