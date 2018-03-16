"""
问题描述:有一座大楼有0~N层，地面算作第0层,最高的一层为第N层。已知棋子从第0层掉落
肯定不会摔落，从第i层掉落可能会摔落，也可能不会摔破(1<=i<=N)。给定整数N作为楼层数，
再给定整数K作为棋子数，返回如果想找到棋子不会摔破的最高层数，即使在最差的情况下扔的
最少次数。一次只能扔一个棋子。

举例:
N=10, k=1
返回10。因为只有１棵棋子，所以不得不从第1层开始一直试到第10层，在最差的情况下，即第
10层是不会摔坏的最高层，最少也要扔10次。
Ｎ=3, k=2
返回2.先在2层扔1颗棋子，如果碎了，试第一层，如果没碎，试第3层
N=105, k=2
返回14。
第一个棋子先在14层扔，碎了则用仅存的一个棋子试1~13
若没碎，第一个棋子继续在27层扔，碎了则用仅存的一个棋子试15~26
若没碎，第一个棋子继续在39层扔，碎了则用仅存的一个棋子试28~38
若没碎，第一个棋子继续在50层扔，碎了则用仅存的一个棋子试40~49
若没碎，第一个棋子继续在60层扔，碎了则用仅存的一个棋子试51~59
若没碎，第一个棋子继续在69层扔，碎了则用仅存的一个棋子试61~68
若没碎，第一个棋子继续在77层扔，碎了则用仅存的一个棋子试70~76
若没碎，第一个棋子继续在84层扔，碎了则用仅存的一个棋子试78~83
若没碎，第一个棋子继续在90层扔，碎了则用仅存的一个棋子试85~89
若没碎，第一个棋子继续在95层扔，碎了则用仅存的一个棋子试91~94
若没碎，第一个棋子继续在99层扔，碎了则用仅存的一个棋子试96~98
若没碎，第一个棋子继续在102层扔，碎了则用仅存的一个棋子试100、101
若没碎，第一个棋子继续在104层扔，碎了则用仅存的一个棋子试103
若没碎，第一个棋子继续在105层扔，若到这一步还没碎，那么105便是结果
"""
import sys


class PieceDropProblem:
    @classmethod
    def solution_by_recursive(cls, n, k):
        if n < 1 or k < 1:
            return 0

        return cls.recursive_solution_detail(n, k)

    @classmethod
    def recursive_solution_detail(cls, n, k):
        if n == 0:
            return 0

        if k == 1:
            return n

        res = sys.maxsize
        for i in range(1, n+1):
            res2 = max(cls.recursive_solution_detail(n-i, k), cls.recursive_solution_detail(i-1, k-1))
            if res > res2:
                res = res2

        return res + 1

    @classmethod
    def solution_by_dp(cls, n, k):
        if n < 1 or k < 1:
            return 0
        if k == 1:
            return n

        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][1] = i

        for row in range(1, n+1):
            for col in range(2, k+1):
                min_value = sys.maxsize
                for i in range(1, row+1):
                    min_value = min([min_value, max(dp[row-i][col], dp[i-1][col-1])])

                dp[row][col] = min_value + 1

        return dp[n][k]


if __name__ == '__main__':
    print(PieceDropProblem.solution_by_recursive(21, 2))
    print(PieceDropProblem.solution_by_dp(21, 2))