"""
问题描述:给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。
如何删除才能使得回文串最长呢？

输入
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.

输出
对于每组数据，输出一个整数，代表最少需要删除的字符个数。

示例
abcda => 2
google => 2
"""


import sys


def get_max_len(strs):
    reversed_strs = strs[::-1]
    length = len(strs)
    dp = [[0] * (length+1) for _ in range(length+1)]

    for i in range(length):
        for j in range(length):
            if strs[i] == reversed_strs[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(length - dp[length][length])


if __name__ == '__main__':
    while True:
        s = sys.stdin.readline().strip()
        if not s:
            break

        get_max_len(s)