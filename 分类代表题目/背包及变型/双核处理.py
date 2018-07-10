"""
问题描述: 一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，
假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。n个任务可以按照任意顺序放入
CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，求这个最小的时间。

输入: 输入包括两行： 第一行为整数n(1 ≤ n ≤ 50) 第二行为n个整数length[i](1024 ≤ length[i]
 ≤ 4194304)，表示每个任务的长度为length[i]kb，每个数均为1024的倍数。

输出描述: 输出一个整数，表示最少需要处理的时间

示例1
输入
5 3072 3072 7168 3072 1024

输出
9216
"""
import sys


class Solution:
    def get_least_work_time(self, arr):
        if len(arr) <= 2:
            print(max(arr))
            return

        total = sum(arr) // 2 + 1
        dp = [[0 for _ in range(total)] for _ in range(len(arr)+1)]
        for i in range(1, len(arr)+1):
            for j in range(1, total):
                if j >= arr[i-1]:
                    dp[i][j] = max([dp[i-1][j], dp[i-1][j-arr[i-1]] + arr[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]

        print(max([dp[len(arr)][total-1], sum(arr)-dp[len(arr)][total-1]]))


if __name__ == '__main__':
    s = Solution()
    n = int(sys.stdin.readline())
    args = list(map(int, sys.stdin.readline().split()))
    s.get_least_work_time(args)