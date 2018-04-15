"""
问题: 将一个 M*N 的矩阵按照对角线依次打印出来,比如
1, 2, 3, 4
2, 3, 4, 5
4, 5, 6, 7

打印结果为
1
2 2
3 3 4
4 4 5
5 6
7
"""


def print_maxtrix(matrix):
    if not matrix:
        return

    row_length = len(matrix)
    col_length = len(matrix[0])

    limit_row = 0
    limit_col = 0

    # 从第一行最左边开始打印
    while limit_row < row_length and limit_col < col_length:
        cur_row = 0
        cur_col = limit_col
        while cur_row <= limit_row and cur_col >= 0:
            print(matrix[cur_row][cur_col], end=' ')
            cur_row += 1
            cur_col -= 1
        print()
        limit_col += 1
        limit_row += 1

    # 如果列数大于行数，则单独把多余的列打印出来
    if col_length > row_length:
        limit_bottom_col = 1
        while limit_col < col_length:
            cur_row = 0
            cur_col = limit_col
            while cur_col >= limit_bottom_col:
                print(matrix[cur_row][cur_col], end=' ')
                cur_row += 1
                cur_col -= 1
            print()
            limit_bottom_col += 1
            limit_col += 1
    # 如果行数大于列数，则单独把多余的行打印出来
    elif col_length < row_length:
        limit_up_row = 1
        while limit_row < row_length:
            cur_row = limit_up_row
            cur_col = col_length - 1
            while cur_row < row_length:
                print(matrix[cur_row][cur_col], end=' ')
                cur_row += 1
                cur_col -= 1
            print()
            limit_up_row += 1
            limit_row += 1

    limit_bottom_col = 1
    limit_up_row = 1
    # 从第二行最右边开始打印
    while limit_up_row < row_length:
            cur_row = limit_up_row
            cur_col = limit_col - 1
            while cur_row < row_length and cur_col >= limit_bottom_col:
                print(matrix[cur_row][cur_col], end=' ')
                cur_row += 1
                cur_col -= 1
            print()
            limit_bottom_col += 1
            limit_up_row += 1


if __name__ == '__main__':
    mat = [
        [1, 2, 4, 10, 5],
        [2, 2, 4, 5, 4],
        [4, 2, 4, 5, 6],
        [0, 3, 4, 5, 3]
    ]

    print_maxtrix(mat)