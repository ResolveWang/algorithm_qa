"""
问题描述: 小易有n块砖块，每一块砖块有一个高度。小易希望利用这些砖块堆砌两座相同高度的塔。
为了让问题简单，砖块堆砌就是简单的高度相加，某一块砖只能使用在一座塔中一次。小易现在让能
够堆砌出来的两座塔的高度尽量高，小易能否完成呢。

输出描述:

如果小易能堆砌出两座高度相同的塔，输出最高能拼凑的高度，如果不能则输出-1. 保证答案不大于
500000。

示例1
输入
3 2 3 5
输出
5
"""


import sys


class Solution:
    def __init__(self):
        self.max_height = 500000
        self.height = 0

    def get_max_height(self, n, heights):
        heights.sort()
        sums = [0] * len(heights)
        for i in range(len(heights)):
            if i == 0:
                sums[i] = heights[0]
            else:
                sums[i] = sums[i-1] + heights[i]
        self.process(n-1, 0, 0, sums, heights)
        if not self.height:
            print(-1)
        else:
            print(self.height)

    def process(self, n, low, high, sums, heights):
        if low == high:
            self.height = max([low, self.height])

        if n < 0:
            return
        if low > self.max_height:
            return
        if low+sums[n] < high:
            return
        if low+high+sums[n] <= self.height*2:
            return

        self.process(n - 1, min([low+heights[n], high]), max([low+heights[n], high]), sums, heights)
        self.process(n - 1, min([high+heights[n], low]), max([high+heights[n], low]), sums, heights)
        self.process(n - 1, low, high, sums, heights)


if __name__ == '__main__':
    total = int(sys.stdin.readline().strip())
    args = list(map(int, sys.stdin.readline().strip().split()))
    s = Solution()
    s.get_max_height(total, args)