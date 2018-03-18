"""
问题描述:给定一个整型数组arr,数组中每个值为正数，表示完成一幅画作需要的时间，
再给定一个整数num表示画匠的数量，每个画匠只能画连在一起的画作。所有的画家并行
工作，请返回完成所有的画作需要的最小时间。

举例:
arr=[3,1,4], num=2
最好的分配方式是为第一个画匠3和1,第二个画匠4，所需时间是4

arr=[1,1,1,4,3], num=3
最好的分配方式是第一个画匠画前三个1,所需时间为3。第二个画匠画4,第三个画匠画3,
返回4
"""
import sys


class LimnerProblem:
    @classmethod
    def best_solution(cls, arr, num):
        if not arr or num < 1:
            return 0

        if len(arr) <= num:
            return max(arr)
        else:
            min_value = 0
            max_value = sum(arr)
            while max_value != min_value + 1:
                mid = int((min_value + max_value) / 2)
                if cls.get_num(arr, mid) > num:
                    min_value = mid
                else:
                    max_value = mid

            return max_value

    @classmethod
    def get_num(cls, arr, limit):
        if max(arr) > limit:
            return sys.maxsize

        step = 0
        res = 1
        for i in arr:
            step += i
            if step > limit:
                res += 1
                step = i
        return res

    @classmethod
    def solution_by_dp(cls, arr, num):
        if not arr or num < 1:
            return 0

        dp = [[0 for _ in arr] for _ in range(num)]
        for i, _ in enumerate(arr):
            dp[0][i] = sum(arr[:i + 1])

        for i in range(1, num):
            j = 1
            while j < len(arr):
                min_value = sys.maxsize
                for k in range(j):
                    dp[i][j] = min([max([dp[i-1][k], sum(arr[k+1:j+1])]), min_value])
                    min_value = dp[i][j]
                j += 1

        return dp[num-1][len(arr)-1]


if __name__ == '__main__':
    print(LimnerProblem.best_solution([1, 1, 1, 4, 3], 3))
    print(LimnerProblem.solution_by_dp([1, 1, 1, 4, 3], 3))
