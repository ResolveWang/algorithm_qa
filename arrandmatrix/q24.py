"""
问题描述:用一个整型矩阵matrix表示一个网络，１代表有路，０代表无路，
每个位置只要不越界，都有上下左右４个方向，求从最左上角到最右下角的最短通路值。

例如:
matrix为:
1  0  1  1  1
1  0  1  0  1
1  1  1  0  1
0  0  0  0  1

通路只有一条，由12个1构成，所以返回12.
"""


class ShortestPath:
    @classmethod
    def get_shortest_path(cls, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0 or \
                matrix[0][0] != 1 or matrix[-1][-1] != 1:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        path_map = [[0 for _ in range(col)] for _ in range(row)]
        path_map[0][0] = 1

        rq = list()
        cq = list()

        rq.append(0)
        cq.append(0)

        while len(rq) > 0 and len(cq) > 0:
            r = rq.pop(0)
            c = cq.pop(0)

            if r == row - 1 and c == col - 1:
                return path_map[r][c]

            cls.walk(path_map[r][c], r-1, c, matrix, path_map, rq, cq)
            cls.walk(path_map[r][c], r+1, c, matrix, path_map, rq, cq)
            cls.walk(path_map[r][c], r, c-1, matrix, path_map, rq, cq)
            cls.walk(path_map[r][c], r, c+1, matrix, path_map, rq, cq)

        return 0

    @classmethod
    def walk(cls, pre_length, to_row, to_col, matrix, path_map, rq, cq):
        if to_row < 0 or to_col < 0 or to_row >= len(matrix) or \
                to_col >= len(matrix[0]):
            return

        if matrix[to_row][to_col] == 0 or path_map[to_row][to_col] != 0:
            return

        cur_length = pre_length + 1
        path_map[to_row][to_col] = cur_length
        rq.append(to_row)
        cq.append(to_col)


if __name__ == '__main__':
    my_matrix = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]

    print(ShortestPath.get_shortest_path(my_matrix))