"""
问题描述:给定一个整型数组arr,返回不包含本位置值的累乘数组.

例如:
arr=[2, 3, 1, 4],它的累乘数组是[12, 8, 24, 6]

要求:
1.时间复杂度为O(N)
2.除需要返回的结果数组外,额外空间复杂度为O(1)

进阶:
对时间和空间复杂度都不变,要求不能用除法
"""


class ArrProduct:
    @classmethod
    def get_product_by_div(cls, arr):
        if not arr or len(arr) < 2:
            return

        all_value = 1
        res = [0 for _ in range(len(arr))]
        count_zero = 0
        zero_index = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                count_zero += 1
                zero_index = i
            else:
                all_value = arr[i] * all_value

        if count_zero > 1:
            pass
        elif count_zero == 1:
            res[zero_index] = all_value
        else:
            for i in range(len(arr)):
                res[i] = int(all_value/arr[i])

        return res

    @classmethod
    def get_product(cls, arr):
        if not arr or len(arr) < 2:
            return

        res = [0 for _ in range(len(arr))]
        res[0] = arr[0]

        for i in range(1, len(arr)):
            res[i] = res[i-1] * arr[i]

        tmp = 1
        for i in range(len(arr)-1, 0, -1):
            if i == len(arr) - 1:
                res[i] = res[i-1]
            else:
                tmp *= arr[i+1]
                res[i] = res[i-1] * tmp

        res[0] = tmp
        return res


if __name__ == '__main__':
    my_arr = [1, 2, 3, 4]
    print(ArrProduct.get_product_by_div(my_arr))
    print(ArrProduct.get_product(my_arr))