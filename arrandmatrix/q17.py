"""
问题描述:给定一个矩阵matrix,其中的值有正、负和0,返回子矩阵的最大累加和.

例如,矩阵matrix为
-90  48  78
64   -40 64
-81  -7  66
其中,最大累加和的子矩阵为:
48  78
-40 64
-7  66
所以返回累加和209.

例如,matrix为:
-1  -1  -1
-1  2   2
-1  -1  -1

其中,最大累加和的子矩阵为:
2  2
所以返回累加和为4.
"""
import sys
from arrandmatrix.q16 import MaxSum


class MaxMatrixSum:
    @classmethod
    def get_max_sum(cls, matrix):
        if not matrix:
            return 0

        max_value = -sys.maxsize

        for i in range(len(matrix)):
            j = i
            pre_arr = [0 for _ in range(len(matrix[0]))]
            while j < len(matrix):
                arr = cls.arr_add(matrix[j], pre_arr)
                max_value = max([MaxSum.get_max_sum(arr), max_value])
                j += 1
                pre_arr = arr

        return max_value

    @classmethod
    def arr_add(cls, arr1, arr2):
        return [arr1[i]+arr2[i] for i in range(len(arr1))]


if __name__ == '__main__':
    my_matrix = [
        [-90, 48, 78],
        [64, -40, 64],
        [-81, -7, 66]
    ]

    print(MaxMatrixSum.get_max_sum(my_matrix))