"""
问题描述: 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设
网格的四个边均被水包围。

示例

输入:
11000
11000
00100
00011

输出: 3
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        visited = set()

        row_length = len(grid)
        col_length = len(grid[0])
        row = 0
        count = 0
        while row < row_length:
            col = 0
            while col < col_length:
                if (row, col) in visited:
                    col += 1
                    continue

                if grid[row][col] == "1":
                    count += 1
                    tmp_queue = {(row, col)}
                    while tmp_queue:
                        tmp_row, tmp_col = tmp_queue.pop()
                        visited.add((tmp_row, tmp_col))
                        if grid[tmp_row][tmp_col] == '0':
                            continue

                        if tmp_row-1 >= 0 and (tmp_row-1, tmp_col) not in visited and \
                                (tmp_row-1, tmp_col) not in tmp_queue and \
                                grid[tmp_row - 1][tmp_col] == "1":
                            tmp_queue.add((tmp_row-1, tmp_col))
                        if tmp_row+1 < row_length and (tmp_row+1, tmp_col) not in visited and \
                                (tmp_row+1, tmp_col) not in tmp_queue and \
                                grid[tmp_row + 1][tmp_col] == "1":
                            tmp_queue.add((tmp_row+1, tmp_col))
                        if tmp_col-1 >= 0 and (tmp_row, tmp_col - 1) not in visited and \
                                (tmp_row, tmp_col-1) not in tmp_queue and \
                                grid[tmp_row][tmp_col-1] == "1":
                            tmp_queue.add((tmp_row, tmp_col - 1))
                        if tmp_col+1 < col_length and (tmp_row, tmp_col + 1) not in visited and \
                                (tmp_row, tmp_col+1) not in tmp_queue and \
                                grid[tmp_row][tmp_col+1] == "1":
                            tmp_queue.add((tmp_row, tmp_col + 1))
                else:
                    visited.add((row, col))
                col += 1
            row += 1

        return count



