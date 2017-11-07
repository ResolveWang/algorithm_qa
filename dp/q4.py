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
import time


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

    @classmethod
    def get_all_way_2(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return 0
        d = {}
        rs = cls.recurise_and_remember(arr, 0, aim, d)
        return rs

    @classmethod
    def recurise_and_remember(cls, arr, index, aim, mymap):
        res = 0
        if index == len(arr):
            if aim == 0:
                res = 1
            else:
                res = 0
        else:
            i = 0
            while arr[index]*i <= aim:
                mykey = '*'.join([str(index + 1), str(aim - arr[index] * i)])
                rs = mymap.get(mykey, 0)
                if rs == 0:
                    rs = cls.recurise_and_remember(arr, index + 1, aim - arr[index] * i, mymap)
                    mymap[mykey] = rs
                res += rs
                i += 1

        return res

    @classmethod
    def get_all_way_3(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return 0

        n = len(arr)
        dp = [[0 for _ in range(aim+1)] for _ in range(n)]

        i = 0
        while i < n:
            dp[i][0] = 1
            i += 1
        j = 0
        while arr[0]*j <= aim:
            dp[0][arr[0]*j] = 1
            j += 1

        i = 1
        while i < n:
            j = 1
            while j <= aim:
                num = 0
                k = 0
                while j - arr[i] * k >= 0:
                    num += dp[i-1][j-arr[i]*k]
                    k += 1
                dp[i][j] = num
                j += 1
            i += 1
        return dp[n-1][aim]

    @classmethod
    def get_all_way_4(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return 0

        n = len(arr)
        dp = [[0 for _ in range(aim+1)] for _ in range(n)]

        i = 0
        while i < n:
            dp[i][0] = 1
            i += 1
        j = 0
        while arr[0]*j <= aim:
            dp[0][arr[0]*j] = 1
            j += 1

        i = 1
        while i < n:
            j = 1
            while j <= aim:
                dp[i][j] = dp[i-1][j]
                if j - arr[i] >= 0:
                    dp[i][j] += dp[i][j-arr[i]]
                j += 1
            i += 1
        return dp[n-1][aim]

    @classmethod
    def get_all_way_5(cls, arr, aim):
        if not arr or len(arr) == 0 or aim < 0:
            return 0

        n = len(arr)
        dp = [0 for _ in range(aim+1)]

        i = 0
        while arr[0] * i <= aim:
            dp[arr[0] * i] = 1
            i += 1

        i = 1
        while i < n:
            j = 1
            while j <= aim:
                if j - arr[i] >= 0:
                    dp[j] += dp[j-arr[i]]
                j += 1
            i += 1
        return dp[aim]


if __name__ == '__main__':
    start_time = time.time()
    print(CoinsConstructer.get_all_way_1([10, 5, 1, 25], 1000))
    way1_end_time = time.time()
    print(CoinsConstructer.get_all_way_2([10, 5, 1, 25], 1000))
    way2_end_time = time.time()
    print(CoinsConstructer.get_all_way_3([10, 5, 1, 25], 1000))
    way3_end_time = time.time()
    print(CoinsConstructer.get_all_way_4([10, 5, 1, 25], 1000))
    way4_end_time = time.time()
    print(CoinsConstructer.get_all_way_4([10, 5, 1, 25], 1000))
    way5_end_time = time.time()

    print('way1 costs {} seconds'.format(way1_end_time - start_time))
    print('way2 costs {} seconds'.format(way2_end_time - way1_end_time))
    print('way3 costs {} seconds'.format(way3_end_time - way1_end_time))
    print('way3 costs {} seconds'.format(way4_end_time - way3_end_time))
    print('way3 costs {} seconds'.format(way5_end_time - way4_end_time))



