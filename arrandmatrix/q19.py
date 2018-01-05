"""
问题描述:给定一个double类型的数组arr，其中的元素可正、可负、可0，返回子数组累乘的最大
乘积。

例如:
arr=[-2.5,4,0,3,0.5,8,-1],子数组[3,0.5,8]累乘可以获得最大的乘积12,所以返回12.
"""


class SubArrMaxSum:
    @classmethod
    def get_max_sum(cls, arr):
        if not arr:
            return

        if len(arr) == 1:
            return arr[0]

        pre_max = arr[0]
        pre_min = arr[0]
        res = arr[0]

        for i in range(1, len(arr)):
            end_max = pre_max * arr[i]
            end_min = pre_min * arr[i]

            pre_max = max([arr[i], end_max, end_min])
            pre_min = min([arr[i], end_max, end_min])

            res = max([res, pre_max])

        return res


if __name__ == '__main__':
    my_arr = [-2.5, 4, 0, 3, 0.5, 8, -1]
    print(SubArrMaxSum.get_max_sum(my_arr))
