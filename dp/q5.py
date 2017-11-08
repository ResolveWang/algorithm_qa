"""
问题描述：给定数组arr,返回arr的最长递增子序列。比如
arr=[2, 1, 5, 3, 6, 4, 8, 9, 7],返回的最长递增子序列为[1, 3, 4, 8, 9]

要求：如果arr长度为N,请实现时间复杂度为O(NlogN)的方法
"""


class MaxSubSeq:
    @classmethod
    def find_dp_way_1(cls, arr):
        """复杂度为O(N^2)"""
        dp = [1 for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max([dp[j]+1, dp[i]])

        return dp

    @classmethod
    def get_res_list_1(cls, arr):
        if not arr:
            return

        dp = cls.find_dp_way_1(arr)
        return cls.common_compute(arr, dp)

    @classmethod
    def common_compute(cls, arr, dp):
        max_len = max(dp)
        index = 0
        for ind, value in enumerate(dp):
            if value == max_len:
                index = ind
                break

        res = list()
        temp = index
        res.insert(0, arr[index])
        while temp >= 0:
            if arr[temp] < arr[index] and dp[temp] == dp[index] - 1:
                res.insert(0, arr[temp])
                index = temp
            temp -= 1

        return res

    @classmethod
    def get_res_list_2(cls, arr):
        if not arr:
            return

        dp = cls.find_dp_way_2(arr)
        return cls.common_compute(arr, dp)

    @classmethod
    def find_dp_way_2(cls, arr):
        dp = [0 for _ in range(len(arr))]
        ends = [0 for _ in range(len(arr))]
        ends[0] = arr[0]
        dp[0] = 1

        right = 0

        for i in range(1, len(arr)):
            l = 0
            r = right
            while l <= r:
                m = int((l + r)/2)
                if arr[i] > ends[m]:
                    l = m + 1
                else:
                    r = m - 1
            right = max([l, right])
            ends[l] = arr[i]
            dp[i] = l + 1

        return dp


if __name__ == '__main__':
    print(MaxSubSeq.get_res_list_1([2, 1, 5, 3, 6, 4, 8, 9, 7]))
    print(MaxSubSeq.get_res_list_2([2, 1, 5, 3, 6, 4, 8, 9, 7]))