"""
问题: 给定一个二维网格和一个单词，找出该单词是否存在于网格中。单词必须按照字母顺序，
通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同
一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
"""


class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                res = self.process(board, row, col, word, 0, [])
                if res:
                    return res
        return False

    def process(self, board, row, col, word, index, path):
        if board[row][col] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        if row < len(board) - 1 and (row + 1, col) not in path:
            res = self.process(board, row + 1, col, word, index + 1, path + [(row, col)])
            if res:
                return res

        if row > 0 and (row - 1, col) not in path:
            res = self.process(board, row - 1, col, word, index + 1, path + [(row, col)])
            if res:
                return res

        if col < len(board[0]) - 1 and (row, col + 1) not in path:
            res = self.process(board, row, col + 1, word, index + 1, path + [(row, col)])
            if res:
                return res

        if col > 0 and (row, col - 1) not in path:
            res = self.process(board, row, col - 1, word, index + 1, path + [(row, col)])
            if res:
                return res
        return False


