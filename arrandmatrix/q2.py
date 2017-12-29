"""
问题描述:给定一个矩阵,大小是N*N,把这个矩阵调整成顺时针转动90度后的形式。

例如:
１　２　３　４
５　６　７　８
9  10 11 12
13 14 15 16

顺时针转动90度,为:
13  9  5  1
14  10 6  2
15  11 7  3
16  12 8  4
"""


class MatrixRoater:
    @classmethod
    def roate_matrix_by_circle(cls, matrix, start_r, start_c, end_r, end_c):
        i = 0

        while i < end_c - start_c:
            tmp_value = matrix[start_r][start_c+i]
            matrix[start_r][start_c+i] = matrix[end_r-i][start_c]
            matrix[end_r-i][start_c] = matrix[end_r][end_c-i]
            matrix[end_r][end_c-i] = matrix[start_r+i][end_c]
            matrix[start_r+i][end_c] = tmp_value
            i += 1

    @classmethod
    def roate_maxtrix(cls, matrix):
        start_r = 0
        start_c = 0
        end_r = len(matrix) - 1
        end_c = len(matrix[0]) - 1

        while start_r <= end_r:
            cls.roate_matrix_by_circle(matrix, start_r, start_c, end_r, end_c)
            start_r += 1
            start_c += 1
            end_c -= 1
            end_r -= 1

        return matrix


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(MatrixRoater.roate_maxtrix(arr))