"""
问题描述：给定数组arr，arr中的所有值都为正数且不重复。每个值代表一种面值的货币，每种
面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱有多少种方法。

举例：
arr=[5, 10 ,25, 1], aim=0
组成0元的方法有1种，就是所有面值的货币都不用，所以返回1.
arr=[5, 10, 25, 1], aim=5
组成15元的方法有6种，分别为3张5元、1张10元+1张5元、1张10元+5张1元、10张1元+1张5元、
2张5元+5张1元和15张1元。所以返回6.
arr=[3, 5], aim=2
任何方法都无法组成2元，所以返回0.
"""


class CoinsConstructer:
    @classmethod
    def get_all_way_1(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return 0

        return cls.recurise_count(arr, 0, aim)

    @classmethod
    def recurise_count(cls, arr, index, aim):
        res = 0
        if index == len(arr):
            if aim == 0:
                res = 1
            else:
                res = 0
        else:
            i = 0
            while arr[index]*i <= aim:
                res += cls.recurise_count(arr, index + 1, aim - arr[index] * i)
                i += 1

        return res


if __name__ == '__main__':
    print(CoinsConstructer.get_all_way_1([10, 5, 1, 25], 1000))




