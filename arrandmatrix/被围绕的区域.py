"""
问题:给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连
的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

思路:
从特性出发，边界区域的'O'不可能被包围，它相邻的'O'不会被包围，以此类推，获取所有不会被包围的点，然后遍历把除这些点以外的
所有点都变成'X'
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        row_length = len(board)
        col_length = len(board[0])

        if row_length <= 1 or col_length <= 1:
            return

        row, col = 0, 0
        unreachable = set()
        res = set()

        while col < col_length:
            if board[row][col] == 'O':
                unreachable.add((row, col))
            col += 1

        col -= 1
        while row < row_length:
            if board[row][col] == 'O':
                unreachable.add((row, col))
            row += 1

        row -= 1
        while col >= 0:
            if board[row][col] == 'O':
                unreachable.add((row, col))
            col -= 1

        col = 0
        while row >= 0:
            if board[row][col] == 'O':
                unreachable.add((row, col))
            row -= 1

        while unreachable:
            row, col = unreachable.pop()
            res.add((row, col))
            if col - 1 >= 0:
                if board[row][col - 1] == 'O' and (row, col - 1) not in res and (row, col - 1) not in unreachable:
                    unreachable.add((row, col - 1))
            if col + 1 < col_length:
                if board[row][col + 1] == 'O' and (row, col + 1) not in res and (row, col + 1) not in unreachable:
                    unreachable.add((row, col + 1))
            if row - 1 >= 0:
                if board[row - 1][col] == 'O' and (row - 1, col) not in res and (row - 1, col) not in unreachable:
                    unreachable.add((row - 1, col))
            if row + 1 < row_length:
                if board[row + 1][col] == 'O' and (row + 1, col) not in res and (row + 1, col) not in unreachable:
                    unreachable.add((row + 1, col))

        row = 1
        while row < row_length:
            col = 1
            while col < col_length:
                if board[row][col] == 'O' and not (row, col) in res:
                    board[row][col] = 'X'
                col += 1
            row += 1




