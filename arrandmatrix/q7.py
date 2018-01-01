"""
问题描述:给定一个有N*M的整型矩阵matrix和一个整数K,matrix的每一行
和每一列都是排好序的。实现一个函数，判断k是否在matrix中.

例如:
0  1  2  5
2  3  4  7
4  4  4  8
5  7  7  9

如果Ｋ为7,返回True；如果K为6,返回False.

要求:
时间复杂度为O(N+M),额外空间复杂度为O(1).
"""


class NumberFinder:
    @classmethod
    def find_num_in_matrix(cls, matrix, num):
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if matrix[row][col] == num:
                return True
            elif matrix[row][col] > num:
                col -= 1
            else:
                row += 1
        else:
            return False


if __name__ == '__main__':
    my_matrix = [
        [0, 1, 2, 3, 4, 5, 6],
        [10, 12, 13, 15, 16, 17, 18],
        [23, 24, 25, 26, 27, 28, 29],
        [166, 176, 186, 187, 190, 195, 200],
        [233, 243, 321, 341, 356, 370, 380]
    ]
    print(NumberFinder.find_num_in_matrix(my_matrix, 233))
    print(NumberFinder.find_num_in_matrix(my_matrix, 203))
