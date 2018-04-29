"""
问题: 实现 int sqrt(int x) 函数。计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例:
8 => 2
8 的平方根是 2.82842...,由于返回类型是整数，小数部分将被舍去。
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        num = 2
        start = 0
        end = 2
        while True:
            if x < num ** 2:
                num = (start + end) >> 1
                end = num
            elif num ** 2 <= x < (num + 1) ** 2:
                return num
            elif (num + 1) ** 2 == x:
                return num + 1
            elif x > (num + 1) ** 2:
                start = num + 1
                num *= 2
                end = num


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(8192))