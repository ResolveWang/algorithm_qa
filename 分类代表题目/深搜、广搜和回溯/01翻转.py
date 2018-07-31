"""
问题描述:牛牛正在挑战一款名为01翻转的游戏。游戏初始有A个0,B个1，牛牛的目标就是把所有的值都变为1，
每次操作牛牛可以任意选择恰好K个数字，并将这K个数字的值进行翻转(0变为1，1变为0)。牛牛如果使用最少
的操作次数完成这个游戏就可以获得奖品，牛牛想知道最少的操作次数是多少？

例如:A = 4 B = 0 K = 3
0000 -> 1110 -> 1001 -> 0100 -> 1111
需要的最少操作次数为4

输入描述:
输入为一行： 一共三个整数A(0 ≤ A ≤ 100,000),B(0 ≤ B ≤ 100,000),K(1 ≤ K ≤100,000).
以空格分隔
输出描述:
输出一个整数，表示最少需要的操作次数。如果不能完成，则输出-1
示例1
输入
4 0 3
输出
4
"""


import sys


class Solution:
    def get_reversed_time(self, a, b, k):
        if a == 0:
            print(0)
            return

        if k == a:
            print(1)
            return

        if k > a + b:
            print(-1)
            return

        visited = {a}
        queue = list()
        queue.append((a, b, 0))
        while queue:
            cur = queue.pop(0)
            if cur[0] == 0:
                print(cur[2])
                return

            for i in range(1, min([cur[0], k])+1):
                if cur[1] < k - i:
                    continue

                new_a = cur[0] - i + (k - i)
                if new_a == 0:
                    print(cur[2]+1)
                    return
                if new_a not in visited:
                    visited.add(new_a)
                    queue.append((new_a, cur[0]+cur[1]-new_a, cur[2]+1))
        print(-1)


if __name__ == '__main__':
    s = Solution()
    a, b, k = map(int, sys.stdin.readline().split())
    s.get_reversed_time(a, b, k)