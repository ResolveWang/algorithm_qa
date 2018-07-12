"""
问题描述: 易老师购买了一盒饼干，盒子中一共有k块饼干，但是数字k有些数位变得模糊了，看不清楚数字
具体是多少了。易老师需要你帮忙把这k块饼干平分给n个小朋友，易老师保证这盒饼干能平分给n个小朋友。
现在你需要计算出k有多少种可能的数值

输入描述:
输入包括两行：
第一行为盒子上的数值k，模糊的数位用X表示，长度小于18(可能有多个模糊的数位)
第二行为小朋友的人数n
输出描述:
输出k可能的数值种数，保证至少为1
示例1
输入
9999999999999X 3
输出
4

状态转移方程: dp[i][(10*j+w)%n] += dp[i-1][j]
"""


import sys


class Solution:
    def get_possible_rs(self, args, children):
        dp = [[0]*children for _ in range(len(args)+1)]
        dp[0][0] = 1
        for i in range(1, len(args)+1):
            for j in range(children):
                for w in range(10):
                    if args[i-1] == 'X' or int(args[i-1]) == w:
                        dp[i][(10*j+w) % children] += dp[i-1][j]
        print(dp[len(args)][0])


if __name__ == '__main__':
    k = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    s = Solution()
    s.get_possible_rs(k, n)