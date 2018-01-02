"""
给定一个矩阵maxtrix，按照“之”字形的方式打印这个矩阵，例如:
１　２　３　４
５　６　７　８
9  10 11  12

“之”字形打印的结果为:1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12
要求:
额外空间复杂度为O(1)。
"""


class MaxtrixPrinter:
    @classmethod
    def zig_maxtrix_print(cls, matrix):
        row_length = len(matrix)
        col_length = len(matrix[0])
        if row_length == 1:
            for i in matrix[0]:
                print(i, end=' ')

        if col_length == 1:
            for i in matrix:
                print(matrix[i][0], end=' ')

        print(matrix[0][0], end=' ')

        up_to_down = True
        tr = 0
        tc = 0
        dr = 0
        dc = 0

        while tr < row_length - 1 and dc < col_length - 1:
            if tc < col_length - 1:
                tc += 1
            else:
                tr += 1

            if dr < row_length - 1:
                dr += 1
            else:
                dc += 1

            tmp_tc = tc
            tmp_tr = tr
            tmp_dr = dr
            tmp_dc = dc

            if up_to_down:
                while tmp_tr <= tmp_dr and tmp_dc <= tmp_tc:
                    print(matrix[tmp_tr][tmp_tc], end=' ')
                    tmp_tr += 1
                    tmp_tc -= 1
            else:
                while tmp_tr <= tmp_dr and tmp_dc <= tmp_tc:
                    print(matrix[tmp_dr][tmp_dc], end=' ')
                    tmp_dr -= 1
                    tmp_dc += 1

            up_to_down = not up_to_down


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    MaxtrixPrinter.zig_maxtrix_print(arr)


