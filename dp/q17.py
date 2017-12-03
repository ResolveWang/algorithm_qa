"""
问题描述：N皇后问题是指在N*N的棋盘上要摆N个皇后，要求任何两个皇后不同行、不同列，也不在
同一条斜线上，给定一个整数n,返回n皇后的摆法有多少种。

举例：
n=1，返回1
n=2或者3，2皇后和3皇后无论怎么摆都不行，返回0
n=8，返回92
"""


class NQueenProblem:
    @classmethod
    def solve_by_recursive(cls, n):
        if n < 1:
            return 0
        record = [0 for _ in range(n)]
        return cls.recursive_detail(0, record, n)

    @classmethod
    def recursive_detail(cls, row, record, n):
        if row == n:
            return 1
        res = 0
        for col in range(n):
            if cls.is_valid(row, col, record):
                record[row] = col
                res += cls.recursive_detail(row+1, record, n)

        return res

    @classmethod
    def is_valid(cls, row, col, record):
        i = 0
        while i < row:
            if record[i] == col or abs(i-row) == abs(record[i]-col):
                return False
            i += 1

        return True


if __name__ == '__main__':
    print(NQueenProblem.solve_by_recursive(8))