"""
问题描述：给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来
就是路径和，返回所有的路径中最小的路径和。比如，给定m如下：
1 3 5 9
8 1 3 4
5 0 6 1
8 8 4 0
路径1， 3， 1， 0， 6， 1， 0是所有路径中路径和最小的，所以返回12.
"""


class ShortestWay:
    @classmethod
    def find_shortest_way_1(cls, arr):
        if arr is None or len(arr) == 0:
            return 0

        my_arr = list()
        row_count = len(arr)
        col_count = len(arr[0])
        for row in arr:
            my_arr.append([0 for _ in row])

        for i in range(col_count):
            if i == 0:
                my_arr[0][i] = arr[0][i]
            else:
                my_arr[0][i] = arr[0][i] + my_arr[0][i-1]

        for i in range(row_count):
            if i == 0:
                continue
            else:
                my_arr[i][0] = arr[i][0] + my_arr[i-1][0]

        for row in range(1, row_count):
            for col in range(1, col_count):
                my_arr[row][col] = min((my_arr[row-1][col], my_arr[row][col-1])) + arr[row][col]

        return my_arr[row_count-1][col_count-1]

    @classmethod
    def find_shortest_way_2(cls, arr):
        if arr is None or len(arr) == 0:
            return 0
        my_arr = list()
        row_count = len(arr)
        col_count = len(arr[0])
        length = min([row_count, col_count])
        for _ in range(length):
            my_arr.append(0)

        if row_count > col_count:
            for i in range(row_count):
                for j in range(col_count):
                    if i == 0 and j == 0:
                        my_arr[j] = arr[0][0]
                    else:
                        if i == 0:
                            my_arr[j] = my_arr[j-1] + arr[0][j]
                        else:
                            if j != 0:
                                my_arr[j] = min([my_arr[j-1], my_arr[j]]) + arr[i][j]
                            else:
                                my_arr[j] = arr[i][j] + my_arr[j]

        if row_count <= col_count:
            for i in range(col_count):
                for j in range(row_count):
                    if i == 0 and j == 0:
                        my_arr[j] = arr[0][0]
                    else:
                        if i == 0:
                            my_arr[j] = my_arr[j-1] + arr[j][0]
                        else:
                            if j != 0:
                                my_arr[j] = min([my_arr[j-1], my_arr[j]]) + arr[j][i]
                            else:
                                my_arr[j] = arr[j][i] + my_arr[j]

        return my_arr[-1]


if __name__ == '__main__':
    m = [
            [1, 3, 5, 9],
            [8, 1, 3, 4],
            [5, 0, 6, 1],
            [8, 8, 4, 0]
    ]

    print(ShortestWay.find_shortest_way_1(m))
    print(ShortestWay.find_shortest_way_2(m))