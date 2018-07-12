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
        # 排序过后从最高的砖块开始拿
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

        # 剪枝过程参考　https://blog.mythsman.com/2017/03/31/1/#堆砖块
        # 递归完成
        if n < 0:
            return
        # 高的一边比题目给的大
        if high > self.max_height:
            return
        # 矮的加剩下的比高的小
        if low+sums[n] < high:
            return
        # 高的和矮的加剩下的不大于已知的方案
        if low+high+sums[n] <= self.height*2:
            return

        # 砖块放矮的一边，注意加了一块砖之后AB塔高矮可能发生变化
        self.process(n - 1, min([low+heights[n], high]), max([low+heights[n], high]), sums, heights)
        # 砖块如果放高的一边或者丢弃，那么AB塔相对高矮程度不会变化
        self.process(n - 1, low, high+heights[n], sums, heights)
        self.process(n - 1, low, high, sums, heights)


if __name__ == '__main__':
    total = int(sys.stdin.readline().strip())
    args = list(map(int, sys.stdin.readline().strip().split()))
    s = Solution()
    s.get_max_height(total, args)