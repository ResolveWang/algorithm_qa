"""
问题描述: 小易来到了一条石板路前，每块石板上从1挨着编号为：1、2、3.
这条石板路要根据特殊的规则才能前进：对于小易当前所在的编号为K的 石板,
小易单次只能往前跳K的一个约数(不含1和K)步，即跳到K+X(X为K的一个非1和
本身的约数)的位置。 小易当前处在编号为N的石板，他想跳到编号恰好为M的石
板去，小易想知道最少需要跳跃几次可以到达。

例如：
N = 4，M = 24：
4->6->8->12->18->24
于是小易最少需要跳跃5次，就可以从4号石板跳到24号石板
"""


import sys
import math


class Solution:
    def get_smallest_steps(self, m, n):
        path = [100 for _ in range(n+1)]
        path[m] = 0
        for i in range(m, n-1):
            if path[i] == 100:
                continue

            factors = self.get_factors(i)
            for factor in factors:
                tmp = factor + i
                if tmp <= n and path[tmp] > path[i] + 1:
                    path[tmp] = path[i] + 1
        print(path[n])

    def get_factors(self, m):
        rs = list()
        for i in range(2, int(math.sqrt(m))+1):
            if m % i == 0:
                rs.append(i)
                if int(m / i) != i:
                    rs.append(int(m/i))
        return rs


if __name__ == '__main__':
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    s = Solution()
    s.get_smallest_steps(a, b)