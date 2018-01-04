"""
问题描述:给定一个数组arr,返回子数组的最大累加和.

例如:
arr=[1, -2, 3, 5, -2, 6, -1],所有的子数组中,[3, 5, -2, 6]可以累加出
最大的和12,所以返回12.

要求:
如果arr长度为N,要求时间复杂度为O(N),额外空间复杂度为O(1).
"""


class MaxSum:
    @classmethod
    def get_max_sum(cls, arr):
        if not arr:
            return 0

        sum_arr = []
        for i in range(len(arr)):
            if i == 0:
                sum_arr.append(arr[i])
            else:
                if sum_arr[i-1] < 0:
                    sum_arr.append(arr[i])
                else:
                    sum_arr.append(arr[i]+sum_arr[i-1])

        return max(sum_arr)


if __name__ == '__main__':
    my_arr = [-2, -3, -5, -1]
    print(MaxSum.get_max_sum(my_arr))