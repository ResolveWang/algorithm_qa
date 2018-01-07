"""
问题描述:给定一个N*N的矩阵matrix,在这个矩阵中,只有0和1两种值,返回边框全是1
的最大正方形的边长长度.

例如:
0  1  1  1  1
0  1  0  0  1
0  1  0  0  1
0  1  1  1  1
0  1  0  1  1

其中,边框全是1的最大正方形的大小是4*4,所以返回4.
"""


class MaxSizeGetter:
    @classmethod
    def get_matrix_size(cls, matrix):
        if not matrix:
            return 0

        n = len(matrix)

        right, down = cls.get_board_map(matrix)
        max_board_length = 0

        for row in range(n):
            for col in range(n):
                if row > col:
                    cur_length = n - row
                else:
                    cur_length = n - col
                for l in range(cur_length, 0, -1):
                    if down[row][col] >= l and right[row][col] >= l and down[row][col+l-1] >= l \
                            and right[row+l-1][col] >= l:
                        max_board_length = max([l, max_board_length])
                        break

        return max_board_length

    @classmethod
    def get_board_map(cls, matrix):
        row_length = len(matrix)
        col_length = len(matrix[0])
        right = [[0 for _ in range(col_length)] for _ in range(row_length)]
        down = [[0 for _ in range(col_length)] for _ in range(row_length)]
        right[row_length-1][col_length-1] = matrix[row_length-1][col_length-1]
        down[row_length-1][col_length-1] = matrix[row_length-1][col_length-1]

        for i in range(row_length-2, -1, -1):
            right[i][col_length-1] = matrix[i][col_length-1]
            if matrix[i][col_length-1] == 0:
                down[i][col_length-1] = 0
            else:
                down[i][col_length-1] = 1 + down[i+1][col_length-1]

        for i in range(col_length-2, -1, -1):
            down[row_length-1][i] = matrix[row_length-1][i]
            if matrix[row_length-1][i] == 0:
                right[row_length-1][i] = 0
            else:
                right[row_length-1][i] = 1 + right[row_length-1][i+1]

        for row in range(row_length-2, -1, -1):
            for col in range(col_length-2, -1, -1):
                if matrix[row][col] == 0:
                    down[row][col] = 0
                    right[row][col] = 0
                else:
                    down[row][col] = 1 + down[row+1][col]
                    right[row][col] = 1 + right[row][col+1]

        return right, down


if __name__ == '__main__':
    my_matrix = [
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1]
    ]

    print(MaxSizeGetter.get_matrix_size(my_matrix))