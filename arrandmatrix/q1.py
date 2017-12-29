"""
问题描述:给定一个矩阵matrix,请按照转圈的方式打印它。

例如：
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

打印结果为:
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""


class MatrixPrinter:
    @classmethod
    def print_matrix(cls, matrix):
        start_r = 0
        start_c = 0
        end_r = len(matrix) - 1
        end_c = len(matrix[0]) - 1
        while start_r <= end_r and start_c <= end_c:
            cls.print_cycle_of_matrix(matrix, start_r, start_c, end_r, end_c)
            start_c += 1
            start_r += 1
            end_r -= 1
            end_c -= 1

    @classmethod
    def print_cycle_of_matrix(cls, matrix, start_r, start_c, end_r, end_c):
        if start_r == end_r:
            while start_c <= end_c:
                print(matrix[start_r][start_c], end=' ')
                start_c += 1
        elif start_c == end_c:
            while start_r <= end_r:
                print(matrix[start_r][start_c], end=' ')
                start_r += 1
        else:
            tmp_c = start_c
            tmp_r = start_r
            while tmp_c != end_c:
                print(matrix[tmp_r][tmp_c], end=' ')
                tmp_c += 1
            while tmp_r != end_r:
                print(matrix[tmp_r][tmp_c], end=' ')
                tmp_r += 1
            while tmp_c != start_c:
                print(matrix[tmp_r][tmp_c], end=' ')
                tmp_c -= 1
            while tmp_r != start_r:
                print(matrix[tmp_r][tmp_c], end=' ')
                tmp_r -= 1


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    MatrixPrinter.print_matrix(arr)