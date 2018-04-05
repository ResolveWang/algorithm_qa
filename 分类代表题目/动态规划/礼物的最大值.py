"""
在一个m*n的棋盘的每一1格都放有一个礼物，每个礼物都有一定的价值（价值都大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋
盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

比如：
1  10 3  8
12 2  9  6
5  7  4  11
3  7  16 5

最大的路线为(1,12,5,7,7,16,5),那么我们能拿到最大价值为53的礼物
"""


class GiftMaxValue:
    def get_max_value(self, matrix):
        if not matrix:
            return 0

        if len(matrix[0]) == 1:
            max_sum = 0
            for cols in matrix:
                max_sum += cols[0]
            return max_sum

        if len(matrix) == 1:
            return sum(matrix[0])

        row_length = len(matrix)
        col_length = len(matrix[0])
        dp = [[0 for _ in range(col_length)] for _ in range(row_length)]

        dp[0][0] = matrix[0][0]
        for i in range(1, col_length):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]
        for i in range(1, row_length):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]

        for row in range(1, row_length):
            for col in range(1, col_length):
                dp[row][col] = max([dp[row - 1][col], dp[row][col - 1]]) + matrix[row][col]

        return dp[row_length - 1][col_length - 1]


if __name__ == '__main__':
    mat = [
        [1, 10, 3, 8],
        [12, 2, 9, 6],
        [5, 7, 4, 11],
        [3, 7, 16, 5]
    ]

    print(GiftMaxValue().get_max_value(mat))
