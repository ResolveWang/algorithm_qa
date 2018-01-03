"""
问题描述:给定一个无序数组arr,其中元素可正、可负、可0,给定一个整数k.求arr所有
的子数组中累加和小于或等于k的最长子数组长度.
例如: arr=[3,-2,-4,0,6],k=-2,相加和小于等于-2的最长子数组为[3,-2,-4,0],
所以结果返回４.
"""


class MaxLengthGetter:
    @classmethod
    def get_max_length(cls, arr, k):
        if not arr:
            return 0

        sum_arr = list()
        pre_sum = 0
        max_pre_sum = 0
        help_arr = list()
        for i in range(len(arr)):
            cur_sum = pre_sum + arr[i]
            sum_arr.append(cur_sum)
            pre_sum = cur_sum
            if i == 0:
                max_pre_sum = cur_sum
            else:
                max_pre_sum = max([max_pre_sum, cur_sum])
            help_arr.append(max_pre_sum)
        max_length = 0
        for i in range(len(arr)):
            diff = sum_arr[i] - k
            res = cls.bisect_select(help_arr[:i+1], diff)
            if res != -1:
                max_length = max([max_length, i - res + 1])

        return max_length

    @classmethod
    def bisect_select(cls, arr, k):
        left = 0
        right = len(arr) - 1
        res = -1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] >= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


if __name__ == '__main__':
    my_arr = [3, -2, -4, 0, 6]
    print(MaxLengthGetter.get_max_length(my_arr, -2))