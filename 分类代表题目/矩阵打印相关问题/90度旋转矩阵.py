"""
问题描述: 给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一
个矩阵来旋转图像。

技巧:
顺时针旋转: 先将矩阵进行上下行对称交换，然后再以左上到右下的对角线为对称轴进
行元素交换，比如
 1 2 3     7 8 9     7 4 1
 4 5 6  => 4 5 6  => 8 5 2
 7 8 9     1 2 3     9 6 3

逆时针旋转: 将矩阵进行左右对称交换，再以左上到右下的对角线为对称轴进行元素交换，
比如
1 2 3     3 2 1     3 6 9
4 5 6  => 6 5 4  => 2 5 8
7 8 9     9 8 7     1 4 7
"""


class Rotation:
    def matrix_rotate(self, matrix):
        """顺时针交换"""
        matrix.reverse()
        n = len(matrix[0])
        for i in range(n):
            for j in range(n):
                if j < i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def matrix_rotate2(self, matrix):
        """逆时针交换"""
        for row in matrix:
            row.reverse()
        n = len(matrix[0])
        for i in range(n):
            for j in range(n):
                if j < i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution = Rotation()
    solution.matrix_rotate2(matrix)
    print(matrix)