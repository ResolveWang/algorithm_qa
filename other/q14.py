"""
问题描述:给定一个正数数组arr,其中所有的值都为整数,以下是最小不可组成和的概念:
1)把arr每个子集内的所有元素加起来会出现很多值,其中最小的记为min,最大的记为max.
2)在区间[min,max]上,如果有数不可以被arr某一个子集相加得到,那么其中最小的那个数是
arr的最小不可组成和.
3)在区间[min,max]上,如果所有的数都可以被arr的某一个子集相加得到,那么max+1是arr
的最小不可组成和.
请写函数返回正数数组arr的最小不可组成和.

举例:
arr=[3, 2, 5],子集{2}相加产生２为min，子集{3, 2, 5}相加产生10为max.在区间[2, 10]
上,4、６和9不能被任何子集相加得到,其中４是arr的最小不可组成和.
arr=[1,2,4]。子集{1}相加产生1为min，子集{1,2,4}相加产生7为max。在区间[1,7]上，任何
数都可以被子集相加得到，所以8是arr的最小不可组成和.

进阶题目:
如果已知正数数组arr中肯定有1这个数,是否能更快地得到最小不可组成和?
"""
import sys


class UnformedSum:
    @classmethod
    def unformed_sum(cls, arr):
        if not arr:
            return 1

        my_set = set()
        cls.process(arr, 0, 0, my_set)

        min_value = sys.maxsize
        for i in arr:
            min_value = min([min_value, i])

        i = min_value
        while True:
            if i not in my_set:
                return i
            i += 1

    @classmethod
    def process(cls, arr, index, cur_sum, cur_set):
        if index == len(arr):
            cur_set.add(cur_sum)
            return

        cls.process(arr, index+1, cur_sum+arr[index], cur_set)
        cls.process(arr, index+1, cur_sum, cur_set)

    @classmethod
    def unformed_sum_dp(cls, arr):
        if not arr:
            return 1
        max_sum = sum(arr)
        min_value = min(arr)
        dp = [False for _ in range(max_sum+1)]
        dp[0] = True
        for i in arr:
            dp[i] = True

        for i in range(len(arr)):
            for j in range(arr[i]+1, max_sum-arr[i]+1):
                if dp[j] is True:
                    dp[j+arr[i]] = True

        for i in range(min_value, len(dp)):
            if not dp[i]:
                return i

        return max_sum+1

    @classmethod
    def unformed_sum_contined_1(cls, arr):
        if not arr:
            return 1

        sorted_arr = sorted(arr)
        sum_val = 0
        for i in range(len(sorted_arr)):
            if sum_val + 1 < sorted_arr[i]:
                return sum_val + 1
            sum_val += arr[i]

        return sum_val + 1


if __name__ == '__main__':
    print(UnformedSum.unformed_sum_dp([3, 2, 5]))
    print(UnformedSum.unformed_sum_dp([1, 2, 4]))
    print(UnformedSum.unformed_sum_contined_1([1, 2, 4]))