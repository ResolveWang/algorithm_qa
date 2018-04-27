"""
问题: 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

比如:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return list()

        res = list()
        left_up_row = 0
        left_up_col = 0
        right_down_row = len(matrix) - 1
        right_down_col = len(matrix[0]) - 1
        # 注意和矩阵相关的遍历和打印问题，边界条件左上和右下的横纵坐标都得考虑
        while left_up_row <= right_down_row and left_up_col <= right_down_col:
            cur_row = left_up_row
            cur_col = left_up_col
            if left_up_row != right_down_row and left_up_col != right_down_col:
                while cur_col < right_down_col:
                    res.append(matrix[cur_row][cur_col])
                    cur_col += 1
                while cur_row < right_down_row:
                    res.append(matrix[cur_row][cur_col])
                    cur_row += 1
                while cur_col > left_up_col:
                    res.append(matrix[cur_row][cur_col])
                    cur_col -= 1
                while cur_row > left_up_row:
                    res.append(matrix[cur_row][cur_col])
                    cur_row -= 1
            elif left_up_row == right_down_row:
                while cur_col <= right_down_col:
                    res.append(matrix[cur_row][cur_col])
                    cur_col += 1
            elif left_up_col == right_down_col:
                while cur_row <= right_down_row:
                    res.append(matrix[cur_row][cur_col])
                    cur_row += 1
            right_down_col -= 1
            right_down_row -= 1
            left_up_col += 1
            left_up_row += 1
        return res


if __name__ == '__main__':
    matrix = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    solution = Solution()
    print(solution.spiralOrder(matrix))

