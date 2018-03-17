"""
问题描述:一条直线上有居民点，邮局只能建在居民点上。给定一个有序整型数组arr,
每个值代表居民点的一维坐标，再给定一个正数num，表示邮局数量。选择num个居民
点建立num个邮局，使所有的居民点到邮局的总距离最短，返回最短的总距离。

举例：
arr=[1,2,3,4,5,1000],num=2
第一个邮局建立在3位置,第二个建立在1000位置,那么1位置到邮局距离为2,2位置到
邮局距离为1,3位置到邮局距离为0,4位置到邮局距离为1,5位置到邮局距离为2,1000位置
到邮局距离为0.这种方案下,距离最短,为6,所以返回6
"""
import sys


class PostAddress:
    @classmethod
    def solution_by_dp(cls, arr, num):
        if not arr or num < 1 or len(arr) <= num:
            return 0

        length = len(arr)
        w = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        for i, _ in enumerate(arr):
            j = i + 1
            while j < length:
                w[i][j] = w[i][j - 1] + arr[j] - arr[int((i + j) / 2)]
                j += 1

        dp = [[0 for _ in range(length)] for _ in range(num)]
        for i in range(length):
            dp[0][i] = w[0][i]

        for i in range(1, num):
            for j in range(i + 1, length):
                dp[i][j] = sys.maxsize
                for k in range(j + 1):
                    dp[i][j] = min([dp[i][j], dp[i - 1][k] + w[k + 1][j]])

        return dp[num - 1][length - 1]


if __name__ == '__main__':
    print(PostAddress.solution_by_dp([1, 2, 3, 4, 5, 1000], 2))
