"""
问题描述:今年的世界杯要开始啦，牛牛作为一个球迷，当然不会放过去开幕式现场的机会。
但是牛牛一个人去又觉得太过寂寞，便想叫上了他的n个小伙伴陪他一起去莫斯科(一共n+1人)。
当牛牛开始订开幕式的门票时，发现门票有m种套餐，每种套餐需要花费x元，包含y张门票，
每张门票也可以单独购买，此时这张门票的价格为k元。请问牛牛要怎样选择购买门票，
使得他花费的钱最少。(每种套餐可以购买次数没有限制)。

示例
输入:
2 2 5
6 2
13 3

输出:
11
"""
import sys


class WorldCup:
    def get_all_cost(self):
        n, m, k = list((map(int, sys.stdin.readline().strip().split())))
        n += 1
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = i*k

        while m > 0:
            x, y = list((map(int, sys.stdin.readline().strip().split())))
            for i in range(1, n+1):
                if i - y >= 0:
                    dp[i] = min([dp[i], dp[i-y]+x])
                else:
                    dp[i] = min([dp[i], x])
            m -= 1
        print(dp[n])


if __name__ == '__main__':
    word_cup = WorldCup()
    word_cup.get_all_cost()